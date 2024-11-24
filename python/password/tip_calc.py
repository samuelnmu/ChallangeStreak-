def tip_calculator():
    
    try:
        bill = float(input("Enter the total bill: "))
        tip_percentage = int(input("How much tip would you like to tip in percentage?: "))
        split_people = int(input("How many people are spliting?: "))
        
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return
    
    if bill < 0 or tip_percentage < 0 or split_people <= 0:
        print("Please ensure all values are positive.")
        return
    
    total_tip = bill *(tip_percentage/100)
    total_bill = bill + total_tip
    
    amaunt_per_person = total_bill / split_people
    
    print(f"\nTotal bill including tip: ${total_bill: 2f}")
    print(f"\nTotal tip: ${total_tip: 2f}")
    print(f"Each person should pay ${amaunt_per_person}")
    
tip_calculator()

