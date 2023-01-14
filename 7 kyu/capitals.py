def capitals(word):
    indexs = []
    for i in range(len(word)):
        if word[i].isupper():
            indexs.append(i)
    return indexs