Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop.
r =int(input("Enter range of dictionary "))
k=[ ]
v=[ ]
dict ={}
for i in range (r):
    a=input('enter keys ')
    k.append(a)
    a=input('enter values ')
    v.append(a)
for i in range (r):
    dict[k[i]]= v[i]    
print(dict)

#Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.
#Print the marks of a given student from that dictionary for every subject. 
#Hint: Use nested dictionary to store subjects marks.
student={'abc':{'sub1':100,'sub2':66,'sub3':89},'cde':{'sub1':77,'sub2':99,'sub3':66},'def':{'sub1':22,'sub2':88,'sub3':88}}
name=input("enter the name of student ")
for k,v in student.items():
    if name == k:
        print('sub 1:',student[k]['sub1'])
        print('sub 2:',student[k]['sub2'])
        print('sub 3:',student[k]['sub3'])
    
