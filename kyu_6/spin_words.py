
def spin_words(sentence):
    # Your code goes here
    if len(sentence) < 5:
        return sentence

    lists = sentence.split(' ')
    separador =" "
    count = 0
    for i in range(0, len(lists)):
        count += 1
        if len(lists[i]) >= 5:
            lists[i] = lists[i][::-1]
                
    return [separador.join(lists)][0]