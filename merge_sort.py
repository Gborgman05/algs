#Galen Borgman
#3/23/2020
#Merge Sort
def merge_sort(unsorted: list):
    if len(unsorted) == 1:
        return unsorted
    else:
        left = merge_sort(unsorted[:len(unsorted) // 2])
        right = merge_sort(unsorted[len(unsorted) // 2:])
        l_pointer = 0
        r_pointer = 0
        while l_pointer + r_pointer < len(unsorted):
            if r_pointer >= len(right) or (l_pointer < len(left) and left[l_pointer] <= right[r_pointer]):
                unsorted[l_pointer + r_pointer] = left[l_pointer]
                l_pointer += 1
            else:
                unsorted[l_pointer + r_pointer] = right[r_pointer]
                r_pointer += 1
        return unsorted

if __name__ == "__main__":
    print(merge_sort([3,6,8,3,1,-10]))
