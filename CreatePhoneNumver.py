#Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
#Example
#create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
def create_phone_number(n):
    #your code here
    #slicing then convert ot string
    str1 = ''.join(str(e) for e in n[0:3]) 
    str2 = ''.join(str(e) for e in n[3:6])
    str3 = ''.join(str(e) for e in n[6:])
    x = '('+ str1 + ')'+ ' ' + str2 + '-' + str3
    return x

#best solution
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
