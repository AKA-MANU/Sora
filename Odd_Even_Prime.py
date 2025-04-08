def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def is_odd(number):
    return number % 2 != 0

def analyze_number(number):
    odd_or_even = "odd" if is_odd(number) else "even"
    prime_status = "prime" if is_prime(number) else "not prime"
    return (f"{number} is {odd_or_even} and {prime_status}")

def list_primes_up_to(number):
    return [i for i in range(2, number + 1) if is_prime(i)]

def list_odds_up_to(number):
    return [i for i in range(1, number + 1) if is_odd(i)]   
   

# 
try:
    number = int(input("Enter a number to analyze: "))
    print(analyze_number(number))
    
    # Optional: List primes up to the number
    choice = input("Would you like to see all prime numbers up to this number? (yes/no): ").lower()
    if choice == "yes":
        primes = list_primes_up_to(number)
        print(f"Prime numbers up to {number}: {primes}")
    elif choice == "no":
        odds = list_odds_up_to(number)
        print(f"Odd numbers up to {number}: {odds}")
except ValueError:
    print("Please enter a valid integer!")
    