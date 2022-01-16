best_palindrome = 0 #I first defined the best palindrome as equivalent to 0
for number in range(100,999):
    z = number #I then took two 3 digit numbers
    for number in range(100,999):
        x = number 
        product = x * z #I then multiplied them together
        reversed_num = str(product)[::-1] #I then found the number reversed 
        reversed_num = int(reversed_num) #Palindromes have the property in which they are equivalent reversed and forward
        product = int(product) #I then made the product an integer

        if product == reversed_num: #If the product is equivalent to the reversed number then it is a palindrome and I ultimately found the biggest one
            if product > best_palindrome:
                best_palindrome = product
                print(product)
            
