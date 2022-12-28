# Range declaration
start = 5
end = 20
 
if start % 2 != 0:
 
    for num in range(start, end + 1, 2):
        print(num, end=" ")
else:
 
    for num in range(start+1, end + 1, 2):
        print(num, end=" ")
