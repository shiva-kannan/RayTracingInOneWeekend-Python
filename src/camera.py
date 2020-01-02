"""camera.py: Main Camera Class"""

__author__ = "Shiva Kannan"

from ray import *
from vector import Vector3


class Camera:

    def __init__(self):
        self.lower_left_corner = Vector3(-2.0, -1.0, -1.0)
        self.horizontal = Vector3(4.0, 0.0, 0.0)
        self.vertical = Vector3(0.0, 2.0, 0.0)
        self.origin = Vector3(0.0, 0.0, 0.0)

    def get_ray(self, u, v):
        """
        Rays from camera to scene moved along u and v offset vectors
        :param u: Horizontal movement
        :param v: Vertical movement
        :return: Offset ray object
        """

        return Ray(origin=self.origin,
                   direction=self.lower_left_corner + self.horizontal*u + self.vertical*v - self.origin)
