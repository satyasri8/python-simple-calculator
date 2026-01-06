"""
Task 3: Word Counter (Basic Version)

Description:
This program reads a text file and counts the number
of words present in the file. It also handles errors
such as file not found.
"""

# Ask user for file name
file_name = input("Enter the file name (with extension): ")

try:
    # Open the file in read mode
    with open(file_name, "r") as file:
        content = file.read()

        # Split content into words
        words = content.split()

        # Count number of words
        word_count = len(words)

        print(f"Total number of words: {word_count}")

except FileNotFoundError:
    print("Error: File not found. Please check the file name.")

except Exception as e:
    print("An unexpected error occurred:", e)
