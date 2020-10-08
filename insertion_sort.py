#Galen Borgman
#3/23/2020
#Insertion Sort
def insertion_sort(unsorted):
    for i in range(len(unsorted)):
        inserted = False
        j = 0
        while not inserted:
            if unsorted[i]


def main():
    unsorted = [0, 2, 3, 1, 6, -19, 100, 3]
    sorted_list = insertion_sort(unsorted)
    print("unsorted:")
    print(unsorted)
    print("sorted:")
    print(sorted_list)
if "__name__" == "__main__":
    main()
