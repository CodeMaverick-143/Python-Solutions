def Race(A, B, C):

    distance_naruto = abs(A - C)
    distance_sasuke = abs(B - C)
    

    if distance_naruto < distance_sasuke:
        return "N" 
    elif distance_sasuke < distance_naruto:
        return "S"  
    else:
        return "D"
