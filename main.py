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
        if char in chars:
            chars[char] += 1
        else: 
            chars[char] = 1
    return chars
    
    
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

main()