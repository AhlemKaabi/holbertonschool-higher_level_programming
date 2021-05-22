#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary is {}:
        return None
    for key in a_dictionary:
        if a_dictionary[key] == max(a_dictionary.values()):
            return key
