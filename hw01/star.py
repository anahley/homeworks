"""
Alec Nahley
nahle003
CSCI 1133 Section 050
Assignment 1
"""
import turtle

SIDE_LENGTH = 100
TURN_ANGLE = 144  # using left turns


def main():
    make_star(SIDE_LENGTH, TURN_ANGLE)


def make_star(length, theta):
    turtle.showturtle()
    turtle.left(180 + theta)  # starting angle
    for i in range(5):
        turtle.forward(length)
        turtle.left(theta)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
