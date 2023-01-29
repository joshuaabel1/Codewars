
def how_much_i_love_you(nb_petals):
    lists = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return lists[(nb_petals - 1) % len(lists)]