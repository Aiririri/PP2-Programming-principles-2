
#python booleans
print (10 > 9) #True
print (10 = 9) #False
print (10 < 9) #False

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #"b is not greater than a
  
print(bool("Hello"))#True
print(bool(15))#True

x = "Hello"
y = 15

print(bool(x))#True
print(bool(y))#True

bool("abc")#True
bool(123)#True
bool(["apple", "cherry", "banana"])#True

bool(False)#False
bool(None)#False
bool(0)#False
bool("")#False
bool(())#False
bool([])#False
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))#False


def myFunction() :
  return True

print(myFunction())#True




def myFunction() :
  return True

if myFunction():
  print("YES!") #output: YES!
else:
  print("NO!")



x = 200
print(isinstance(x, int))#True






