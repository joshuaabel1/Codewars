
def get_count(sentence):
    vocals = "aeiou"
    count = 0
    for i in vocals:
        count += sentence.count(i)
    return count   