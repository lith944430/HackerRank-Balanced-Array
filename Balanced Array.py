left = [0]
x=0
arr=[1,2,3,3]
print(arr)
for i in range(1, len(arr)):
    x+=arr[i-1]
    left.append(x)
print(left)


right = [0]
y=0
arr=[1,2,3,3]
arr.reverse()
for i in range(1, (len(arr))):
    y+=arr[i-1]
    right.append(y)
right.reverse()
print(right)

arr.reverse()
for i in range(1, len(arr)):
    if left[i]==right[i]:
        print (i)

        
