import time
while True:
    
    print("Rules to be follow:")
    print("Each person get Two books from different caterogy:")
    time.sleep(3)
    books = int(input("How many books do you need?: "))
    print()
    grade = int(input("choose the book grade as your want(1-12)"))
    science = ["biology","chemistry","physics"]
    regular_sub = ["math", "social", "English"]
    computer = ["software_engineering","data_science","machine_learning"]

    choose = input("\nchoice between these Three types(Exit/science/regular_sub/computer): ")

    if choose == "exit":
        print("Come visit again")
        break
    if choose == "science": 
        print("\nHere are the available books type:",science)
    elif choose == "regular_sub":
        print("\nHere are the available books type:",regular_sub)
    elif choose == "computer":
        print("\nHere are the available books type:",computer)
    else:
        print("The books you are looking is not available")
