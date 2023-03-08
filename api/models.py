
class Version():

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
