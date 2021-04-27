
def line(length, pos):
    for i in range(length-pos):
        print(" ", end = '')
    for i in range(2*pos-1):
        print("*", end = '')
    print('')

def shape(size):
    for i in range(size):
        line(size, i)
    for i in range(size):
        line(size, size-i)

shape1=int(input("Enter Input Here:"))

shape(shape1)