def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    count_dictionary = {}
    text_list = set(text.lower())
    for i in text_list:
        count_dictionary[i] = text.lower().count(i)
    return(count_dictionary)

# def sort_on(dict):
#     return dict[i]

def sorted_dict(character_dict):
    # character_dict.sort(reverse=True, key=character_dict[])
    return(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))