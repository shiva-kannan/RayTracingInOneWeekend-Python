"""camera.py: Main Camera Class"""

__author__ = "Shiva Kannan"

from ray import *
from vector import Vector3


class Camera:

    def __init__(self, lookfrom, lookat, vup, vfov, aspect):
        self.theta = vfov * math.pi/180
        self.half_height = math.tan(self.theta/2)
        self.half_width = aspect * self.half_height
        self.origin = lookfrom
        w = unit_vector(lookfrom - lookat)
        u = unit_vector(cross(vup, w))
        v = cross(w, u)
        self.lower_left_corner = self.origin - u * self.half_width - v * self.half_height - w
        self.horizontal = u * self.half_width * 2
        self.vertical = v * self.half_height * 2

    def get_ray(self, u, v):
        """
        Rays from camera to scene moved along u and v offset vectors
        :param u: Horizontal movement
        :param v: Vertical movement
        :return: Offset ray object
        """

        return Ray(origin=self.origin,
                   direction=self.lower_left_corner + self.horizontal*u + self.vertical*v - self.origin)
