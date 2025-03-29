#Ray McMillin, 3/28/25, Calculate Numbers Code
def sum_numbers_from_file():
    try:
        with open('numbers.txt', 'r') as file:
            total = 0
            for line in file:
                try:
                    number = int(line.strip()) 
                    total += number 
                except ValueError:
                    print(f"Warning: '{line.strip()}' is not a valid number and was skipped.")
        
        print(f"The sum of the numbers in numbers.txt is: {total}")

    except IOError:
        print("Error: The file 'numbers.txt' could not be opened or read.")

if __name__ == '__main__':
    sum_numbers_from_file()
