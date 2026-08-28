import numpy as np

def hdi(theta, pdf, confidence=0.95):
    sorted_p = np.sort(pdf)[::-1]
    HDI_height = sorted_p[np.cumsum(sorted_p) >= level*sum(sorted_p)][0]
    HDI_mass = sum(pdf[pdf >= HDI_height])
    HDI = theta[pdf >= HDI_height]
    mean = theta[np.argmax(pdf)]

    return HDI[0], HDI[-1]