#Ray McMillin, 3/28/25, Random Number Code
import random

def generate_random_numbers():
    try:
        num_numbers = int(input("Enter how many random numbers you would like to generate (up to 1000): "))
        
        if num_numbers < 1 or num_numbers > 1000:
            print("The number must be between 1 and 1000.")
            return
        
        with open('random_numbers.txt', 'w') as file:
            for _ in range(num_numbers):
                random_number = random.randint(1, 500)
                file.write(f"{random_number}\n")

        print(f"Successfully wrote {num_numbers} random numbers to 'random_numbers.txt'.")

    except ValueError:
        print("Please enter a valid number.")

if __name__ == '__main__':
    generate_random_numbers()
