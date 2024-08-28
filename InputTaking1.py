# 4


# split method :- it works with a string

# s = 'invalid, literal, for int(), with base'
# li = []

# li = s.split(",")

# print(li)

# ------------------------------------------------------------------------------

# map 

# li = [3,1,2,4,5,6]

# for i in range(len(li)):
#     li[i] = (2* li[i])

#     print(li[i])

# ------------------------------------------------------------------------------

# numbers = ['1', '2', '4', '6', '10']

# ans  = list(map(int, numbers))
# print(type(numbers[0]))
# print(type(ans[0]))

# ------------------------------------------------------------------------------


# n = int(input("Enter range: "))
# arr = list(map(int, input().split()))

# print(arr)

# ------------------------------------------------------------------------------


# Taking n*m matrix 

# n is number of column 
# m is number of row 

n = int(input("Enter the size of matrix n & m: "))
print(f'matrix row would be {n} and column would be {n}')
print("Enter the elements of each row")
mat = []

for _ in range(n):
    mat.append(list(map(int, input().split())))

print(mat)