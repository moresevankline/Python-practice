"""Compute the volume of a sphere with a radius of 5. The formula for a sphere is 4⁄3πr3. Note: The answer is around 500, not 400 (in case you are using Python 2).
Write a function sphere_volume that returns the volume of a sphere when given radius r as a parameter. Then write a main program that calls sphere_volume to print the volume of a sphere with a radius of 5. Should the print statement go in the sphere_volume or the main program?"""
        
class Sphere():
    def sphere_volume(self, r):
        self.radius = r
        formula = ((4 * 3.14) * (r ** 3)) / 3
        return formula
        
n = Sphere()

print(int(n.sphere_volume(5)))   
print(int(n.sphere_volume(10)))                                       
       
        