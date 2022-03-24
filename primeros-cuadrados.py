"""
This program allows you to create a list of the first 100 
natural numbers squared
"""



def run():
    list = []
    for number in range (1,101):
        result = number*number
        list.append(result)     #Adding results to the list
    print(list)
    """
    Another way to do the same would be:

    list = [i**2 for i in range (1,101) if i % 3 != 0]
    print(list)
    """

if __name__ == "__main__":
    run()