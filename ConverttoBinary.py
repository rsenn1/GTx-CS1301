number = 215

if number >= 128: 
    first = 1 
    number -=128
else:
   first = 0

string = "{0}" .format(first)
if number >= 64:
    second = 1
    number -=64
else:  
    second = 0

string = "{0}{1}" .format(first,second)
if number >= 32:
    third = 1
    number -=32
else:
    third = 0

string = "{0}{1}{2}" .format(first,second,third)
if number >= 16:
    fourth = 1
    number -= 16
else:
    fourth = 0

string = "{0}{1}{2}{3}" .format(first,second,third,fourth)   
if number >= 8:
    fifth = 1
    number -= 8
else:
    fifth = 0

string = "{0}{1}{2}{3}{4}" .format(first,second,third,fourth,fifth)
if number >= 4:
    sixth = 1
    number -=4
else:
    sixth = 0
string = "{0}{1}{2}{3}{4}{5}" .format(first,second,third,fourth,fifth,sixth)    
if number >= 2:
    seventh = 1
    number -=2
else:
    seventh = 0
string = "{0}{1}{2}{3}{4}{5}{6}" .format(first,second,third,fourth,fifth,sixth,seventh)   
if number >= 1:
    eighth =1
    number -= 1
else:
    eighth = 0
string = "{0}{1}{2}{3}{4}{5}{6}{7}" .format(first,second,third,fourth,fifth,sixth,seventh,eighth)     

print(string)


