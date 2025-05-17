#Rules and task for the whole weeks sunday to saturday
#User can get the information for the particular days 
#After this i will add the mark system to find if the task
#is complete or not
#Just a Demo talking for myself their are more to add
import time

print("Just a Demo")
time.sleep(2)
print("Rules and Task for the whole week")
time.sleep(2)
print("Recommended;")
time.sleep(1)
print("Start from the small task and habit")

def Sunday():
    print("\n[Wake up at 6AM],[Exercise at 6:30]")
    print("[Walking],[Coding],[Reading 3 pages of book]")
    print("[Soccer at Evening]")
    
def Monday():
    print("\nCleaning day,and same as Sunday->")
    return Sunday()
    
def Tuesday():
    print("same as sunday")
    return Sunday()
def Wednesday():
    print("\nsame as sunday")
    return Sunday()
    
def Thursday():
    print("\nsame as Sunday")
    return Sunday()
    
    
def Friday():
    print("\nCleaning day and complete all task ASAP")
    return Sunday()
    
def Saturday():
    print("\nRefreshment")
while True:
    
    print("Routine and Task:")
    print("1.Sunday")
    print("2.Monday")
    print("3.Tuesday")
    print("4.Wednesday")
    print("5.Thursday")
    print("6.Friday")
    print("7.Saturday")   
    choose = input("Choose the option(1-7)")

    if choose == "1":
        Sunday()
    if choose == "2":
        Monday()
    if choose == "3":
        Tuesday()
    if choose == "4":
        Wednesday()
    if choose == "5":
        Thursday()
    if choose == "6":
        Friday()
    if choose == "7":
        Saturday()
    if choose == "8":
        print("\nSee ya!")
        break
    
