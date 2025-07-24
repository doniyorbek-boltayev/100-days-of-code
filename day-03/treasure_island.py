print("Welcome to 'Do you know Doniyorbek well?' ")

year = int(input("What year did Sir Doniyorbek was born? "))
if year == 2006:
    print("Correct, continue")
    hobby = input("Which sport Doniyorbek enjoys the most. F for football and T for table tennis: ")
    if hobby == "T":
        print("Correct, continue")
        color = input("Which color is Doniyorbek's favourite. R for red, G for green, B for blue: ")
        if color == "G":
            print("CONGRATULTIONS, you know Doniyorbek very well!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
    
else:
    print("Game Over!")
