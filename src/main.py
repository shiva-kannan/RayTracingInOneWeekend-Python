import os
from vector import *
from ray import Ray


@accepts(Ray)
def color(r):
    unit_direction = unit_vector(r.direction)
    # Graphics trick of scaling it to 0.0 < y < 1.0
    t = 0.5*(unit_direction.y + 1.0)
    # Lerping between (255, 255, 255) which is white to a light shade blue (128, 255*0.7, 255)
    return Vector3(1.0, 1.0, 1.0)*(1.0-t) + Vector3(0.0, 0.0, 1.0)*t


def ray_camera_background():
    path = os.path.join(os.path.dirname(__file__), "..", "images", "ray_camera_background_0.ppm")
    ppm_file = open(path, 'w')
    rows = 200
    columns = 100
    title = "P3\n{r} {c}\n255\n".format(r=rows, c=columns)
    lower_left_corner = Vector3(-2.0, -1.0, -1.0)
    horizontal = Vector3(4.0, 0.0, 0.0)
    vertical = Vector3(0.0, 2.0, 0.0)
    origin = Vector3(0.0, 0.0, 0.0)
    ppm_file.write(title)
    for j in range(columns-1, -1, -1):
        for i in range(0, rows, 1):
            u = float(i)/float(rows)
            v = float(j)/float(columns)
            rayr = Ray(origin, lower_left_corner + horizontal*u + vertical*v)
            col = color(rayr)
            ir = int(255.99*col.r)
            ig = int(255.99*col.g)
            ib = int(255.99*col.b)
            value = "{ir} {ig} {ib}\n".format(ir=ir, ig=ig, ib=ib)
            ppm_file.write(value)
    ppm_file.close()


if __name__ == '__main__':
    ray_camera_background()
