
def enough(cap, on, wait):
    # Your code here
    current_people = (cap - on)
    if current_people > wait:
        return 0
    return wait - current_people