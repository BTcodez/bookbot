def get_book_text(path):
    with open(path) as f:
        return f.read()
        

def count_words(text):
    #print(text)
    words = text.split()
    return len(words)
    
def count_chars(text):
    char_count = {}

    for char in text:
        low_char = char.lower()
        if low_char not in char_count:
            char_count[low_char] = 1
        else:
            char_count[low_char] += 1
    return char_count   
    