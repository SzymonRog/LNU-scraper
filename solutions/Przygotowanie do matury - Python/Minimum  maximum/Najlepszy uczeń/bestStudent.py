def bestStudent( studentScores ):
    max_score = 0
    best_student =""
    for i in studentScores:
        if i[1] > max_score:
            max_score = i[1]
            best_student = i[0]
            
    return best_student