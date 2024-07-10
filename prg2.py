list1 = [11, 5, 17, 18, 23]

def list_sum(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + list_sum(list, size - 1)

sum = list_sum(list1, len(list1))
 
print("Sum of all elements : ", sum)