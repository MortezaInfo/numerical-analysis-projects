import numpy as np
import sympy as sp
from scipy.interpolate import CubicSpline

x_points = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y_points = np.array([1, 3, 5, 8, 5, 2], dtype=float)

x = sp.Symbol('x')
poly = 0

for i in range(len(x_points)):
    Li = 1
    for j in range(len(x_points)):
        if i != j:
            Li *= (x - x_points[j]) / (x_points[i] - x_points[j])
    poly += y_points[i] * sp.simplify(Li)

poly_simplified = sp.expand(poly)
print("Lagrange polynomial:")
print(poly_simplified)

cs = CubicSpline(x_points, y_points, bc_type='natural')

print("\nCubic spline piecewise coefficients:")
for i in range(len(x_points) - 1):
    a = cs.c[3, i]
    b = cs.c[2, i]
    c = cs.c[1, i]
    d = cs.c[0, i]
    print(f"Interval [{x_points[i]}, {x_points[i+1]}]:")
    print(f"S{i}(x) = {a} + {b}(x-{x_points[i]}) + {c}(x-{x_points[i]})^2 + {d}(x-{x_points[i]})^3")
