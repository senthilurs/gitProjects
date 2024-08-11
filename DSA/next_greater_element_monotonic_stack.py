def next_greater_element(arr):
    n = len(arr)
    stack = []
    result = [-1] * n
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            print(i,stack,)
            result[stack.pop()] = arr[i]
        
        stack.append(i)
    
    return result

input = [1,4,6,3,2,7]
print(next_greater_element(input))
