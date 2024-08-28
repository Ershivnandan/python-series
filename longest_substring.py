def longest_substring(s, n, k):
  max_len = 0
  
  for unique_chars in range(1, 27):
    left = 0
    window_freq = {}
    num_unique = 0
    num_at_least_k = 0
    
    for right in range(n):
      if s[right] not in window_freq:
        window_freq[s[right]] = 0
        num_unique += 1
      window_freq[s[right]] += 1
      
      if window_freq[s[right]] == k:
        num_at_least_k += 1
      
      while num_unique > unique_chars:
        if window_freq[s[left]] == k:
          num_at_least_k -= 1
        window_freq[s[left]] -= 1
        if window_freq[s[left]] == 0:
          del window_freq[s[left]]
          num_unique -= 1
        left += 1
      
      if num_unique == num_at_least_k:
        max_len = max(max_len, right - left + 1)
  
  print(max_len)

n = int(input())

s = input()

k = int(input())
  
longest_substring(s, n, k)
