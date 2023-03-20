import base64
import io

import cv2
import numpy as np

from models import BalconyModel, BalconyResult

def _prepare_image(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    ret, img_binary = cv2.threshold(
        img_blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return img_binary


def _find_contour(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    best_cnt_area = -1
    best_cnt_rect = None
    for cnt in contours:
        rect = cv2.boundingRect(cnt)
        area = rect[2]*rect[3]  # width * height
        if area > best_cnt_area:
            best_cnt_area = area
            best_cnt_rect = rect
    return (best_cnt_rect, best_cnt_area)


def _get_corners(rect):
    x, y, w, h = rect
    return ((x, y), (x+w, y), (x+w, y+h), (x, y+h))


def _base64_to_image(data: str):
    base64_decoded = base64.b64decode(data)
    return np.frombuffer(io.BytesIO(base64_decoded))


def extract_metadata(balcony: BalconyModel) -> BalconyResult | None:
    if not balcony or not balcony.base64 or balcony.base64 == '':
        return None

    res = BalconyResult()
    img = _base64_to_image(balcony.base64)
    img_prep = _prepare_image(img)
    rect, area = _find_contour(img_prep)
    res.corners = _get_corners(rect)
    res.area = area
    res.boundary = rect
    return res
