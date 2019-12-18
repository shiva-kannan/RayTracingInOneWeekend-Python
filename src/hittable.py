"""hittable.py: Implementation of the Hittable abstract class"""

__author__ = "Shiva Kannan"

from abc import ABC, abstractmethod
from vector import Vector3


class Hittable(ABC):

    @abstractmethod
    def hit(self, ray, t_min, t_max, hit_record):
        pass


class HitRecord:
    def __init__(self, t=0.0, p=Vector3(0.0, 0.0, 0.0), normal=Vector3(0.0, 0.0, 0.0)):
        self.t = t
        self.p = p
        self.normal = normal
