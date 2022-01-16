#Euler #5:
for number in range(1,100000000000): #check all the numbers from a range of 1 to 10000000000000
    x = number  #If the number is divisible by the first 20 natural numbers then I print it, and I find the smallest possible one
    if x%20 == 0:
        if x%19 ==0:
            if x%18 ==0:
                if x%17 ==0:
                    if x%16 ==0:
                        if x%15 ==0:
                            if x%14 ==0:
                                if x%13 ==0:
                                    if x%11 ==0:
                                        if x%7 ==0:
                                            if x%5 ==0:
                                                print(x)


                                                
#Euler #6:                                        
sum = 0 #define the first sum as 0
for number in range (0,101): #then for the number in the range of 0 to 100 I add the number to the initial sum
    sum = sum + number
sum = sum**2 #I then square that total sum and then I print it
print(sum)

sum2 = 0 #I then define a second sum
for number in range(0, 101): #I generate each number from the range of 0 to 100
    sum2 = sum2 + number**2 #I then square each number generated and then I add it to the second sum
print(sum2)
print(sum - sum2) #I subtract the second sum from the first in order to obtain the answer
