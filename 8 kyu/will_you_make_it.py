def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! 
    c = fuel_left * mpg
    if c >= distance_to_pump:
        return True
    else:
        return False
    