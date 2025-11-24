def get_num_words(book_text):
    num_words = len(book_text.split())
    return(f"Found {num_words} total words")


def get_num_chars(book_text):
    char_dict = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in char_dict:
            count = char_dict[char]
            char_dict[char] = count + 1
        else:

            char_dict[char] = 1
    return char_dict


def create_dictionary_list(dictionary):
    list_of_dict = []

    for key in dictionary:
        val = dictionary[key]
        d = {"char": key, "num": val}
        list_of_dict.append(d)
    #print(f"create_dictionary_list: {list_of_dict}")
    return list_of_dict

def sort_on(items):
    return items["num"]

def sort_dictionary_list(dictionary_list):
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
