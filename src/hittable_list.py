"""hittable_list.py: Implementation of array of 'hittable' object"""

__author__ = "Shiva Kannan"

from hittable import Hittable, HitRecord
from vector import *


class Hittable_List(Hittable):
    def __init__(self, hittable_objects):
        self.hittable_objects = hittable_objects

    def hit(self, ray, t_min, t_max, hit_record):
        # Initializing a temp hit record variable
        tmp_hit_rec = HitRecord()
        hit_anything = False
        closest_so_far = t_max
        for item in self.hittable_objects:
            if item.hit(ray, t_min, closest_so_far, tmp_hit_rec):
                hit_anything = True
                closest_so_far = tmp_hit_rec.t
                hit_record.t = tmp_hit_rec.t
                hit_record.p = tmp_hit_rec.p
                hit_record.normal = tmp_hit_rec.normal
        return hit_anything
