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
        if self.base64 and len(self.base64) > 0:
            base64_decoded = base64.b64decode(self.base64)
            image = Image.open(io.BytesIO(base64_decoded))
            self.width = image.width
            self.height = image.height
            self.img = np.array(image)
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
