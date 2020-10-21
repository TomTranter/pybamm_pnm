# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:20:20 2020

@author: Tom
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.close('all')


def RK(x, U0, A):
    R = 8.314
    T = 298.15
    F = 96485
    term1 = R*T/F*np.log((1-x)/x)
    term2 = 0
    for k in range(len(A)):
        term2 += (A[k]/F)*((2*x-1)**(k+1) - (2*x*k*(1-x))/(2*x-1)**(1-k))
    return U0 + term1 + term2

def RK_fit(x, U0, a0, a1, a2, a3, a4, a5, a6):
    A = [a0, a1, a2, a3, a4, a5, a6]
    R = 8.314
    T = 298.15
    F = 96485
    term1 = R*T/F*np.log((1-x)/x)
    term2 = 0
    for k in range(len(A)):
        term2 += (A[k]/F)*((2*x-1)**(k+1) - (2*x*k*(1-x))/(2*x-1)**(1-k))
    return U0 + term1 + term2

U0_LiCoO2 = -29.614
xmin_LiCoO2 = .45
x = np.linspace(xmin_LiCoO2, 0.99, 101)
A_LiCoO2 = [0.64832e7,
            -0.65173e7,
            0.65664e7,
            -0.65787e7,
            0.63021e7,
            -0.50465e7,
            0.27113e7,
            -0.69045e6]
plt.figure()
plt.plot(x, RK(x, U0_LiCoO2, A_LiCoO2))

test_x = x[::2]
test_rk = RK(test_x, U0_LiCoO2, A_LiCoO2) + (1 - np.random.random(len(test_x)))*5e-2
plt.figure()
plt.scatter(test_x, test_rk)
popt, pcov = curve_fit(RK_fit, test_x, test_rk)
x_wider = np.linspace(0.35, 0.99,101)
plt.plot(x_wider, RK_fit(x_wider, *popt))

def RKn_fit(x, U0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9):
    A = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
    R = 8.314
    T = 298.15
    F = 96485
    term1 = R*T/F*np.log((1-x)/x)
    term2 = 0
    for k in range(len(A)):
        term2 += (A[k]/F)*((2*x-1)**(k+1) - (2*x*k*(1-x))/(2*x-1)**(1-k))
    return U0 + term1 + term2

neg_ocp_data = np.array([
[0.003916912,	0.901051092],
[0.006841474,	0.715641404],
[0.012510623,	0.563924161],
[0.02353397,	0.418918412],
[0.042611108,	0.294092136],
[0.069179623,	0.236639504],
[0.100479928,	0.206126581],
[0.130497925,	0.199216368],
[0.161145828,	0.175448683],
[0.191786232,	0.148310253],
[0.221774234,	0.127917062],
[0.253127031,	0.12099935],
[0.284487327,	0.117452382],
[0.314520322,	0.117283657],
[0.345880618,	0.113736689],
[0.376581013,	0.113564215],
[0.407273909,	0.110020997],
[0.437966805,	0.106477778],
[0.469312103,	0.096189322],
[0.500642404,	0.079159376],
[0.5313353,	0.075616158],
[0.562043194,	0.078814428],
[0.593403489,	0.07526746],
[0.624111383,	0.07846573],
[0.654811778,	0.078293256],
[0.686839474,	0.074742539],
[0.716872469,	0.074573814],
[0.748232765,	0.071026846],
[0.778258261,	0.067487377],
[0.808943658,	0.060573414],
[0.839606559,	0.043547218],
[0.852249663,	0.026622257],
[0.864877768,	0.002955807]
])
neg_popt, pcov = curve_fit(RKn_fit, neg_ocp_data[:, 0], neg_ocp_data[:, 1])
plt.figure()
plt.scatter(neg_ocp_data[:, 0], neg_ocp_data[:, 1])
plt.plot(neg_ocp_data[:, 0], RKn_fit(neg_ocp_data[:, 0], *neg_popt))


pos_ocp_data = np.array([
[0.220677,	4.278846],
[0.248916,	4.211538],
[0.277195,	4.177885],
[0.301963,	4.168269],
[0.330854,	4.153846],
[0.352649,	4.125000],
[0.377973,	4.086538],
[0.400936,	4.048077],
[0.428631,	4.019231],
[0.455145,	3.990385],
[0.481660,	3.961538],
[0.509939,	3.927885],
[0.533504,	3.899038],
[0.557063,	3.865385],
[0.582987,	3.836538],
[0.610676,	3.802885],
[0.639568,	3.788462],
[0.673758,	3.764423],
[0.707358,	3.740385],
[0.735064,	3.721154],
[0.766304,	3.697115],
[0.796364,	3.673077],
[0.827014,	3.649038],
[0.859434,	3.625000],
[0.891854,	3.600962],
[0.920740,	3.581731],
[0.944322,	3.567308],
[0.969679,	3.557692],
[0.986181,	3.543269],
[0.995609,	3.533654],
[0.999694,	3.495192],
[1.000925,	3.038462]
])
#pos_popt, pcov = curve_fit(RK_fit, pos_ocp_data[:, 0], pos_ocp_data[:, 1], maxfev=100000)
plt.figure()
plt.scatter(pos_ocp_data[:, 0], pos_ocp_data[:, 1])
#plt.plot(pos_ocp_data[:, 0], RK_fit(pos_ocp_data[:, 0], *pos_popt))
x = np.linspace(pos_ocp_data[:, 0].min(), pos_ocp_data[:, 0].max(), 1001)
for n in [5,]:
    ppoly = np.poly1d(np.polyfit(pos_ocp_data[:, 0], pos_ocp_data[:, 1], n))
    plt.plot(x, ppoly(x), label=str(n))
plt.legend()
np.polynomial.polynomial.polyfit(pos_ocp_data[:, 0], pos_ocp_data[:, 1], n)