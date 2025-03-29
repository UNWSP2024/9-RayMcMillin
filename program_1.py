#Ray McMillin, 3/28/25, Names.TXT Code

def count_file_lines():
    try:
        with open('names.txt', 'r') as file:
            lines = file.readlines()

        num_names = len(lines)

        print(f"Number of names in the file: {num_names}")

    except FileNotFoundError:
        print("The file 'names.txt' was not found.")

if __name__ == '__main__':
    count_file_lines()
