fruits = ["Orange","Pineapple","Banana","Grapes"] #creation
friends = ["Mary","Oscar","Fred", "John", "Rahab"] #creation
lucky_names = [2,4,5,2,5,3,6,9,5] #creation
print(fruits[0]) #access
print(fruits[0].isnumeric())

print(fruits) #print all elements

print(fruits[1:])
friends.extend(fruits)
print(friends)
friends.pop()
print(friends)
friends.sort(key=None, reverse=False)
print(friends)
friends.clear()
