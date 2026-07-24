def total(m1,m2,m3,m4,m5):
    return  m1 + m2 + m3 + m4 + m5
def percentage(total):
    return (total/500) * 100
def grade(per):
    if per >= 90:
        return "A"
    elif per >= 80:
        return "B"
    elif per >= 70:
        return "C"
    elif per >= 60:
        return "D"
    else:
        return "F" 
    