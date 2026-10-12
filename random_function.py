import random 
import time
fruits = ["Apple", "Banana", "Grapes", "Avocado"]

fruit_choice = random.choice(fruits)
random_num = random.randint(1,10) 
print("Random Number:", random_num)
time.sleep(3)
print("Random fruits", fruit_choice)
