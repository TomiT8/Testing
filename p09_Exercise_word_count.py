def word_count(word):
    if len(word) == 0:
        return 0
    else:
        return word.count(" ") + 1


print(word_count(""))
