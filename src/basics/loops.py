#While Loops
i = 1 #declare the initiator state
while i <= 10:
    print("Loop number "+str(i))
    i +=1

#For Loops
for letter in "Gichure Academy":
    print(letter)
    
friends = ["Mary","Oscar","Fred", "John", "Rahab"]

for friend in friends:
    print(friend)

for index in range(10):
    print(index)
    
for index in range(4,10):
    print(index)
    
for index in range(len(friends)):
    print(friends[index])
    
for index in range(10):
    if(index % 2 == 0):
        print(str(index) + " is even number")
    else:
        print(str(index) + " is odd number")