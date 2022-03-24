"""
This program allows you to create a list using list comprehension.
Our list will have all multiplies of 4 that are also multiplies of 6
and 9, up to 5 digits.
"""


def run():
    multiplies = [element for element in range (1, 100000) 
    if element%4==0
    and element%6==0
    and element%9==0
    ]
    print(multiplies)


if __name__ == "__main__":
    run()