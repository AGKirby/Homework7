def fizzbuzz():
    output = ""
    for i in range(1, 101): #numbers 1 to 100
        if(i % 3 == 0): #multiple of 3          step 2
            output += "Fizz"
        else: 
            output += str(i) 
        output += '\n'
    return output
