
def oddCount(lst):
    count = 0
    for num in lst:
        if num % 2 != 0:
            count += 1
    return count
print(oddCount([1, 2, 3, 4, 5]))  # Output: 3