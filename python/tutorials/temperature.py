def temperature():
    name = input("What is your name? ")
    print(f"Welcome to our Website {name}")
    
    temp = int (input("What is the temparature? "))
    
    if temp >= 30:
        print("Its a hot day")
    elif temp >= 15:
        print("Its a chilly day")
    else:
        print("Its a cold day, Keep warm")
    
temperature()


