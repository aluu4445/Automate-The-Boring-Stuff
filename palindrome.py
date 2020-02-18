x = 123

if x < 0:
    print(False)
    
if x == 0:
    print(True)
        
x_str = list(map(int, str(x)))
len_x = len(x_str)
print(x_str)
        
if x_str[len(x_str)-1] == 0:
    print(False)
        
y = x_str
z = x_str
       
for i in range(len_x):
        print(x_str)
        print(z)
        y[i] = z[len_x-i-1]
            
            
print(x_str)
print(y)
print(x_str == y)
