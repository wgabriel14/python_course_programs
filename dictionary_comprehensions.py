"""
This program allows you to create a dictionary where 
the keys are the first 100 natural numbers and
the values the first 100 natural numbers but squared
"""


def run():
    dictionary = {numbers: numbers**2 for numbers in range(1,101)}
    print(dictionary)


if __name__ == "__main__":
    run()