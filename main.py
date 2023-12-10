def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    letters_dict = get_letter_count(text)
    sorted_letters_list = sort_dict_to_list(letters_dict)
    print(f"--- Begin report of {book_path} ---" )
    print(f"{num_words} words found in the document")
    print()
    
    for item in sorted_letters_list:
        if not item["letters"].isalpha():
            continue
        print(f"The '{item['letters']}' character was found {item['count']} times")
        
    print("--- End report ---")

def word_count(text):
    words = text.split()
    return len(words)

def sort_dict_to_list(letters):
    sort_lst = []
    for x in letters:
        sort_lst.append({"letters": x, "count": letters[x]})
    sort_lst.sort(reverse=True, key=sort_on)
    return sort_lst  
 
def get_letter_count(text):
    letters = {}
    for words in text.lower():
        for x in words:
            if x not in letters:
                letters[x] = 1
            else:
                letters[x] += 1
    return letters
       

          
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
           
main()