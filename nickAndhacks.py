def nickAndHacks(n, nick=1):
    if nick > n:
        return "No"
    if nick == n:
        return "Yes"
    
    found = (nickAndHacks(n, nick * 10) == "Yes") or (nickAndHacks(n, nick * 20) == "Yes")
    return "Yes" if found else "No"


# Test cases
test_cases = [1, 2, 10, 25, 200]
results = [nickAndHacks(n) for n in test_cases]

for result in results:
    print(result)
