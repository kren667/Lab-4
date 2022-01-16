start_number = 1 #These are the starting sequences of the Fibonacci sequence
second_number = 2
def calcevenFibvalues(start_number, second_number):
    sum_even_values = 2 #defined the sum of the even terms of the sequence
    value = start_number + second_number
    while value < 4000000: #While loop to ensure that the Fibonacci sequence does not exceed teh value of 4,000,000
        value = start_number + second_number #Newly generated term of the Fibonacci Sequence
        start_number = second_number #Second most recent term of the Fibonacci Sequence
        second_number = value #Most recent term of the Fibonacci sequence
        if value % 2 == 0: #If the term is deivisible by 2, then add it to the sum
            sum_even_values = sum_even_values + value
    return sum_even_values

print(calcevenFibvalues(1,2))
