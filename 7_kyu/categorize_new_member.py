def open_or_senior(data):
    resp = []
    senior = "Senior"
    open = "Open"
    for i in data:
        if i[0] >= 55 and i[1] > 7: 
            resp.append(senior)
            
        else:
            resp.append(open)
            
    return resp 