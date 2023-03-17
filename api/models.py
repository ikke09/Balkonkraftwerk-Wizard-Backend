
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


class BalconyCornerModel():
    def __init__(self, x=0.0, y=0.0) -> None:
        self.x = x
        self.y = y


class BalconyModel():
    def __init__(self) -> None:
        self.corners = []
        self.area = 0.0
        self.numbersOfSolarPanels = 0
