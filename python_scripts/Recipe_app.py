# Ingredients
Eggs = "Eggs"
Milk = "Milk"
Flour = "Flour"
Butter = "Butter"
Vanilin = "Vanilin"
Sugar = "Sugar"
Baking_soda = "Baking soda"
Vinegar = "Vinegar"
Jam = "Jam (any)"

# Quantity
Eggs_q = float(3)
Eggs_q_new = float()
Milk_q = float(20)
Milk_q_new = float()
Flour_q = float(520)
Flour_q_new = float()
Butter_q = float(200)
Butter_q_new = float()
Vanilin_q = float(2)
Vanilin_q_new = float()
Sugar_q = float(200)
Sugar_q_new = float()
Baking_soda_q = float(5)
Baking_soda_q_new = float()
Vinegar_q = float(5)
Vinegar_q_new = float()
Jam_q = float(200)
Jam_q_new = float()

# Omelette recipe
ing_omelette = [Eggs, Milk]
omelette_q = [Eggs_q, Milk_q]

# Cake recipe
ing_cake = [Flour, Butter, Vanilin, Eggs, Sugar, Baking_soda, Vinegar, Jam]
cake_q = [Flour_q, Butter_q, Vanilin_q, Eggs_q, Sugar_q, Baking_soda_q, Vinegar_q, Jam_q]

# Calculation values
residue = float()
insufficient = ""
insufficient_q = float()

dish = input("What do you want to cook?\nOmelette (1)\nCake (2): ")



# Omelette recipe
if dish == "Omelette" or dish == "omelette" or dish == "1":
    print("***************\nOmelette recipe:\n*************** ")
    for one,two in zip(ing_omelette,omelette_q):
        print (one,two)
    insufficient = input("Please specify which ingredient you have insufficient: ")
    insufficient_q = float(input("Enter how much you have now: "))
### eggs option in omelette
    if insufficient == Eggs or insufficient == "eggs" or insufficient == "e" or insufficient == "E":
            def change_recipe_omelette(Eggs, Eggs_q, Milk, Milk_q_new):
                residue = Eggs_q / insufficient_q
                Milk_q_new = Milk_q / residue
                return Eggs, round(insufficient_q), Milk, round(Milk_q_new)
            print("********************\nNew omelette recipe:\n******************** ")
            print(change_recipe_omelette(Eggs , Eggs_q , Milk , Milk_q_new))
### milk option im omelette
    elif insufficient == Milk or insufficient == "milk" or insufficient == "m" or insufficient == "M":
            def change_recipe_omelette(Eggs, Eggs_q, Milk, Milk_q_new):
                residue = Milk_q / insufficient_q
                Eggs_q_new = Eggs_q / residue
                return Eggs, round(Eggs_q_new), Milk, round(insufficient_q)
            print("********************\nNew omelette recipe:\n******************** ")
            print(change_recipe_omelette(Eggs, Eggs_q, Milk, Milk_q_new))



# Cake recipe
elif dish == "Cake" or dish == "cake" or dish == "2":
    print("*************\nCake recipe:\n************* ")
    for one,two in zip(ing_cake,cake_q):
        print (one,two)
    insufficient = input("Please specify which ingredient you have insufficient: ")
    insufficient_q = float(input("Enter how much you have now: "))
### Flour option in cake
    if insufficient == Flour or insufficient == "flour" or insufficient == "f" or insufficient == "F":
        def change_recipe_cake(Flour, Flour_q, Butter, Butter_q_new, Vanilin, Vanilin_q_new, Eggs, Eggs_q_new, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q_new, Jam, Jam_q_new):
            residue = Flour_q / insufficient_q
            Butter_q_new = Butter_q / residue
            Vanilin_q_new = Vanilin_q / residue
            Eggs_q_new = Eggs_q / residue
            Sugar_q_new = Sugar_q / residue
            Baking_soda_q_new = Baking_soda_q / residue
            Vinegar_q_new = Vinegar_q / residue
            Jam_q_new = Jam_q / residue
            return Flour, round(insufficient_q), Butter, round(Butter_q_new), Vanilin, round(Vanilin_q_new), Eggs, round(Eggs_q_new), Sugar, round(Sugar_q_new), Baking_soda, round(Baking_soda_q_new), Vinegar, round(Vinegar_q_new), Jam, round(Jam_q_new)
        print("****************\nNew cake recipe:\n**************** ")
        print(change_recipe_cake(Flour, Flour_q, Butter, Butter_q_new, Vanilin, Vanilin_q_new, Eggs, Eggs_q_new, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q_new, Jam, Jam_q_new))
