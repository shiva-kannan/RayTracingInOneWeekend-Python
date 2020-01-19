"""camera.py: Main Camera Class"""

__author__ = "Shiva Kannan"

from ray import *
from vector import Vector3
import random


# A similar implementation instead for a circle and not a sphere
def random_in_unit_disk():
    # The rejection method to get a random point inside a unit radius sphere centred at origin
    p = Vector3(random.random(), random.random(), 0.0)*2 - Vector3(1.0, 1.0, 0.0)
    while dot(p, p) >= 1.0:
        p = Vector3(random.random(), random.random(), 0.0)*2 - Vector3(1.0, 1.0, 0.0)
    return p


class Camera:

    def __init__(self, lookfrom, lookat, vup, vfov, aspect, aperture, focus_dist):
        self.lens_radius = aperture/2.0
        self.theta = vfov * math.pi/180
        self.half_height = math.tan(self.theta/2)
        self.half_width = aspect * self.half_height
        self.origin = lookfrom
        self.w = unit_vector(lookfrom - lookat)
        self.u = unit_vector(cross(vup, self.w))
        self.v = cross(self.w, self.u)
        self.lower_left_corner = self.origin\
                                 - self.u * self.half_width * focus_dist\
                                 - self.v * self.half_height * focus_dist\
                                 - self.w * focus_dist
        self.horizontal = self.u * self.half_width * focus_dist * 2
        self.vertical = self.v * self.half_height * focus_dist * 2

    def get_ray(self, s, t):
        """
        Rays from camera to scene moved along u and v offset vectors
        :param u: Horizontal movement
        :param v: Vertical movement
        :return: Offset ray object
        """

        rd = random_in_unit_disk() * self.lens_radius
        offset = self.u * rd.x + self.v * rd.y
        return Ray(origin=self.origin + offset,
                   direction=self.lower_left_corner + self.horizontal*s + self.vertical*t - self.origin - offset)
