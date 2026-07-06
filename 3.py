import numpy as np
from scipy.integrate import quad, simpson, trapezoid

def f(x):
    return np.exp(x**2)

x = np.linspace(0, 1, 100)
y = f(x)

trap_result = trapezoid(y, x)

simp_result = simpson(y=y, x=x)

gauss_result, error = quad(f, 0, 1)

print(f"Trapezoidal: {trap_result:.6f}")
print(f"Simpson:     {simp_result:.6f}")
print(f"Gaussian:    {gauss_result:.6f}")
