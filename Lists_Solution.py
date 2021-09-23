if __name__ == '__main__':
    N = int(input())
    num_list=[]
    for i in range(N):
        query, *line =input().split()
        nums=list(map(int,line))
        if "insert" in query:
            num_list.insert(nums[0],nums[1])
        elif "append" in query:
            num_list.append(nums[0])
        elif "remove" in query:
            num_list.remove(nums[0])
        elif "sort" in query:
            num_list.sort()
        elif "pop" in query:
            num_list.pop()
        elif "reverse" in query:
            num_list.reverse()
        elif "print" in query:
            print(num_list)