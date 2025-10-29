import sys

from stats import get_book_text
from stats import count_words
from stats import count_chars
from stats import sort_chars


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_count = count_chars(text)
    sorted_chars = sort_chars(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(" --------- Character Count -------")
    for i in sorted_chars:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
   
main()
    



    
