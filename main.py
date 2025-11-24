import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sort_dictionary_list
from stats import create_dictionary_list

def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #book = "books/frankenstein.txt"
    book = sys.argv[1]
    word_count = get_num_words(get_book_text(book))
    char_dict = get_num_chars(get_book_text(book))
    dictionary_list = sort_dictionary_list(create_dictionary_list(char_dict))
    #print(f"type of {type(dictionary_list)}")
    #print(f"in main: {dictionary_list}")

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    
    for item in dictionary_list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    
    print("============= END ===============")


main()
