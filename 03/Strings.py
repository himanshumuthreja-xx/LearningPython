sample_string = "It's a beautiful day"
print (sample_string)
reverse_sample_string = sample_string[::-1]
print(reverse_sample_string)
print(2+3) # Prints 5
print ('2'+'3') #prints 23 as string
# print ('2'+3) #Error. Can only concatenate str to str not int.

#Methods
x = 'Hello World'
print(x)
x = x.upper() # UPPER CASE THE STRING
print (x)
x = x.lower() # lower case the string
print (x)
x = x.split() # Splits the string into multiple objects. If no delimeter is mentioned, it splits with any whitespace.
print (x)
x = 'Hello World' # Since x was a list now.
x = x.split(',')
print(x)
x = 'Hello World' # Since x was a list now.
x = x.split('o')
print(x)


# Formatting

# .format() method
print('This is a string {}'.format('INSERTED'))
print('The {} {} {}'.format('fox','brown','quick'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

# Float formatting.
result = 100/777
print('Result was {}'.format(result))
print('Result was {r:1.4f}'.format(r=result))

# f string formattinh
result = 100/777
print(f'Result was {result}')
print(f'Result was {result:1.3f}')