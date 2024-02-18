#Write a Python program to print all positive numbers in a range.
lst1=[2,-4,9,-8,-7,9,34,23,24,-3,9,-3]
lst2=[]
for i in range(0,len(lst1)):
    if(lst1[i]>0):
        lst2.append(lst1[i])
print("Positive numbers in the range:", lst2)