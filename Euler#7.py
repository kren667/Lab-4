import math
prime_list = [2] #list of primes
def isPrime(current_number, prime_list): #define a function to check if the current number is a prime
    for number in prime_list: #Check that every number in the prime list is able to divide the number 
        if current_number%number == 0:
            return False
    prime_list.append(current_number) #If no previous prime can divide the number, then it is a prime and it is added to the list
    return(current_number)


starting_val = 3 #starting value for the input
while len(prime_list) != 10002: #while the terms of the list do not exceed 10,000 terms, I loop through the function isPrime to check if the current number I am on is a prime and keep adding it to my list
    isPrime(starting_val, prime_list)
    starting_val = starting_val + 1

print(prime_list[10000]) #I print the 10,001st term of the prime list
