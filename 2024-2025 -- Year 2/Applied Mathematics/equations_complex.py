import math

def solve_quadratic(a, b, c):
    # Дискриминант
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))

# Уравнение (a): x^2 + 8x + 20 = 0
print("Equation (a): x^2 + 8x + 20 = 0")
a_roots = solve_quadratic(1, 8, 20)
print(f"Roots of equation (a): {a_roots}")

# Уравнение (b): 1/2 * x^3 - 2x^2 + 4x = 0
print("\nEquation (b): 1/2 * x^3 - 2x^2 + 4x = 0")

# Первый корень x = 0
b_roots = [0]

# Решаем квадратное уравнение 1/2 * x^2 - 2x + 4 = 0
quadratic_roots = solve_quadratic(0.5, -2, 4)
b_roots.extend(quadratic_roots)

print(f"Roots of equation (b): {b_roots}")
