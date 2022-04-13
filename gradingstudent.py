def gradingStudents(grades):
    for i in range(0,len(grades)):
        
        if grades[i] < 38:
            continue
        else:
            grade = grades[i]
            rem = grade % 5
            if rem == 3:
                grade = grade + 2
                grades[i] = grade
            elif rem == 4:
                grade = grade + 1
                grades[i] = grade
            else:
                continue
    return grades
