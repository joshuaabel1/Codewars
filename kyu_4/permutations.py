
import itertools

def permutations(s):
    lists = list(s)
    frases = list(itertools.permutations(s))

    resultado = set([''.join(frase) for frase in frases])            

    return resultado