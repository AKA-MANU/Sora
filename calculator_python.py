while True:
    
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))

    print("Enter the operation: ")
    print("1.ADD")
    print("2.SUB")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    print("5.EXIT")
    choose = input("Enter the choice (1-5): ")


    if choose =="5":
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
    
    else: 
        print("Please choose the right option")          

    
       
       
       
         

  
        
        
        
   

