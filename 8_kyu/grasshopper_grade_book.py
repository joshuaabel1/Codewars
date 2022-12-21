def get_grade(s1, s2, s3):
    # Sumamos los valores
    
    score = (s1 + s2 + s3) / 3
    qualification= ["A", "B", "C", "D", "F"]
    if 90 <= score <= 100:
        return qualification[0]
    
    elif 80 <= score < 90:
        return qualification[1]
    
    elif 70 <= score < 80:
        return qualification[2]
        
    elif 60 <= score < 70:
        return qualification[3]

    return qualification[4]