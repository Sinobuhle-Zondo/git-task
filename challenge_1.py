#get input of 3 side of the triangle from the user to calculate the area
import math
calc_length = input("Enter the length of all 3 sides of the triangle: \n")

side1 = calc_length[0]
side2 = calc_length[1]
side3 = calc_length[2]

side1 = float(side1)
side2 = float(side2)
side3 = float(side3)

semi_par = (side1 + side2 + side3) / 2

print(f"The value of semi_parameter is: {semi_par}")

area = math.sqrt(semi_par * (semi_par - side1) * (semi_par -side2) * (semi_par - side3))

print(f"The area of the triangle is: {area}")
