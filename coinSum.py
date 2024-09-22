def find_sums(arr):
  
  def generate_sums(index, current_sum):
    if index == len(arr):
      sums.add(current_sum)
      return
    generate_sums(index + 1, current_sum + arr[index])
    generate_sums(index + 1, current_sum)
  
  sums = set()
  generate_sums(0, 0)
  sums.discard(0)
  distinct_sums = sorted(sums)
  print(len(distinct_sums))
  print(*distinct_sums)

n = 3
arr = [3, 5, 2]
find_sums(arr)