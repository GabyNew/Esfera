import numpy as np

# Constante de Stefan-Boltzmann
cte= 5.67e-8

r = 0.15
error_r = 0.01
e = 0.90 
error_e = 0.05
T = 550
error_T = 20

# Área superficial de una esfera (4 * pi * r^2)
A= 4 * np.pi * r**2

# ley de Stefan-Boltzmann)
H = A * e * cte * T**4

rmax = r + error_r
rmin = r - error_r
emax = e + error_e
emin = e - error_e
Tmax = T + error_T
Tmin = T - error_T

Amax = 4 * np.pi * rmax**2
Amin = 4 * np.pi * rmin**2

Hmax = Amax * emax * cte * Tmax**4
Hmin = Amin * emin * cte * Tmin**4

# Mostrar resultados
print("\nProblema 4.10 (Esfera de cobre):")
print(f"H = {H:.2f} W")
print(f"H_min = {Hmin:.2f} W")
print(f"H_max = {Hmax:.2f} W")
