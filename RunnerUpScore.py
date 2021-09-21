n = int(input())
#takes input,splits the input by white spaces, and maps the int function onto the resultant list of strings
arr = map(int, input().split())
new_arr = set(arr)
m=max(new_arr)
new_arr.remove(m)
print(max(new_arr))
