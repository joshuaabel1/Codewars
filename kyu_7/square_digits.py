
def square_digits(num):
    array = str(num)
    num_parser = ''
    for i in array:
        num_string = int(i)**2
        num_parser += str(num_string)
    num_result = int(num_parser)
        
    return num_result