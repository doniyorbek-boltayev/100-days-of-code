# random
import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)
print(f"Doniyorbek's favourite number is {my_module.my_favourite_number}")

random_number_0_to_1 = random.random() * 99 # multiplying by number which is 10 in this case shifts the output by the same number.
print(random_number_0_to_1)
print(f"{random_number_0_to_1:.0f}")

random_float = random.uniform(1, 10)
print(random_float)

# mini game. Heads or Tails
random_number = random.randint(0,1)
if random_number == 1:
    print("Heads")
else:
    print("Tails")

# list
my_list = [23, "hello", -34.5]
print(my_list[-0])

regions_of_Uzbekistan = ["Tashkent", "Andijan Region", "Bukhara Region", "Fergana Region", "Jizzakh Region", "Namangan Region", "Navoiy Region", "Qashqadaryo Region", "Samarqand Region", "Sirdaryo Region", "Surxondaryo Region", "Tashkent Region", "Xorazm Region", "Republic of Karakalpakstan"]
regions_of_Uzbekistan[1] = "Tashkent City"
print(regions_of_Uzbekistan, "\n")

regions_of_Uzbekistan.append("Doniyorbek Region")
print(regions_of_Uzbekistan,"\n")

regions_of_Uzbekistan.extend(["Diyorbek Region", "Davronbek Region"])
print(regions_of_Uzbekistan,"\n")

new_regions = ["Muhammadali Region", "Mirsaid Region"] # another way of working with .extend()
regions_of_Uzbekistan.extend(new_regions)
print(regions_of_Uzbekistan)

# "Who pays the bill" problem
frineds = ["Doniyorbek", "Behzod", "Alibek", "Jonibek", "Akbar"]

random_num = random.randint(0,4)
print(f"{frineds[random_num]} is paying the bill")

# alternative method using random.choice()
random_person = random.choice(frineds)
print(f"{random_person} is paying the bill")

# nested lists

friuts = ["Apple", "Banana", "Pealers", "Strawberry"]
veggies = ["Tomato", "Potato", "Cucumber"]

doniyor_eats = [friuts, veggies]
print(doniyor_eats[0][3])
