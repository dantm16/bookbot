def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))        

def count_words(text):
    word_count = 0
    for word in text.split():
        word_count += 1
    return word_count



main()