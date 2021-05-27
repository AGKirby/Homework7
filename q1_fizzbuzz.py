def fizzbuzz():
    output = ""
    for i in range(1, 101): #numbers 1 to 100
        append = ""
        if(i % 3 == 0): #multiple of 3
            append += "Fizz"
        if(i % 5 ==0): #multiple of 5
            append += "Buzz"
        if(append == ""): 
            append += str(i)  
        output += append + '\n'
    return output
