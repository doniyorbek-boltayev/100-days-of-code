def greeting():
    print("Hello")
    print("How are you feeling today?")
    print("Want to talk? Call 999 :)")

# Functions that allow for inputs
def greeting_v2(name, location):
    print(f"Hello {name}")
    print(f"How are you feeling today, {name}?")
    print(f"How is it the weather in {location}?")

greeting_v2("Doniyorbek", "Birmingham") # this is positional arguments
greeting_v2(location = "Tashkent", name = "Alibek") # this is keyword arguments

