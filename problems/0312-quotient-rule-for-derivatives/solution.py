import numpy as np

def quotient_rule_derivative(g_coeffs, h_coeffs, x):
    g_x = np.polyval(g_coeffs, x)
    h_x = np.polyval(h_coeffs, x)

    g_diff_coeffs = np.polyder(g_coeffs)
    h_diff_coeffs = np.polyder(h_coeffs)

    g_diff = np.polyval(g_diff_coeffs, x)
    h_diff = np.polyval(h_diff_coeffs, x)

    return (g_diff * h_x - g_x * h_diff) / (h_x ** 2)