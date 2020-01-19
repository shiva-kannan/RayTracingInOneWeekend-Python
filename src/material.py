"""material.py: Abstract class for material"""

__author__ = "Shiva Kannan"

from abc import ABC, abstractmethod
from vector import *
import random
from ray import Ray


def random_in_unit_sphere():
    # The rejection method to get a random point inside a unit radius sphere centred at origin
    p = Vector3(random.random(), random.random(), random.random())*2 - Vector3(1.0, 1.0, 1.0)
    while p.squared_length >= 1.0:
        p = Vector3(random.random(), random.random(), random.random())*2 - Vector3(1.0, 1.0, 1.0)
    return p


def reflect(in_vector, normal):

    return in_vector - normal * (dot(in_vector, normal) * 2)


class Material(ABC):

    @abstractmethod
    def scatter(self, ray_in, hit_record, scattered):
        pass


class Lambertian(Material):

    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, ray_in, hit_record, scattered):
        target = hit_record.p + hit_record.normal + random_in_unit_sphere()
        scattered.origin = hit_record.p
        scattered.direction = target - hit_record.p
        # attenuation = self.albedo
        return True, self.albedo


class Metal(Material):

    def __init__(self, albedo, fuzz):
        self.albedo = albedo
        if fuzz < 1: self.fuzz = fuzz
        else: self.fuzz = 1

    def scatter(self, ray_in, hit_record, scattered):
        reflected = reflect(unit_vector(ray_in.direction), hit_record.normal)
        scattered.origin = hit_record.p
        scattered.direction = reflected + random_in_unit_sphere() * self.fuzz
        # attenuation = self.albedo
        return dot(scattered.direction, hit_record.normal) > 0, self.albedo
