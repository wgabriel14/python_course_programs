"""
This program allows you to create a list of the first 100 
natural numbers squared
"""



def run():
    list = []
    for number in range (1,101):
        result = number*number
        list.append(result)
    print(list)

if __name__ == "__main__":
    run()