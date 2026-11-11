def match_words(words):
    ctr = 0
    empty_list = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            empty_list.append(word)
    print("list of same charecter at first and last:", empty_list)
    return ctr
count = match_words(["abc", "cfc", "xyz", "aba", "1221"])
print("number of words having first and last charecter same:", count)