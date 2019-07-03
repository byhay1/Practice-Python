#----------------
#Dictionaries use a key:value pair in order to grab objects
#easier
#Unlike list you don't need to know where it is indexed but because of this it can not be sorted.
#----------------

#define your key value pairs
my_dict = {'key1':'value1','key2':'value2'}
prices_lookup = {'apple':.99,'orange':.59,'dragonfruit':2.39}
d1 = {'k1':100,'k2':200,'k3':300}


#if you want something from the dictionary use my_dict['key1']
print('',"To get 'value1' then use my_dict['key1'] : \n", my_dict['key1'], '\n')

#good for assigning interchangeable values
print('',"Find the price of an apple using prices_lookup['apple'] : \n", prices_lookup['apple'],'\n Again prices_lookup[dragonfruit] is: \n',prices_lookup['dragonfruit'])

#dictionaries are flexible
#assign key:int,key:list, and key:dictionary
d = {'k1':123,'k2':[0,1,2],'k3':{'insidekey':100}}
print(''," \n Lets mess around with this 'complexionary': \n",  d['k2'], '\n', d['k2'][1], '\n', d['k3'],'\n', d['k3']['insidekey'])

#add to dictionary by assigning a new key:value
#assign k4 with 400
d['k4'] = 400
#print new dictionary with k4:400
print('', "\n Add a new key:value in the dictionary like this: \n", "d['k4'] = 400; sooooooo: \n",d, '\n')

#get just the keys using the method .key()
print(d1.keys())

#get just the values using the method values()
print(d1.values())

#get the pairing (tuple) by using the method .items()
print(d1.items())