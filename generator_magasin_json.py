# Generateur de donnees

import random
import datetime
import json
import io

def custom_gauss():
    output = int(random.gauss(4.5, 2))
    if output < 0 :
        output = output * (-1)
    if output > 9 :
        output = 9*2 - output
    
    return output
    
random_hour_morning = random.gauss(10,1)
random_hour_evening = random.gauss(15,1)
# product and price will be selected by gaussian, middle values are advantaged
original_products = [("brosse a dents", 5, 2), ("magazine", 3, 3), ("legumes", 2, 5), ("pain", 1, 8), ("sauce tomate", 2, 8), ("pates", 1, 10), ("riz", 1, 10), ("soda", 3, 15), ("papier toilette", 3, 3), ("coton tige", 2, 2)]
products = original_products
animals = ["rat", "ecureuil", "cheval", "dauphin", "chat", "chien", "baleine", "belette", "poisson", "ane"]
products_per_animal = {}

# Each animal have his preferences
for animal in animals:
    random.shuffle(products)
    
    # black magic to copy a list and not make it point to the same object
    products_per_animal[animal] = products[:]
    print("shuffkle")
    print(animal)
    print(products)

for animal in animals:
    print(animal)
    print(products_per_animal[animal])
    
    

with io.open("gene_output.txt", "w", encoding="utf-8") as output_file:
    for month in [7,8]:
        for day in range(1,32):
            iteration = random.randint(800,1500)
            for i in range(0,iteration):
                sell = {}

                if random.randint(0,1) == 0:
                    hour = int(random.gauss(10,1))
                else:
                    hour = int(random.gauss(15,1))
                minute = random.randint(0,59)
                seconde = random.randint(0,59)

                date = datetime.datetime(2021, month, day, hour, minute, seconde)

                # about the client
                animal_number = custom_gauss()
                animal = animals[animal_number]

                # About the product
                product_number = custom_gauss()   
                product = products_per_animal[animal][product_number][0]
                price = products_per_animal[animal][product_number][1]
                quantity = random.randint(0,products_per_animal[animal][product_number][2])


                sell["client"] = animal
                sell["time"] = date.isoformat()
                sell["total"] = price * quantity
                sell["product"] = product
                sell["price"] = price
                sell["quantity"] = quantity

                output_file.write(json.dumps(sell).decode("unicode_escape"))
                output_file.write(u"\n")
                #print(sell)

