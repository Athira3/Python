import graphics.circle
from graphics import rectangle as rec
from graphics.ThreeDimensionalGraphics.cuboid import *
from graphics.ThreeDimensionalGraphics import sphere

rect_len = float(input('Enter length of the rectangle:'))
rect_bre = float(input('Enter breadth of the rectangle:'))
rect_area = rec.rectangle_area(rect_len, rect_bre)
print('Area of rectangle=', rect_area)
rect_perimeter = rec.rectangle_perimeter(rect_len, rect_bre)
print('perimeter of rectangle=', rect_perimeter)
cir_rad = float(input('Enter radius of the circle:'))
cir_area = graphics.circle.circle_area(cir_rad)
print('Area of circle=', cir_area)
cir_perimeter = graphics.circle.circle_perimeter(cir_rad)
print('perimeter of circle=', cir_perimeter)
cub_len = float(input('Enter length of the cuboid:'))
cub_bre = float(input('Enter breadth of the cuboid:'))
cub_hie = float(input('Enter height of the cuboid:'))
cub_area = cuboid_area(cub_len, cub_bre, cub_hie)
print('Area of cuboid=', cub_area)
cub_perimeter = cuboid_perimeter(cub_len, cub_bre, cub_hie)
print('perimeter of cuboid=', cub_perimeter)
sph_rad = float(input('Enter radius of the sphere:'))
sph_area = sphere.sphere_area(sph_rad)
print('Area of sphere=', sph_area)
sph_perimeter = sphere.sphere_perimeter(sph_rad)
print('perimeter of sphere=', sph_perimeter)
