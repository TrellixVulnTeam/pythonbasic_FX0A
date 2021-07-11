def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "Mora"}

    super_list = [
        {"firstname": "Facundo", "lastname": "Mora"},
        {"firstname": "Isidro", "lastname": "Flores"},
        {"firstname": "Andres", "lastname": "Garcia"},
        {"firstname": "Alejandra", "lastname": "Smith"}

    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 2.5, 4.2, 6.5]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == "__main__":
    run()
