def main():
    book_path = "books/frankenstein.txt"
    text = full_book(book_path)
    total_words = count_words(text)
    total_chars = count_characters(text)
    print(f"The total number of words in this book is {total_words}.")
    print("The total number of characters is broken down as follows:")
    for char in total_chars:
        print(f"{char}: {total_chars[char]}")

    
             

def count_words(text):
    return len(text.split())

def full_book(book_path):
    with open(book_path) as f:
        return f.read()    

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


main()