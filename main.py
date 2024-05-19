# b-> width of the rectangle
# a -> height of the rectangle
def make_rectangle(a, b):
    """
    Makes a rectangle of dimensions axb
    a: height of rectangle
    b: width of rectangle
    
    for e.g.
        make_rectangle(5, 15)
        
        >>> 
            ooooooooooooooo
            o             o
            o             o
            o             o
            ooooooooooooooo
    
    """
    for i in range(a):
        for j in range(b):
            if i == 0 or i == (a - 1):
                print("o", end="")
            else:
                if j == 0 or j == (b - 1):
                    print("o", end="")
                else:
                    print(" ", end="")
        print()







if __name__ == '__main__':
    make_rectangle(5, 15) # 5x15 
