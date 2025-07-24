# global scope
player_health = 100


def drink_potion():#
    print(player_health) # accessing global variable inside function
    # local scope
    player_strength = 15
    print(player_strength)


# print(player_strength) this line generates an error, since player_strength is local variable.
drink_potion()


# Concept of global & local scope applies to everything in programming language not just only variables.
# For example we can have function in global scope and local scope. see below;


user_name = 'Nemo'
def game():
    print('Welcome!', user_name)
    def lives():
        player_lives = 3
        print(f'You have {player_lives} lives')
    lives() # note, here local function is called within 'parent' function
game()


# there is Block Scope in Python!


age = 18
if age >= 18:
    permission_granted = True
print(permission_granted) # notice, here even though permission_granted was created inside if block, it does not show up an error.
# that i because, in python if new variable was to be created under blocks like if, while, for - it would be considered in global scope.
# however, this is not the case with functions.


game_level = 10
enemies = ['Me','Myself','Nemo']


def create_enemy():
    new_enemy = ''
    if game_level > 5:
        new_enemy = enemies[0]
   
    print(new_enemy)
create_enemy()

# exercise
def is_prime(num):
    is_divisible = False
    if num == 2:
        return True
    elif num == 1:
        return False
    elif num % 2 == 0:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            
        return True
print(is_prime(75))


# modifying global variables

name = "Doniyor"
def change_name():
    global name
    name = "Doniyorbek"
    return name
print(change_name()) # this method is discouraged, since it is prone to makeing errors later on.

# instead using this approach is more suitable

surname = "Boltae"
def change_surname(family_name):
    family_name = surname + 'v'
    return family_name
print(change_surname(surname)) # this method is encouraged, as it make your code less dependent on global variables.

# However, global feature in python is crutial while dealing with CONSTANTS
# global constants
PI = 3.14159
GOOGLE_URL = "https://www.google.com"

def show_pi():
    print(PI)
show_pi()
