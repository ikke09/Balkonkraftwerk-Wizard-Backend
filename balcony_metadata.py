import base64

import cv2
import numpy as np

from models import BalconyImageIn, BalconyImageOut, Corner, Boundary


def _prepare_image(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    ret, img_binary = cv2.threshold(
        img_blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return img_binary


def _find_contour(img) -> tuple[Boundary, int]:
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    best_cnt_area = -1
    best_cnt_rect: tuple[int, int, int, int] = (0, 0, 0, 0)
    for cnt in contours:
        rect = cv2.boundingRect(cnt)
        area = rect[2]*rect[3]  # width * height
        if area > best_cnt_area:
            best_cnt_area = area
            best_cnt_rect = rect
    boundary = Boundary(
        x=best_cnt_rect[0], y=best_cnt_rect[1], w=best_cnt_rect[2], h=best_cnt_rect[3])
    return (boundary, best_cnt_area)


def _get_corners(rect) -> list[Corner]:
    x, y, w, h = rect
    return [Corner(x=x, y=y), Corner(x=x+w, y=y), Corner(x=x+w, y=y+h), Corner(x=x, y=y+h)]


def _base64_to_image(data: str):
    base64_decoded = base64.b64decode(data)
    nparr = np.fromstring(string=base64_decoded, dtype=np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)


def extract_metadata(balcony: BalconyImageIn) -> BalconyImageOut | None:
    if not balcony or not balcony.base64 or balcony.base64 == '':
        return None

    res = BalconyImageOut()
    img = _base64_to_image(balcony.base64)
    if img is None or len(img) == 0:
        return None

    img_prep = _prepare_image(img)
    rect, area = _find_contour(img_prep)
    res.corners = _get_corners(rect)
    res.area = area
    res.boundary = rect
    return res
