
def better_than_average(class_points, my_points):
    points = class_points + [my_points]
    
    average = sum(points) / len(points)
    
    return my_points > average