def leapyear(year: int):
    if(year % 4 == 0): #divisible by 4
        if(year % 100 != 0): #but not divisible by 100
            return True
        elif(year % 400 == 0): #unless divisible by 400
            return True
    return False