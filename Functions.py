# Copyright (c) 2021, Xin Tan
# All rights reserved

# Add index to each letter, e.g. TEST -> [ ['T',0], ['E',1], ['S',2], ['T',3] ]
def add_index_to_list(word_list):
    word_list_with_index = []
    i = 0
    while i < len(word_list):
        word_index_pair = [word_list[i], i]
        word_list_with_index.append(word_index_pair)
        i += 1
    return word_list_with_index


# Get a list of indexes for correct letter,
# e.g. word_list_with_index[ ['T',0], ['E',1], ['S',2], ['T',3] ]
# user_input: T
# return [0,3]
def get_index(user_input, word_list_with_index):
    index = []
    i = 0
    while i < len(word_list_with_index):
        if user_input == word_list_with_index[i][0]:
            index.append(word_list_with_index[i][1])
            word_list_with_index.remove(word_list_with_index[i])
            i -= 1

        i += 1
    return index



