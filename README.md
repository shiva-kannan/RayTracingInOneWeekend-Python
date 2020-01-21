# Ray Tracing in One Weekend in Python 

> Link Followed : https://raytracing.github.io/books/RayTracingInOneWeekend.html


```NOTE : All the Steps are pushed under separate branches for someone to look at iterations. Master has the latest merged code```


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
* This took me some time to get my code working because I realised I had to override the _add_ _sub_ properties of the
list Vector3 class to perform any sort of operations 
* I also learnt that after overriding the methods the operator order mattered. vector x 2 worked since I had defined the method 
that way but, 2 x vector doesn't work

But yes finally got to the lerp blue image! 

![Lerp Ray Camera Image](images/ray_camera_background.png)

## Step 4:
After a bit of Vector algebra brush-up I learnt about how to represent a sphere in a vector form and then it was pretty straightforward 

* Check if the ray is hitting the sphere: This is done by solving the quadratic `dot(p(t) - C, p(t) - C) = R*R`
* All we had to check was to see if the discriminant was positive to confirm that there is a solution 
* Once this function is written we color the pixel red instead of the gradient and we get a beautiful centre sphere 

![FirstSphere](images/ray_camera_background_sphere.png)

## Step 5
The first part of this step is to generate a way to calculate and visualize the normals 
* We start by calculating the actual determinant -> use that to calculate the normal vector -> make it it's unit vector 
-> map the component values to R/G/B to visualize the normals on the sphere
* Also realised in Python3 the magic method for division should be `__truediv__` instead of just `__div__` 

![Sphere_Normal](images/ray_camera_background_sphere_normal.png)

* The next part of this step was to get an abstract class working to so that we can define what a `hittable` object needs
to implement. Mainly the "hit" function
* We then have a Hittable list class which allows us to define a list of "hittable" objects (in our example case -> two spheres)
* This list is then used to render out the normals for all the spheres in the scene. I went ahead and created two scenes -> one as 
explained in the tutorial and another with a sphere at +102.5 and that's how it looks. Fun! 

![Two Spheres](images/two_spheres_normal.png)     ![Three Spheres](images/three_spheres_normal.png)

## Step 6 
Anti Aliasing! 
I took a long break before this section and so I had to read back everything I had done before to carry on the momentum

* It was straightforward to make a Camera class and abstract what was going on in the main.py into it's own
* Anti Aliasing was about averaging out the color value by sending in multiple rays for the same pixel : Thankfully the random function in Python
was doing it's job of giving me [0, 1) real numbers so that was great! 
* I got stuck at this step for a while because the += operator wasn't working because of the vec3 `_add_` override. 
I had to expand it and it worked fine. I also learnt that I could override the `__iadd__` method to make it work but I kept it this way for now
* Also : Python is acting up already with just 3 spheres and samples = 100. It takes a solid 30s for this to render, but hey it did render! 

![Anti Aliasing](images/anti_aliasing.png)

## Step 7 
Diffuse material! 
This step was to mimic a diffuse material which basically has a color of its own and take on the color of the environment
Light can bounce off randomly at any direction after hitting the object

* Learnt the interesting and hacky Rejection method for calculating a random point inside a unit sphere
* The point of contact between two surfaces as we can see from the image is dark / shadow since it's mostly absorbed
* With a 100 samples : The image with gamma took 133.6 seconds to render (after removing the extra sphere in the scene)

![Diffuse without Gamma](images/diffuse_without_gamma.png)    ![Diffuse With Gamma](images/diffuse_with_gamma.png)

## Step 8 
Materials 
This step I learnt how to decouple material code into an a separate and class and define the scene with the material that
the sphere is coupled with

* Some vector math came to use here to define how a metal material would work
* Learnt the interesting approach to defining a fuzzy metal look that could use the same random unit sphere concept to get a more rough 
look of the same metal material
* The final frame took 269s to render after I put 4 spheres into the scene and applied different materials
* Added the depth parameter to restrict how deep we would want to the rays to keep bouncing


![3 Spheres with Material Class](images/material_class_3_spheres.png)    ![4 Spheres with metal](images/material_class_4_spheres.png)

## Step 9
Positionable camera

Learnt how we can define a movable camera in the scene and it's important parameters

* Writing the camera that was used till now (origin and looking at -z) in the positionable camera form gave me a good understanding of what the variables were
* Playing around with FOV I guessed it correct for what Peter Shirley had put as a closeup image! 

![Initial Camera Test](images/positionable_camera_first.png)    ![Camera position 1](images/positionable_camera_change_view_1.png)

![Much Lesser FOV](images/positionable_camera_change_view_2.png)

## Step 10

Defocus blur (Depth of field)

Simulating a thin lens for getting a defocus blur

* Used a similar random_unit_in_disc trick to augment the lens get_ray function

![Defocus Blur](images/defocus_blur.png)

## Final Renders! 
Even though it took 99 minutes for the last 1200x800 render it was worth it I think! 

Here are three renders with one in 1200x800 res


![First](images/last_scene.png)    ![Second](images/last_scene_2.png)

![ThirdHiRes](images/last_scene_3.png)

And the final render which took a ridiculous 21 hrs

![Final Render](images/last_scene_4.png)


``` NOTE : Haven't implemented Dielectric materials yet. For another day! ```