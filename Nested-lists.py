''' 
if __name__ == '__main__':
    l1=[]
    n=int(input())
    for _ in range(n):
        l1.append([])
        name = input()
        score = float(input())
        l1[0].append(name)
        l1[1].append(score)
    print(l1)
    '''

    '''
    Given the names and grades for each student in a class of N students, store them in a nested list and 
    print the name(s) of any student(s) having the second lowest grade.
    '''
    if __name__ == '__main__':
    a= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([score, name])

    a.sort()
    b = [i for i in a if i[0] != a[0][0]]
    c = [j for j in b if j[0] == b[0][0]]
    
    c.sort(key=lambda x: x[1])
    for i in range(len(c)):
        print(c[i][1])