a = 'hello'  #ASCII
cars =[]
for i in a:
    cars.append(ord(i))
print(cars)
s =''
#for i in cars:
    #s +=chr(i)
#print(s)
#for i in range(10000, 10020):
    #print(chr(i))
print(hex(ord('h')))
bb=b'\x68'
print(bb.decode())