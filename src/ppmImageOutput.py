import os
from vector import Vector3

def hello_world_ppm():
    path = os.path.join(os.path.dirname(__file__), "..", "images", "python_hello_world_ppm_0.ppm")
    ppm_file = open(path, 'w')
    rows = 200
    columns = 100
    title = "P3\n{r} {c}\n255\n".format(r=rows, c=columns)
    ppm_file.write(title)
    for j in range(columns-1, -1, -1):
        for i in range(0, rows, 1):
            # r = float(i)/float(rows)
            # g = float(j)/float(columns)
            # b = 0.2   # A random blue value for an interesting blue blend to the image
            # Converting it into Vector3 type
            color = Vector3(float(i)/float(rows), float(j)/float(columns), 0.2)
            ir = int(255.99*color.r)
            ig = int(255.99*color.g)
            ib = int(255.99*color.b)
            value = "{ir} {ig} {ib}\n".format(ir=ir, ig=ig, ib=ib)
            ppm_file.write(value)
    ppm_file.close()

if __name__ == '__main__':
    hello_world_ppm()


