def leapyear(year: int):
    if(year % 4 == 0): #divisible by 4
        if(year % 100 != 0): #but not divisible by 100
            return True
    return False