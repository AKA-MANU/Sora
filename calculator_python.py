while True:
    
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))

    print("\nEnter the operation: ")
    print("1.ADD")
    print("2.SUB")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    print("5.Discount")
    print("6.EXIT")
    choose = input("Enter the choice (1-6): ")


    if choose =="6":
        print("Exitting,Good_Bye")
        break

    elif choose =="1":
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
    elif choose == "2":
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
    elif choose == "3":
        print(f"{num_1} * {num_2} = {num_1 * num_2}")
    elif choose =="4":
        if num_2 ==0:
            print("Can't be divided by zero!")
                   
        else:
            print(f"{num_1} / {num_2} = {num_1 / num_2:.2f}")
            
    elif choose == "5":
        def calculate_discount (total,discount_percent):
            discount_amount = total * (discount_percent / 100)
            discounted_total = total - discount_amount
            return discounted_total
            
        total_cost = float(input("Enter the total_cost: "))
        discount = input("Do you have discount coupon?:,yes/no")
        
        if discount == "yes":
            discount_percent = float(input("Enter the discount_percent: "))
            final_cost = calculate_discount(total_cost,discount_percent)
            print("Your final cost after discount:", final_cost)
        else:
            ("Your final cost is :",final_cost)        

    else: 
        print("Please choose the right option")          
