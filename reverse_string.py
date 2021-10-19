#Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

#Examples
#"This is an example!" ==> "sihT si na !elpmaxe"
#"double  spaces"      ==> "elbuod  secaps"

import re

def reverse_words(text):
    arr = re.split(' ', text)
    dic =[]
    for i in arr:
        dic.append(i[::-1])
        
    return ' '.join(dic)
