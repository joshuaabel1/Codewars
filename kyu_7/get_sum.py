
def get_sum(a, b):
  # averiguamos cual es el numero mas alto entre las arg
    if a < b:
        smaller = a
        larger = b
    else:
        smaller = b
        larger = a
   # declaramos sum = 0  
    sum = 0
  # declaramos un range entre el mas chico al mas grande
    for i in range(smaller, larger+1):
        sum += i
    
    return sum