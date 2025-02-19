# a = ["apple", "banana", "cherry"]
# b = ["mango", "pineapple", "papaya"]
# c = ("mango", "pineapple", "papaya")
# a.extend(b)
# a.extend(c)

# print(a)


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# # thislist.remove("banana")
# thislist.pop(3)

# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])

# thislist = ["apple", "banana", "cherry"];
# i = 0;
# while i < len(thislist):
#     print(thislist[i]);
#     i = i+1;

# thislist = ["apple", "banana", "cherry"];

# [print(x) for x in thislist]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"];
# # newList = [];

# newList = [x for x in fruits if 'a' in x]
# print(newList)

# for x in fruits:
#     print(x)
#     if 'a' in x:
#         print(x);
#         newList.append(x);

# print(newList);

# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "apple"];
# # newList = [x for x in fruits if x != "apple"];
# newList = [x for x in fruits];
# print(newList)


# newList = [x for x in range(10) if x > 5]
# print(newList)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "apple"];
# newlist = [x.upper() for x in fruits]
# newlist = [x.lower() for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "apple"];
# # newList = ['hello' for x in fruits]
# # newList = [x if x != 'banana' else "orange" for x in fruits]
# newList = []
# for x in fruits:
#     if x != 'banana':
#         newList.append(x)
#     else:
#         newList.append('orange')
# print(newList)


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)


# thislist = [58, 100, 50, 65, 82, 23]
# thislist.sort(reverse=True)
# print(thislist)

# def myFun(n):
#     return abs(n-60)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key=myFun)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# # thislist.sort()
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)


# start hare tomrrow.

https://www.w3schools.com/python/python_lists_join.asp