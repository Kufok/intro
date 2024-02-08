import random


my_list = [1, "proc", 29, "Ahoj"]
random_element = random.choice(my_list) 
print("Ahoj reknes mi na jakem miste je jaka vec v listu")
print(my_list)
print(random_element)
input_user = int(input())
porovnani = my_list[input_user]
if porovnani == random_element:
    print("Ano je to spravne")
else:
    print("Ne je to spatne")