# todo:
#   ideálny stav, ak je vždy za slovom medzera
# def word_count(word):
#     if len(word) == 0:
#         return 0
#     else:
#         return word.count(" ") + 1
#
#
# print(word_count(""))

# todo:
#    regex

# import re
#
#
# def word_count(word):
#     word = word.strip()
#     if len(word) == 0:
#         return 0
#     words = re.findall(r'\b\w+\b', word)
#
#     return len(words)


# todo:
#   tretie riešenie

def word_count(s):
    return len(s.split())
