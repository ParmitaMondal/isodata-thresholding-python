import numpy as np
import imageio.v2 as imageio   # or: from skimage import io as imageio
import matplotlib.pyplot as plt

# --- load image (grayscale) ---
I = imageio.imread('noisy_fingerprint.tif')
if I.ndim == 3:  # convert RGB to gray if needed
    I = (0.2989*I[...,0] + 0.5870*I[...,1] + 0.1140*I[...,2]).astype(I.dtype)

# --- histogram like MATLAB's imhist (256 bins for uint8) ---
counts, N = np.histogram(I.ravel(), bins=256, range=(0, 255))
N = N[:-1]  # bin centers (0..255)

# --- initial threshold T(1) ---
mu_total = counts.sum()
T_prev = np.round((N * counts).sum() / mu_total).astype(int)

# --- compute class means and iterate until convergence ---
def class_mean(counts, N, a, b):
    # mean of histogram slice [a:b] inclusive on bins, guarding empty slices
    c = counts[a:b+1]
    n = N[a:b+1]
    s = c.sum()
    return 0.0 if s == 0 else float((n * c).sum() / s)

T_curr = int(np.round(0.5 * (
    class_mean(counts, N, 0, T_prev) + class_mean(counts, N, T_prev, len(N)-1)
)))

while abs(T_curr - T_prev) >= 1:
    T_prev = T_curr
    mbt = class_mean(counts, N, 0, T_prev)                   # mean below threshold
    mat = class_mean(counts, N, T_prev, len(N)-1)            # mean above threshold
    T_curr = int(np.round(0.5 * (mbt + mat)))

Threshold = T_curr

# --- convert to MATLAB's 'level' in [0,1] and binarize like im2bw ---
level = (Threshold - 1) / (N[-1] - 1)  # same normalization as your code
BW = (I >= Threshold).astype(np.uint8)  # im2bw uses >= threshold on grayscale

# --- show result ---
plt.imshow(BW, cmap='gray')
plt.axis('off')
plt.show()
