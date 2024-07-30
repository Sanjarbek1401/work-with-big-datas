import cmath

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    # Find the two solutions using the quadratic formula
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    roots = [root1, root2]
    real_roots = [r.real for r in roots if r.imag == 0]
    complex_roots = [r for r in roots if r.imag != 0]
    
    real_roots.sort()
    sorted_roots = real_roots + complex_roots
    
    return sorted_roots

# Example usage
a = 1
b = 6
c = 45

solutions = solve_quadratic(a, b, c)
print("The solutions are:", solutions)

 
""" import cmath

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Find the two solutions using the quadratic formula
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return root1, root2

# Example usage
a = 1
b = 6
c = 45

solutions = solve_quadratic(a, b, c)
print("The solutions are:", solutions)
 """