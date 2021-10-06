def grades(x):
    possible_grades = ['A', 'B', 'C', 'D', 'F']
    assert x in possible_grades
    return f"You have got {x}"
