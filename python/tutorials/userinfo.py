def userInfo():
    print("WELCOME TO OMNIMARKET DISTRIBUTORS.")
    print("WE ARE A DISTRIBUTION COMPANY BASED IN KENYA, WE DEAL WITH BUILDING MATERIALS, CEREALS AND ELECTRONICS")
    
    name = input("Enter your name:  ")
    email = input("Enter your email:  ")
    password = int (input("Enter your password:  "))
    
    if password < 6:
        print("Your passwrord is too short! Must be 6 characters and above")
    else:
        print(f"Welcome {name}")
        
userInfo()
    
    
    