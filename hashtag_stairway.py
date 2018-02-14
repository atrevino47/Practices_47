import sys

def staircase(n):
    # Complete this function
    
    space = ' '
    
    for i in range(n+1):
        if i != 0:
            print((space * (n-i)) + ('#' * (i)) )
    
    

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
