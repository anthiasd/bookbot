#This project was created for the boot.dev course, bookbot project.
#Completed 1/13/24

#Open file and return for parsing
def open_book(path_to_file="./books/Frankenstein.txt"): #default to the book being used for project to reduce rerun overhead
    with open(path_to_file) as f:
        contents = f.read()
        return contents, path_to_file #return both the book and path in case defaul path is used

#Split the book into a list of words, return count    
def count_words(book):
    return len(book.split())

#counts up each character occurance, alpha characters only. Returns this as a dictionary by letter.
def count_chars(book):
    book = book.lower()
    chars = {}
    for char in book:
        if char in chars and char.isalpha():
            chars[char] += 1
        elif char.isalpha(): 
            chars[char] = 1
    return chars

#Resorts the character count dictionary into a list of dicts, sorted using the number of occurances
def sort_dict(dict):
    i=0
    listed = []
    for char in dict:
        listed.append({"char":char, "count":dict[char]})
    #listed.sort(reverse=True, key=listed["count"])
    listed.sort(reverse=True,key=sort_key)
    #print(f"\n\n\n{listed}")
    return listed

#function as key for sorting the list of dicts
def sort_key(chars):
    return chars["count"]


def main():
    print("Provide book filepath. 'Enter' for Frankenstein")
    path = None
    path = input()
    if path == '': #get the default path in addition to book if one is not provided via input()
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