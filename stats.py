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


def sort_chars(char_count):
    char_org = [{'char': key, 'num': value} for key, value in char_count.items() if key.isalpha()]
    def sort_nums(num):
        return num['num']
    char_org.sort(reverse=True, key=sort_nums)
    return char_org