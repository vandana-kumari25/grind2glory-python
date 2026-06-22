def largest(arr):
    largest_num = arr[0]

    for num in arr:
        if num > largest_num:
            largest_num = num

    return largest_num

print(largest([10, 5, 25, 7]))