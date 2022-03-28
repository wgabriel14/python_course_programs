"""
This program allows you to create a dictionary where 
the keys are the first 1000 natural numbers and
the values will be its square roots.
"""
import math


def run():
    dictionary = {numbers: math.sqrt(numbers) for numbers in range(1,1001)}
    print(dictionary)


if __name__ == "__main__":
    run()