# Insertion Sort
# running time of O(N^2) (aka dogshit) but its simple to use

# arr = [2, 6, 5, 1, 3, 4]
# how to become [1, 2, 3, 4, 5, 6]?

def insertion_sort(arr):
    for i in range(1, len(arr)):    # for 1 to length of array
        j = i
        while arr[j -1] > arr[j] and j > 0:   # checks for left side larger than current element; we also don't want j = 0
            arr[j -1], arr[j] = arr[j], arr[j -1]   # swaps the position if left > current
            j -= 1

arr = [2, 6, 5, 1, 3, 4]
insertion_sort(arr)
print(arr)

# extension problem:
# what if i want the list as an input, so I can sort any number?

arr = list(map(int, input().split(',')))
insertion_sort(arr)
print(arr)

# what if instead of number like X, Y, Z, I give X Y Z?
arr = list(map(int, input().split(' ')))
insertion_sort(arr)
print(arr)
