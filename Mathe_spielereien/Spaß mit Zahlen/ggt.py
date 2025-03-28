#here i want to find the ggt of two numbers
#not working
def ggt(a, b):
    #default values
    array = []
    x= 0
    if a> b:
        first = a
        secound = b
    else:
        first = b
        secound = a

    while x != 1:
        x = first % secound
        array.append(x)
    return array
ggt(99, 78)