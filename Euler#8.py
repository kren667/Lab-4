number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
number = str(number) #Take the string of the number above
greatest_cons_13 = 0 #defined the greatest product of consecutive 13 digits as 0 initially
product_of_13 = 1 #the product of the 13 current digits is initially 1
int(product_of_13)
while len(number) != 12: #this is to stop the while loop once there is less than 13 digits within the number left
    r = [] #I have a list of the 13 consecutive digits here and I refresh it every time I loop through the while loop
    first = number[0:1] #I append the first through 13th digits of the number above to the list r
    r.append(first)
    second = number[1:2]
    r.append(second)
    third = number[2:3]
    r.append(third)
    fourth = number[3:4]
    r.append(fourth)
    fifth = number[4:5]
    r.append(fifth)
    sixth = number[5:6]
    r.append(sixth)
    seventh = number[6:7]
    r.append(seventh)
    eighth = number[7:8]
    r.append(eighth)
    ninth = number[8:9]
    r.append(ninth)
    tenth = number[9:10]
    r.append(tenth)
    eleventh = number[10:11]
    r.append(eleventh)
    twelfth = number[11:12]
    r.append(twelfth)
    thirteenth = number[12:13]
    r.append(thirteenth)
    print(r)
    for element in r: #I then created a for loop which loops through every number in the list created above and I multiply is with the product of the 13 consecutive digits
        element = int(element) 
        product_of_13 = product_of_13 * element
    if product_of_13 > greatest_cons_13: #If the product of the 13 consecutive digits is greater than the product of the greatest consecutive 13 digits, then it replaces it
        greatest_cons_13 = product_of_13
    number = number[1:] #I remove the first index of the number and analyze the consecutive 13 digits in this reading frame
    
print(greatest_cons_13) #I then print hte greatest 13 consecutive digits 
