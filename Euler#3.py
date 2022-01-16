list_of_factors = [] #define a list of factors
def find_factors(number): #define a function to find factors
    factor = 2 #I started with the number 2 as a factor to check
    while number != 1: #at the end of the loop I will divide the number by its found factor and this loop stops when the number has been divided by every single factor and equals 1
        while number % factor != 0: #when the number is not a factor of the number inputted, I add 1 and keep checking
            factor = factor + 1
            if number % factor == 0: #If it is a factor I append it to the list of factors
                list_of_factors.append(factor)
                number = number/factor #I then divide the number by the factor to ultimately stop the loop
            if number == 1:
                print(list_of_factors) #prints the list of factors, but the factors may not be prime
    for factor in list_of_factors: #this for loop is to remove the non-prime factors from the list of factors
        x = factor
        for integer in range (1,number/2): #take a number from 1 to the original number divided by 2, which is the largest possible factor besides the number itself
            if x%integer == 0: #if the integer is a factor of x I remove it from the list
                list_of_factors.remove(x) 
            elif integer == x: #if the factor is only divisible by itself I add it back to the list
                list_of_factors.append(x)
    print(list_of_factors)
        

find_factors(600851475143) #I make a call to the function
