"""
Alec Nahley
nahle003
CSCI 1133 Section 050
Assignment 1
"""


def main():
    make_change(int(input("Enter in the number of cents ")))


def make_change(cents):
    print(cents // 50, "half dollars")
    print(cents % 50 // 25, "quarters")
    print(cents % 50 % 25 // 10, "dimes")
    print(cents % 50 % 25 % 10 // 5, "nickles")
    print(cents % 50 % 25 % 10 % 5, "pennies")


if __name__ == "__main__":
    main()
