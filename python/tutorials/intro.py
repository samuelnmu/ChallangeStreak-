# name = "John Smith"
# age = 20
# is_new_patient = True

# print(f"Patient Name: {name}. Patients Age: {age}. Is patient newly admitted: {is_new_patient}")

# get name, fav color and output
# name = input("What is your name?")
# color = input("What is your favourite color?")
# print(f"{name} favourite color is {color}")


# collecting age
# name = input("What is your name? ")
# year = int(input("Which year were you born? "))
# age = 2024 - year

# print(f"{name}, You are {age} years old.")

# converting user pounds which is a float to kgs which is an int
# weight = float(input("How many Pounds do you weigh?"))
# kg = int(weight*0.45)
# print(f"You weigh {kg} kilograms")

# multiline string
# greeting = """
# How are you Sir,
# I hope you had an amaizing day.
# You are who you think you are!
# """
# print(greeting)


# methods in python
# name = "samuel loves GLC"
# print(name.upper())
# print(name.lower())
# print(name.find("a")) #finds the value you've passed
# print(name.replace("u", "e")) #replaces the passed value
# print("GLC" in name) #checks if the passed value is in the variable name

# if statement
# weather = int(input("What's the weather in degrees?"))

# if weather <= 10:
#     print("it's cold, keep warm!")
# elif weather <= 25:
#     print("Its warm, What a beautiful day")
# elif weather > 26:
#     print("Its very Hot")
# else:
#     print("It's very cold")
    


# calculating discount
# def calculate_discount(price, discount_percent):
#     """Calculates the final price after applying a discount.

#     Args:
#         price: The original price of the item.
#         discount_percent: The discount percentage.

#     Returns:
#         The final price after applying the discount, or the original price if the discount is less than 20%.
#     """

#     if discount_percent >= 20:
#         discount_amount = price * (discount_percent / 100)
#         final_price = price - discount_amount
#     else:
#         final_price = price

#     return final_price

# if __name__ == "__main__":
#     original_price = float(input("Enter the original price of the item: "))
#     discount_percentage = float(input("Enter the discount percentage: "))

#     final_price = calculate_discount(original_price, discount_percentage)

#     print("The final price after applying the discount is:", final_price)


# def item (price, discount):
#     price = print(input("Enter your Item price to get your discount: "))
    
    
#     if price >= 1000:
#         print("You will have  a discount of 20%")
#     elif price <= 999:
#         print("To get a discount you have to spend a min of 1000")
#     else:
#         print("Your item is not eligible for a discount")
        
#         discount = price * 20 / 100
        
#         final_price = discount
        
#         print(f"Your price after discount is {discount}")





        
