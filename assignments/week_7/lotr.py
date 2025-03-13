# To use this script open up the terminal and input "python lotr.py lotr.txt"

# Import sys library
import sys

# Function to read the file and count the number of "e"s
def count_e(FILENAME):
    with open(FILENAME, 'r') as f:
        text =  f.read()
    num_e = text.count('e')
    num_E = text.count('E')
    return num_e + num_E

# Read in command line argument
if __name__ == "__main__":
    FILENAME = sys.argv[1]
    count = count_e(FILENAME)

# Check the total number of "e"s in the file: 
    print(f"The number of time the letter e appears in {FILENAME} is {count}")

