#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Feb. 18, 2025
# This program calculates the area and perimeter of any rectangle.


# A function to create a formatted statement of the calculated area and perimeter.
def calc_area_perimeter(l, w):
    print("If a rectangle has the dimensions:")
    print(f"{l}cm x {w}cm \n")
    print(f"The area is: {l * w}cm^2")
    print(f"The perimeter is {2 * (l + w)}cm")


if __name__ == "__main__":
    # Call this function with an example 12cm x 30cm rectangle.
    calc_area_perimeter(12, 30)
