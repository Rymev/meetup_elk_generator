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
original_products = [("brosse a dents", 5, 4), ("magazine", 3, 3), ("legumes", 2, 5), ("pain", 1, 5), ("sauce tomate", 1, 3), ("pates", 1, 10), ("riz", 1, 8), ("soda", 2, 5), ("papier toilette", 3, 2), ("coton tige", 2, 1)]
products = original_products
animals = ["rat", "ecureuil", "cheval", "dauphin", "chat", "chien", "baleine", "belette", "poisson", "ane"]
products_per_animal = {}

# Each animal have his preferences
for animal in animals:
    random.shuffle(products)
    products_per_animal[animal] = products
    

for animal in animals:
    print(animal)
    print(products_per_animal[animal])
    
    

with io.open("gene_output.txt", "w", encoding="utf-8") as output_file:
    for month in [7,8]:
        for day in range(1,32):
            iteration = random.randint(300,800)
            for i in range(0,iteration):

                if random.randint(0,1) == 0:
                    hour = int(random.gauss(10,1))
                else:
                    hour = int(random.gauss(15,1))
                minute = random.randint(0,59)
                seconde = random.randint(0,59)

                date = datetime.datetime(2021, month, day, hour, minute, seconde)
                dt = date.strftime('%d/%b/%Y:%H:%M:%S')
                tz = "+0200"

                # about the client
                animal_number = custom_gauss()
                animal = animals[animal_number]


                # About the product
                product_number = custom_gauss()
                product = products_per_animal[animal][product_number][0]
                price = products[product_number][1]
                quantity = random.randint(1, products[product_number][2])

                if random.randint(0,100) < 5:
                    animal = "None"

                verb = "GET"
                rand_verb = random.randint(0,10)
                if rand_verb <= 2:
                    verb = "POST"

                url = "/{}".format(product)

                protocole = "HTTP/1.1"

                code_retour = "200"
                if animal == "None" and verb == "POST":
                    code_retour = "401"
                if random.randint(0,99) <= 4 :
                    code_retour = "500"

                output_file.write(u"[{} {}] - [{}] - {} {} {} {}".format(dt, tz, animal, verb, url, protocole, code_retour))
                output_file.write(u"\n")
                

