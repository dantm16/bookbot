def main():
    book_path = "books/frankenstein.txt"
    text = full_book(book_path)
    total_words = count_words(text)
    print(f"The total number of words in this book is {total_words}")

    
             

def count_words(text):
    return len(text.split())

def full_book(book_path):
    with open(book_path) as f:
        return f.read()    



main()