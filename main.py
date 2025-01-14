def open_book(path_to_file="./books/Frankenstein.txt"):
    with open(path_to_file) as f:
        contents = f.read()
        return contents, path_to_file
    
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
    listed.sort(reverse=True,key=sort_key)
    #print(f"\n\n\n{listed}")
    return listed

def sort_key(chars):
    return chars["count"]


def main():
    print("Provide book filepath. 'Enter' for Frankenstein")
    path = None
    path = input()
    if path == '':
        book, path = open_book()
    else:
        book = open_book(path)

    print(f"=========================\nThis is the book report for {path.split("/")[-1:]}\n=========================")
    print(f"There are {count_words(book)} words in the book")


    chars = count_chars(book)
    char_report = sort_dict(chars)
    #print(char_report[0]["count"])
    for i in range(0, len(char_report)):
        print(f"The character '{char_report[i]["char"]}' has {char_report[i]["count"]} occurances.")
    print("==================\nEnd of book report\n==================")
    

main()