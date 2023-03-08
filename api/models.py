from django.db import models


class Version(models.Model):
    major = models.PositiveIntegerField(verbose_name="MAJOR", default=0)
    minor = models.PositiveIntegerField(verbose_name="MINOR", default=0)
    patch = models.PositiveIntegerField(verbose_name="PATCH", default=1)

    def __str__(self):
        return str(self.major)+"."+str(self.minor)+"."+str(self.patch)

    def json(self):
        return {
            "Major": self.major,
            "Minor": self.minor,
            "Patch": self.patch,
            "Version": self.__str__()
        }
