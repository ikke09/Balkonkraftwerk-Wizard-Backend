from PIL import Image
import base64
import io
import numpy as np


class BalconyModel():

    def __init__(self, data: dict):
        self.base64 = data.get('img', '')
        self.img = None
        self.width = int(data.get('width', 0))
        self.height = int(data.get('height', 0))
        self.url = data.get('url', '')

    def json(self):
        return {
            "Image": self.base64,
            "Url": self.url,
            "Width": self.width,
            "Height": self.height
        }


class VersionModel():

    def __init__(self, major=0, minor=0, patch=1):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        return str(self.major)+"."+str(self.minor)+"."+str(self.patch)

    def json(self):
        return {
            "Major": self.major,
            "Minor": self.minor,
            "Patch": self.patch,
            "Version": self.__str__()
        }

class Corner():

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def json(self):
        return {
            'X': self.x,
            'Y': self.y
        }


class BalconyResult():

    def __init__(self) -> None:
        self.area = 0
        self.boundary = None
        self.corners: list[Corner] = None

    def json(self):
        return {
            'Area': self.area,
            'Width': self.boundary[2],
            'Height': self.boundary[3],
            'Corners': [c.json() for c in self.corners]
        }