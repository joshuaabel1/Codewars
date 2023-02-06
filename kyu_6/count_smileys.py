
def count_smileys(arr):
    # recorremos arr para ver que no este vacio
    if len(arr) == 0:
        return 0
    # declaro un;a variable validate para confirmas caras validas
    eyes1 = ":"
    eyes2 = ";"
    mount1 = ")"
    mount2 = "D"
    count = []
    fix = 0
    for i in arr:
        if (eyes1 in i or eyes2 in i) and (mount1 in i or mount2 in i):
            print(i)
            count.append(i)
        if i == ';oD' or i == ":oD":
            fix += 1
                
    return len(count) - fix #the number of valid smiley faces in array/list