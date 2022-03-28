"""
This program allows you to obtain a new list with the
squares of an original list
"""


def run():
    list1 = [1,2,3,4,5]
    list2 = [i**2 for i in list1]
    print(list2)


if __name__ == "__main__":
    run()