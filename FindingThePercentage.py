
n=int(input())
student_data={}
for i in range (n):
    #splits the input by white spaces,assigning the first item into name, and the rest of the items are assigned to line as a list
    name, *line = input().split() 
    #map() function maps float function onto the list(line) of strings
    marks = list(map(float,line))
    student_data[name] = marks
query_name = input()
total = sum(student_data[query_name])
average = total/3
#prints upto 2 decimal places
print("%.2f"%(average))

    
       

