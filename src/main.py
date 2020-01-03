# Project imports
from vector import *
from ray import Ray
from camera import Camera
from sphere import Sphere
from hittable_list import Hittable_List
from hittable import HitRecord

# Standard Libs
import os
import random
import sys
import time


def random_in_unit_sphere():
    # The rejection method to get a random point inside a unit radius sphere centred at origin
    p = Vector3(random.random(), random.random(), random.random())*2 - Vector3(1.0, 1.0, 1.0)
    while p.squared_length >= 1.0:
        p = Vector3(random.random(), random.random(), random.random())*2 - Vector3(1.0, 1.0, 1.0)
    return p


def color(r, world):
    hit_record = HitRecord()
    # MAXFLOAT in C++
    if world.hit(r, 0.001, sys.float_info.max, hit_record):
        # -1 < t < 1 to 0 < t < 1
        target = hit_record.p + hit_record.normal + random_in_unit_sphere()
        return color(Ray(hit_record.p, target - hit_record.p), world) * 0.5
    else:
        unit_direction = unit_vector(r.direction)
        # Graphics trick of scaling it to 0.0 < y < 1.0
        t = 0.5 * (unit_direction.y + 1.0)
        # Lerping between (255, 255, 255) which is white to a light shade blue (128, 255*0.7, 255)
        return Vector3(1.0, 1.0, 1.0) * (1.0 - t) + Vector3(0.5, 0.7, 1.0) * t
    # # Calculate the normal using the hit point
    # t = hit_sphere(Vector3(0.0, 0.0, -1.0), 0.5, r)
    # if t > 0.0:
    #     N = unit_vector(r.point_at_parameter(t) - Vector3(0.0, 0.0, -1.0))
    #     # Map the unit vector magnitudes to R/G/B : Most common way of showing normal
    #     return Vector3(N.x + 1.0, N.y + 1.0, N.z + 1.0) * 0.5
    # unit_direction = unit_vector(r.direction)


def ray_camera_background():
    path = os.path.join(os.path.dirname(__file__), "..", "images", "diffuse_with_gamma.ppm")
    ppm_file = open(path, 'w')
    rows = 200
    columns = 100
    samples = 100  # Too much for Python
    title = "P3\n{r} {c}\n255\n".format(r=rows, c=columns)
    ppm_file.write(title)
    # Creating two sphere and making a world out of those hittable objects
    object_list = [Sphere(Vector3(0.0, 0.0, -1.0), 0.5), Sphere(Vector3(0.0, -100.5, -1.0), 100.0)]
    world = Hittable_List(object_list)
    main_camera = Camera()
    for j in range(columns-1, -1, -1):
        for i in range(0, rows, 1):
            col = Vector3(0.0, 0.0, 0.0)
            for s in range(0, samples, 1):
                u = float(i + random.random())/float(rows)
                v = float(j + random.random())/float(columns)
                rayr = main_camera.get_ray(u, v)
                col = color(rayr, world) + col
            # Averaging out
            col = col/samples
            col = Vector3(math.sqrt(col.r), math.sqrt(col.g), math.sqrt(col.b))
            ir = int(255.99*col.r)
            ig = int(255.99*col.g)
            ib = int(255.99*col.b)
            value = "{ir} {ig} {ib}\n".format(ir=ir, ig=ig, ib=ib)
            ppm_file.write(value)
    ppm_file.close()


if __name__ == '__main__':
    start_time = time.time()
    ray_camera_background()
    print(time.time() - start_time)
