sum = 0 #Start off defining a variable for the total sum of all multiples of 5 or 3 under 1000
for number in range(1,1000): #Generate a range of numbers from 1 to 1,000 and check each one to find multiples of 3 or 5
    if number % 5 == 0: #multiples of 5 and add them to sum
        sum = sum + number
    elif number % 3 == 0: #multiples of 3 and add them to sum
        sum = sum + number

print(sum) #then print sum
