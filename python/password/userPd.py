user_password = input("Save password: ")
user_input = input("Enter Password: ")

while user_password != user_input:
    print("Incorrect password")
    break
else:
    print("Login successfull")
    
