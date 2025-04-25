# sequential search algorithm: linear search, binary search, jump search
colours = ["gelb", "lila", "blau", "rot","grün" , "grau", "weiß", "schwarz"]
letters = ["A", "C", "D", "E", "G", "H", "I", "Z"]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid]== target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid +1
        else:
            right = right -1 
    return -1

print(binary_search(letters, "H"))