#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
#Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    # Bust a move right here
    arr = [ a for a in str(num)]
    arr.sort(reverse = True)
    return int(''.join(arr))
