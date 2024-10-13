import os

def get_char_count(text):
    sylable = {}
    for char in text:
        if char.isalpha():
            sylable[char.lower()] = sylable.get(char.lower(), 0) + 1
    return sylable

def print_report(text):
    char_dict = get_char_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"The book has {len(text.split())} words.")
    print("")

    for char in sorted(char_dict, key=char_dict.get, reverse=True):
        print(f"The '{char}' character was found {char_dict[char]} times")
    print("--- End report ---")

def main():
    folder_path = "books/"

    files = os.listdir(folder_path)
    book_lst = []
    index = 0

    print("Available Books:")
    for file in files:
        book_lst.append(file)
        print(f"{index}. {file}")
        index += 1

    while True:
        try:
            user_input = int(input("Select one for report generation (enter a number): "))
            if 0 <= user_input < len(book_lst):
                break
            else:
                print(f"Please enter a number between 0 and {len(book_lst) - 1}.")
        except ValueError:
            print("Invalid input, please enter a valid number.")

    with open(f"books/{book_lst[user_input]}", "r") as book:
        content = book.read()

    print_report(content)

if __name__ == "__main__":
    main()
