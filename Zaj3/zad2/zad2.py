from geompy import *

print("=== Figury 2D ===")
print(f"Pole kwadratu o boku 4: {square_area(4)}")
print(f"Obwód kwadratu o boku 4: {square_perimeter(4)}")

print(f"Pole prostokąta 3x5: {rectangle_area(3, 5)}")
print(f"Obwód prostokąta 3x5: {rectangle_perimeter(3, 5)}")

print(f"Pole koła o promieniu 2: {circle_area(2):.2f}")
print(f"Obwód koła o promieniu 2: {circle_perimeter(2):.2f}")

print("\n=== Figury 3D ===")
print(f"Objętość sześcianu o krawędzi 3: {cube_volume(3)}")
print(f"Powierzchnia sześcianu o krawędzi 3: {cube_surface_area(3)}")

print(f"Objętość prostopadłościanu 2x4x6: {cuboid_volume(2, 4, 6)}")
print(f"Powierzchnia prostopadłościanu 2x4x6: {cuboid_surface_area(2, 4, 6)}")

print(f"Objętość kuli o promieniu 5: {sphere_volume(5):.2f}")
print(f"Powierzchnia kuli o promieniu 5: {sphere_surface_area(5):.2f}")
