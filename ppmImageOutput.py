import os

def hello_world_ppm():
    path = "/Users/shiva/Desktop/python_hello_world_ppm_0.ppm"
    ppm_file = open(path, 'w')
    rows = 200
    columns = 100
    title = "P3\n{r} {c}\n255\n".format(r=rows, c=columns)
    ppm_file.write(title)
    for j in range(columns-1, -1, -1):
        for i in range(0, rows, 1):
            r = float(i)/float(rows)
            g = float(j)/float(columns)
            b = 0.2   # A random blue value for an interesting blue blend to the image
            ir = int(255.99*r)
            ig = int(255.99*g)
            ib = int(255.99*b)
            value = "{ir} {ig} {ib}\n".format(ir=ir, ig=ig, ib=ib)
            ppm_file.write(value)
    ppm_file.close()

if __name__ == '__main__':
    hello_world_ppm()


