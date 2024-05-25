def lower_triangular(n):
    for i in range(n):
        print("* " * (i+1))

def upper_triangular(n):
    for i in range(n):
        print("  " * i + "* " * (n-i))

def pyramid(n):
    for i in range(n):
        print(" " * (n-i-1) + "* " * (i+1))

n = int(input("Enter the size of the pattern: "))
    
print("\nLower Triangular:")
lower_triangular(n)

print("\nUpper Triangular:")
upper_triangular(n)

print("\nPyramid:")
pyramid(n)
