# todo
#   ideálny stav, ak je vždy za slovom biely znak
# def word_count(word):
#     if len(word) == 0:
#         return 0
#     else:
#         return word.count(" ") + 1
#
#
# print(word_count(""))

import re


def word_count(word):
    word = word.strip()
    if len(word) == 0:
        return 0
    words = re.findall(r'\b\w+\b', word)

    return len(words)