### Butter option in cake
    if insufficient == Butter or insufficient == "butter" or insufficient == "b" or insufficient == "B":
        def change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q, Vanilin, Vanilin_q_new, Eggs, Eggs_q_new, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q_new, Jam, Jam_q_new):
            residue = Butter_q / insufficient_q
            Flour_q_new = Flour_q / residue
            Vanilin_q_new = Vanilin_q / residue
            Eggs_q_new = Eggs_q / residue
            Sugar_q_new = Sugar_q / residue
            Baking_soda_q_new = Baking_soda_q / residue
            Vinegar_q_new = Vinegar_q / residue
            Jam_q_new = Jam_q / residue
            return Flour, round(Flour_q_new), Butter, round(insufficient_q), Vanilin, round(Vanilin_q_new), Eggs, round(Eggs_q_new), Sugar, round(Sugar_q_new), Baking_soda, round(Baking_soda_q_new), Vinegar, round(Vinegar_q_new), Jam, round(Jam_q_new)
        print("****************\nNew cake recipe:\n**************** ")
        print(change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q, Vanilin, Vanilin_q_new, Eggs, Eggs_q_new, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q_new, Jam, Jam_q_new))
### Vanilin option in cake
    if insufficient == Vanilin or insufficient == "vanilin" or insufficient == "v" or insufficient == "V":
        def change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q_new, Vanilin, Vanilin_q, Eggs, Eggs_q_new, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q_new, Jam, Jam_q_new):
            residue = Vanilin_q / insufficient_q
            Flour_q_new = Flour_q / residue
            Butter_q_new = Butter_q / residue
            Eggs_q_new = Eggs_q / residue
            Sugar_q_new = Sugar_q / residue
            Baking_soda_q_new = Baking_soda_q / residue
            Vinegar_q_new = Vinegar_q / residue
            Jam_q_new = Jam_q / residue
            return Flour, round(Flour_q_new), Butter, round(Butter_q_new), Vanilin, round(insufficient_q), Eggs, round(Eggs_q_new), Sugar, round(Sugar_q_new), Baking_soda, round(Baking_soda_q_new), Vinegar, round(Vinegar_q_new), Jam, round(Jam_q_new)
        print("****************\nNew cake recipe:\n**************** ")
        print(change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q_new, Vanilin, Vanilin_q, Eggs, Eggs_q_new, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q_new, Jam, Jam_q_new))
### Eggs option in cake
    if insufficient == Eggs or insufficient == "eggs" or insufficient == "e" or insufficient == "E":
        def change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q_new, Vanilin, Vanilin_q_new, Eggs, Eggs_q, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q_new, Jam, Jam_q_new):
            residue = Eggs_q / insufficient_q
            Flour_q_new = Flour_q / residue
            Butter_q_new = Butter_q / residue
            Vanilin_q_new = Vanilin_q / residue
            Sugar_q_new = Sugar_q / residue
            Baking_soda_q_new = Baking_soda_q / residue
            Vinegar_q_new = Vinegar_q / residue
            Jam_q_new = Jam_q / residue
            return Flour, round(Flour_q_new), Butter, round(Butter_q_new), Vanilin, round(Vanilin_q_new), Eggs, round(insufficient_q), Sugar, round(Sugar_q_new), Baking_soda, round(Baking_soda_q_new), Vinegar, round(Vinegar_q_new), Jam, round(Jam_q_new)
        print("****************\nNew cake recipe:\n**************** ")
        print(change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q_new, Vanilin, Vanilin_q_new, Eggs, Eggs_q, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q_new, Jam, Jam_q_new))
### Sugar option in cake
    if insufficient == Sugar or insufficient == "sugar" or insufficient == "s" or insufficient == "S":
        def change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q_new, Vanilin, Vanilin_q_new, Eggs, Eggs_q_new, Sugar, Sugar_q, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q_new, Jam, Jam_q_new):
            residue = Sugar_q / insufficient_q
            Flour_q_new = Flour_q / residue
            Butter_q_new = Butter_q / residue
            Vanilin_q_new = Vanilin_q / residue
            Eggs_q_new = Eggs_q / residue
            Baking_soda_q_new = Baking_soda_q / residue
            Vinegar_q_new = Vinegar_q / residue
            Jam_q_new = Jam_q / residue
            return Flour, round(Flour_q_new), Butter, round(Butter_q_new), Vanilin, round(Vanilin_q_new), Eggs, round(Eggs_q_new), Sugar, round(insufficient_q), Baking_soda, round(Baking_soda_q_new), Vinegar, round(Vinegar_q_new), Jam, round(Jam_q_new)
        print("****************\nNew cake recipe:\n**************** ")
        print(change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q_new, Vanilin, Vanilin_q_new, Eggs, Eggs_q_new, Sugar, Sugar_q, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q_new, Jam, Jam_q_new))
