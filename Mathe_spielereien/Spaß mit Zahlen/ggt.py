#here i want to find the ggt of two numbers for using it just print(ggt(a,b))

def ggt(a, b):
    #default values
    array = []
    x = 2
    if a > b:
        first = a
        secound = b
    else:
        first = b
        secound = a

    while x>1:
        x = first % secound
        array.append(x)
        if x > secound:
            first = x
        else: 
            first = secound
            secound = x 
    array.sort()
    for i in range(len(array)):
        if array[i] == 0 or array[i] == 1:
            return array [i+1]
# how do i get only the last number before 0 efficiently ?
print(ggt(99, 78))
# ggt(99,78) = 3
