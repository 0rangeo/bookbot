def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    count_dictionary = {}
    text_list = set(text.lower())
    for i in text_list:
        count_dictionary[i] = text.lower().count(i)
    return(count_dictionary)