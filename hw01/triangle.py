"""
Alec Nahley
nahle003
CSCI 1133 Section 050
Assignment 1
"""
import math


def main():
    sas(
        float(input("Enter shorter side (b): ")),
        float(input("Enter angle between sides in degrees (A): ")),
        float(input("Enter other side (c): "))
    )


def sas(side_b, angle_a, side_c):
    angle_a = math.radians(angle_a)
    side_a = (side_b**2 + side_c**2 - 2*side_b*side_c*math.cos(angle_a)) ** 0.5
    angle_b = math.degrees(math.asin((math.sin(angle_a)*side_b) / side_a))
    angle_c = 180 - angle_b - math.degrees(angle_a)
    print("Angle B is", angle_b)
    print("Side a is", side_a)
    print("Angle C is", angle_c)


if __name__ == "__main__":
    main()
