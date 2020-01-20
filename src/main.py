# Project imports
from vector import *
from ray import Ray
from camera import Camera
from sphere import Sphere
from hittable_list import Hittable_List
from hittable import HitRecord
from material import *

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


def color(r, world, depth):
    # Introducing depth to control how deep we want the rays to keep bouncing off
    hit_record = HitRecord()
    # MAXFLOAT in C++
    if world.hit(r, 0.001, sys.float_info.max, hit_record):
        # -1 < t < 1 to 0 < t < 1
        # Replacing all the code with the material class created
        scattered = Ray(origin=Vector3(0.0, 0.0, 0.0), direction=Vector3(0.0, 0.0, 0.0))
        hit = hit_record.material.scatter(r, hit_record, scattered)
        if depth < 50 and hit[0]:
            return color(scattered, world, depth+1).mul(hit[1])
        else:
            return Vector3(0.0, 0.0, 0.0)
    else:
        unit_direction = unit_vector(r.direction)
        # Graphics trick of scaling it to 0.0 < y < 1.0
        t = 0.5 * (unit_direction.y + 1.0)
        # Lerping between (255, 255, 255) which is white to a light shade blue (128, 255*0.7, 255)
        return Vector3(1.0, 1.0, 1.0) * (1.0 - t) + Vector3(0.5, 0.7, 1.0) * t


def create_scene():

    n = 500
    object_list = [Sphere(Vector3(0, -1000, 0), 1000, Lambertian(Vector3(0.19, 0.78, 0.78)))]
    i = 1
    for a in range(-11, 11, 1):
        for b in range(-11, 11, 1):
            choose_mat = random.random()
            center = Vector3(a+0.9*random.random(), 0.2, b+0.9*random.random())
            if (center - Vector3(4.0, 0.2, 0)).length > 0.9:
                if choose_mat < 0.8:  # Diffuse
                    object_list.append(Sphere(center, 0.2,
                                            Lambertian(Vector3(random.random(),
                                                               random.random(),
                                                               random.random()))))
                else:  # Metal
                    object_list.append(Sphere(center, 0.2,
                                            Metal(Vector3(0.5*(1 + random.random()),
                                                          0.5*(1 + random.random()),
                                                          0.5*(1 + random.random())),
                                                  0.5 * random.random())))
    object_list.append(Sphere(Vector3(0.0, 1.0, 0.0), 1.0, Metal(Vector3(0.7, 0.6, 0.5), 0.95)))
    object_list.append(Sphere(Vector3(-4.0, 1.0, 0.0), 1.0, Lambertian(Vector3(0.4, 0.2, 0.1))))
    object_list.append(Sphere(Vector3(4.0, 1.0, 0.0), 1.0, Metal(Vector3(0.7, 0.6, 0.5), 0.0)))

    return object_list


def ray_camera_background():
    path = os.path.join(os.path.dirname(__file__), "..", "images", "last_scene_4.ppm")
    ppm_file = open(path, 'w')
    rows = 1200
    columns = 800
    samples = 10  # Too much for Python
    title = "P3\n{r} {c}\n255\n".format(r=rows, c=columns)
    ppm_file.write(title)
    # Creating two sphere and making a world out of those hittable objects
    r = math.cos(math.pi/4.0)
    object_list = create_scene()
    world = Hittable_List(object_list)
    # Defining camera parameters
    lookfrom = Vector3(13.0, 2.0, 3.0)
    lookat = Vector3(0.0, 0.0, 0.0)
    focus_distance = 10.0
    aperture = 0.1
    main_camera = Camera(lookfrom, lookat, Vector3(0.0, 1.0, 0.0),
                         20, float(rows)/float(columns), aperture, focus_distance)
    for j in range(columns-1, -1, -1):
        for i in range(0, rows, 1):
            col = Vector3(0.0, 0.0, 0.0)
            for s in range(0, samples, 1):
                u = float(i + random.random())/float(rows)
                v = float(j + random.random())/float(columns)
                rayr = main_camera.get_ray(u, v)
                col = color(rayr, world, 0) + col

            # Averaging out
            col = col/samples
            col = Vector3(math.sqrt(col.r), math.sqrt(col.g), math.sqrt(col.b))
            ir = int(255.99*col.r)
            ig = int(255.99*col.g)
            ib = int(255.99*col.b)
            value = "{ir} {ig} {ib}\n".format(ir=ir, ig=ig, ib=ib)
            ppm_file.write(value)
        print("Column {0} Row {1} done!".format(j, i))
    ppm_file.close()


if __name__ == '__main__':
    start_time = time.time()
    ray_camera_background()
    print(time.time() - start_time)
