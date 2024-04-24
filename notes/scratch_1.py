data = [3,7,6,2,5,4]
print(len(data))
A = [3,7,6]
B = [2,5,4]
i = 0
j = 0
L =[]
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        L.append(A[i])
        i += 1
    else:
        L.append(B[j])
        j += 1
# Add any remaining elements once one list is empty
L += A[i:] + B[j:]
print(L)