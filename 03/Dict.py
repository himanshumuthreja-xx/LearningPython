my_dict = {'key1':'value1',"key2":"value2"}
print(my_dict)
print(my_dict['key1'])
product_prices = {'apple':'100','oranges':40}
print(product_prices['oranges'])
print(type(product_prices['oranges']))
d = {'k1':'str','list':[0,1,2],'dict':{'k1':'v1','k2':3}}
print(d['dict'])
print(d['dict']['k1'])
d['dict']['k3'] = 'v3' # Adds a new key
d['newKey'] = 'newValue' # Adds a new key
print(d['dict']['k3'])
print(d['newKey'])