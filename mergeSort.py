import random
from re import sub

def merge(arr, l, mid, r):
    # print(f"I received {arr[l:r]}, {l, mid, r}")
    l_pointer = 0
    r_pointer = 0

    # Sorted Sub arrays to join:
    L = arr[l:mid]
    R = arr[mid:r]
    # print(L, R)
    l_length = len(L)
    r_length = len(R)
    # print(f"length of each sub array: {sub_arr_length}")

    #print(f"len of array: {len(arr[l:r])}")
    for i in range(l, r):
        # print(arr[l:i+1])
        # print(f"left pointer: {l_pointer}, right pointer: {r_pointer}")
        # print(f"comparing {L[l_pointer]} and {R[r_pointer]}")
        if r_pointer == r_length:
            arr[i] = L[l_pointer]
            l_pointer += 1
        elif l_pointer == l_length:
            arr[i] = R[r_pointer]
            r_pointer += 1
        elif L[l_pointer] < R[r_pointer]:
            # print("left was smaller")
            arr[i] = L[l_pointer]
            l_pointer += 1
        elif L[l_pointer] > R[r_pointer]:
            # print("right was smaler")
            arr[i] = R[r_pointer]
            r_pointer += 1
        else:
            # print("no condition for incertion was met")
            arr[i] = L[l_pointer]
            l_pointer += 1
        # print(f"array after incertion: {arr[l:i+1]}\n")
    
    # print(f"merged array: {arr[l:r]}")
    # return arr[l:r]


def mergeSort(arr, l, r):
    # print(l, r)
    # print("My current array: " + str(arr[l:r]))
    if l == r-1:
        return
    
    mid = (l + r) // 2

    # print("left call on array " + str(arr[l:r]))
    mergeSort(arr, l, mid)
    # print("right call on array " + str(arr[l:r]))
    mergeSort(arr, mid, r)

    # print(f"merging array {arr[l:mid]} and {arr[mid:r]}")
    merge(arr, l, mid, r)







my_array = [random.randint(0, 20) for i in range(15)]
print(f"array bf sorting: {my_array}\n")
mergeSort(my_array, 0, len(my_array))
print(f"\narray after sorting: {my_array}")


#print(merge([3, 5, 8, 1, 4, 7], 0, 3, 6))