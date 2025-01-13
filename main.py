def open_book(path_to_file="./books/Frankenstein.txt"):
    with open(path_to_file) as f:
        contents = f.read()
        return contents
    
def count_words(book):
    return len(book.split())

def count_chars(book):
    book = book.lower()
    chars = {}
    for char in book:
        if char in chars and char.isalpha():
            chars[char] += 1
        elif char.isalpha(): 
            chars[char] = 1
    return chars
    
def sort_dict(dict):
    i=0
    listed = []
    for char in dict:
        listed.append({"char":char, "count":dict[char]})
    #listed.sort(reverse=True, key=listed["count"])
    print(f"\n\n\n{listed}")
    return None


def main():
    print("Provide book filepath. 'Enter' for Frankenstein")
    path = input()
    if path == '':
        book = open_book()
    else:
        book = open_book(path)

    print(f"There are {count_words(book)} words in the book")


    chars = count_chars(book)
    print("The character report:")
    print(f"The character \"{chars}")

    sort_dict(chars)

main()