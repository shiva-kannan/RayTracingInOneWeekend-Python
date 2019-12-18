import os
from vector import *
from ray import Ray
from sphere import Sphere
from hittable_list import Hittable_List
from hittable import HitRecord
import sys

# @accepts(Vector3, float, Ray)
# def hit_sphere(center, radius, ray):
#     oc = ray.origin - center
#     a = dot(ray.direction, ray.direction)
#     b = 2.0 * dot(ray.direction, oc)
#     c = dot(oc, oc) - radius*radius
#     discriminant = b*b - 4*a*c
#     if discriminant < 0:
#         return -1.0
#     else:
#         return float((-b - math.sqrt(discriminant))/(2*a))


def color(r, world):
    hit_record = HitRecord()
    # MAXFLOAT in C++
    if world.hit(r, 0.0, sys.float_info.max, hit_record):
        return Vector3(hit_record.normal.x + 1.0, hit_record.normal.y + 1.0, hit_record.normal.z + 1.0)*0.5
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
    path = os.path.join(os.path.dirname(__file__), "..", "images", "three_spheres_normal.ppm")
    ppm_file = open(path, 'w')
    rows = 200
    columns = 100
    title = "P3\n{r} {c}\n255\n".format(r=rows, c=columns)
    lower_left_corner = Vector3(-2.0, -1.0, -1.0)
    horizontal = Vector3(4.0, 0.0, 0.0)
    vertical = Vector3(0.0, 2.0, 0.0)
    origin = Vector3(0.0, 0.0, 0.0)
    ppm_file.write(title)
    # Creating two sphere and making a world out of those hittable objects
    object_list = [Sphere(Vector3(0.0, 0.0, -1.0), 0.5), Sphere(Vector3(0.0, -100.5, -1.0), 100.0),
                   Sphere(Vector3(0.0, 102.5, -1.0), 100.0)]
    world = Hittable_List(object_list)
    for j in range(columns-1, -1, -1):
        for i in range(0, rows, 1):
            u = float(i)/float(rows)
            v = float(j)/float(columns)
            rayr = Ray(origin, lower_left_corner + horizontal*u + vertical*v)
            # Using the hittable classes and object. Why 2.0 ?
            p = rayr.point_at_parameter(2.0)
            col = color(rayr, world)
            ir = int(255.99*col.r)
            ig = int(255.99*col.g)
            ib = int(255.99*col.b)
            value = "{ir} {ig} {ib}\n".format(ir=ir, ig=ig, ib=ib)
            ppm_file.write(value)
    ppm_file.close()


if __name__ == '__main__':
    ray_camera_background()
