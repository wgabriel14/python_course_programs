def run ():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Williams", "lastname": "Reyes"}


    # Lista de diccionarios / Dict's list
    super_list = [
        {"firstname": "Williams", "lastname": "Reyes"},
        {"firstname": "Maria", "lastname": "Amaya"},
        {"firstname": "Daniel", "lastname": "Perez"},
        {"firstname": "Jesus", "lastname": "Manrique"},
        {"firstname": "Elizabeth", "lastname": "Ordonez"}
    ]


    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }


    for key, value in super_dict.items():
        print(key, "-", value)

# Entry point
if __name__ == "__main__": 
    run()