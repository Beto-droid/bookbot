from typing import TypedDict


def number_of_words(text_to_check:str) -> int:
    list_of_words = text_to_check.split()
    return len(list_of_words)

def number_of_occurring_characters(text_to_check:str) -> dict[str, int]:
    # list_of_words = text_to_check.split()
    recurring_characters:dict[str, int] = {}
    for word in text_to_check:
        if word.lower() in recurring_characters:
            recurring_characters[word.lower()] += 1
        else:
            recurring_characters[word.lower()] = 1
    return recurring_characters

class CharCount(TypedDict):
    char: str
    num: int

def sorted_dictionary(dict_to_sort:dict[str, int]) -> list[CharCount]:

    def sort_on(items):
        return items["num"]
    sorted_list_of_dictionary:list[CharCount] = []
    for key, value in dict_to_sort.items():
        sorted_list_of_dictionary.append({"char": str(key), "num":value})
    sorted_list_of_dictionary.sort(reverse=True, key=sort_on)
    return sorted_list_of_dictionary



