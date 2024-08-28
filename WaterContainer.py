def water_container(arr):
    n = len(arr)
    max_water = 0

    for i in range(n):
        for j in range(i+1, n):
            temp = j - i

            water = min(arr[i], arr[j]) * temp

            max_water = max(max_water, water)
            
    return max_water



arr = [1,8,6,2,5,4,8,3,7]

res = water_container(arr)

print(res)