### Baking soda option in cake
    if insufficient == Baking_soda or insufficient == "baking soda" or insufficient == "ba" or insufficient == "bs" or insufficient == "BA" or insufficient == "BS":
        def change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q_new, Vanilin, Vanilin_q_new, Eggs, Eggs_q_new, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q, Vinegar, Vinegar_q_new, Jam, Jam_q_new):
            residue = Baking_soda_q / insufficient_q
            Flour_q_new = Flour_q / residue
            Butter_q_new = Butter_q / residue
            Vanilin_q_new = Vanilin_q / residue
            Eggs_q_new = Eggs_q / residue
            Sugar_q_new = Sugar_q / residue
            Vinegar_q_new = Vinegar_q / residue
            Jam_q_new = Jam_q / residue
            return Flour, round(Flour_q_new), Butter, round(Butter_q_new), Vanilin, round(Vanilin_q_new), Eggs, round(Eggs_q_new), Sugar, round(Sugar_q_new), Baking_soda, round(insufficient_q), Vinegar, round(Vinegar_q_new), Jam, round(Jam_q_new)
        print("****************\nNew cake recipe:\n**************** ")
        print(change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q_new, Vanilin, Vanilin_q_new, Eggs, Eggs_q_new, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q, Vinegar, Vinegar_q_new, Jam, Jam_q_new))
### Vinegar option in cake
    if insufficient == Vinegar or insufficient == "vinegar" or insufficient == "vi" or insufficient == "VI":
        def change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q_new, Vanilin, Vanilin_q_new, Eggs, Eggs_q_new, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q, Jam, Jam_q_new):
            residue = Vinegar_q / insufficient_q
            Flour_q_new = Flour_q / residue
            Butter_q_new = Butter_q / residue
            Vanilin_q_new = Vanilin_q / residue
            Eggs_q_new = Eggs_q / residue
            Sugar_q_new = Sugar_q / residue
            Baking_soda_q_new = Baking_soda_q / residue
            Jam_q_new = Jam_q / residue
            return Flour, round(Flour_q_new), Butter, round(Butter_q_new), Vanilin, round(Vanilin_q_new), Eggs, round(Eggs_q_new), Sugar, round(Sugar_q_new), Baking_soda, round(Baking_soda_q_new), Vinegar, round(insufficient_q), Jam, round(Jam_q_new)
        print("****************\nNew cake recipe:\n**************** ")
        print(change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q_new, Vanilin, Vanilin_q_new, Eggs, Eggs_q_new, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q, Jam, Jam_q_new))
### Jam option in cake
    if insufficient == Jam or insufficient == "jam" or insufficient == "j" or insufficient == "J":
        def change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q_new, Vanilin, Vanilin_q_new, Eggs, Eggs_q_new, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q_new, Jam, Jam_q):
            residue = Jam_q / insufficient_q
            Flour_q_new = Flour_q / residue
            Butter_q_new = Butter_q / residue
            Vanilin_q_new = Vanilin_q / residue
            Eggs_q_new = Eggs_q / residue
            Sugar_q_new = Sugar_q / residue
            Baking_soda_q_new = Baking_soda_q / residue
            Vinegar_q_new = Vinegar_q / residue
            return Flour, round(Flour_q_new), Butter, round(Butter_q_new), Vanilin, round(Vanilin_q_new), Eggs, round(Eggs_q_new), Sugar, round(Sugar_q_new), Baking_soda, round(Baking_soda_q_new), Vinegar, round(Vinegar_q_new), Jam, round(insufficient_q)
        print("****************\nNew cake recipe:\n**************** ")
        print(change_recipe_cake(Flour, Flour_q_new, Butter, Butter_q_new, Vanilin, Vanilin_q_new, Eggs, Eggs_q_new, Sugar, Sugar_q_new, Baking_soda, Baking_soda_q_new, Vinegar, Vinegar_q_new, Jam, Jam_q))
else:
        print("An error occurred. Please select an available value")

input("\n\nPress Enter to exit: ")








