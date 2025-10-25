def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents
    
#def main():
#   text = get_book_text()
#   return text

def count_words():
    text = get_book_text()
    #print(text)
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")
    
count_words()
    



    
