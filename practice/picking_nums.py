def pickingNumbers(a):
    # Write your code here
    a.sort()
    low = 0
    high = 0
    local_low = 0
    local_high = 0
    for i in range(len(a)):
        if abs(a[local_low] - a[i]) <= 1:
            local_high = i
        else:
            if local_high - local_low > high - low:
                low = local_low
                high = local_high
            if a[i] - 1 in a:
                local_low = a.index(a[i-1])
                local_high = i
            else:
                local_low = i
                local_high = local_low
    if local_high - local_low > high - low:
        low = local_low
        high = local_high
    return high - low + 1

print(pickingNumbers([4, 6, 5, 3, 3, 1]))