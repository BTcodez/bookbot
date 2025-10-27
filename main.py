from stats import get_book_text
from stats import count_words
from stats import count_chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_count = count_chars(text)
    print(f"Found {num_words} total words")
    print(char_count)

    
main()
    



    
