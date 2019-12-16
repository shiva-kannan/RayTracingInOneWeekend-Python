# Ray Tracing in One Weekend in Python 

> Link Followed : https://raytracing.github.io/books/RayTracingInOneWeekend.html

## Step 1:
Setting up the Python 3 project and creating my first ppm output image
* I chose to use pipenv since that's becoming a standard and it's a much easier way to maintain dependencies 
* I also wanted to learn Python3 and get comfortable with it after 3 years of Python2 experience

So here is my first image!

![Hello World Image Output](images/python_hello_world_ppm_0.png)

## Step 2:
The second step was to setup a Vector utility class that will be used by pretty much all the code moving forward
Some decisions I had to make while write this class:
* I tried to have Vector3 as a subclass of numpy.ndarray but chose to write it from scratch because it was easier
* I used a decorator for some utility functions like cross,dot and unit_vector so that I can't pass around non-vectors

## Step 3:
This taught be what a Ray class would look like since Rays over here is an essential entity to navigate
from camera to objects
* This took me some time to get my code working because I realised I head to override the _add_ _sub_ properties of the
list Vector3 class to perform any sort of operations 
* I also learnt that after overriding the methods the operator order mattered. vector x 2 worked since I had defined the method 
that way but, 2 x vector doesn't work

But yes finally got to the lerp blue image! 

![Lerp Ray Camera Image](images/ray_camera_background.png)