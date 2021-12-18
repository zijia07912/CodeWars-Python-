#Given: an array containing hashes of names
#Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
#Example:
#namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

def namelist(names):
    #your code here
    if len(names) == 0:
        return ''
    if len(names) == 1:
        temp = names[0]
        v = list(temp.values())
        return str(''.join(v))
    else:
        temp = names.pop()
        templist  = []
        for val in names:
            v = list(val.values())
            templist.append(str(''.join(v)))
        v = list(temp.values())
        return ', '.join(templist)+" & "+ str(''.join(v))
      
#best solution 
def namelist(names):
    if len(names) > 1:
          return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''
