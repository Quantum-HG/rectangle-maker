'''
MIT License

Copyright (c) 2024 Quantum-HG

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''





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
