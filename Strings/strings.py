###This is a python file that will show how string variables are used.
sSomeString = 'This is a string'
sSomeOtherString = 'this is ALSO a string'

#manipulating strings
sCapitalString = ''

for letter in sSomeString:
    sCapitalString += letter.capitalize()        

#print the string
print('Regular string of letters: ' + sSomeString)

#print the other string
print('Other regular string of letters: ' + sSomeOtherString)

#print a capital string of letters
print('Capital String: ' + sCapitalString)

#concatenate two strings together
print('Combination of both strings: ' + (sCapitalString + sSomeOtherString + sSomeString))

