def likes(names):
    # your code here
    if len(names) == 0:
        return 'no one likes this'
    if len(names) ==1:
        return f"{names[0]} likes this"
    if len(names) ==2:
        return f"{names[0]} and {names[1]} like this"
    if len(names) ==3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    likes = []    
    for name in names:
        likes.append(name)

    count_list = [] 
    if len(likes) > 3:
        count_list = likes[2:len(likes)]
        names_like = likes[0], likes[1]
        return f"{names_like[0]}, {names_like[1]} and {len(count_list)} others like this"