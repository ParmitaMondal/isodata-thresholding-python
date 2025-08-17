# ISODATA (Ridler–Calvard) Image Thresholding in Python

A minimal NumPy/Python implementation of the **Ridler–Calvard / ISODATA** iterative thresholding algorithm.  
It mirrors a common MATLAB script (using `imhist`, iterative class means, and `im2bw`) and produces the same binary output.

## What it does
- Loads a grayscale image (e.g., `noisy_fingerprint.tif`)
- Computes a 256-bin histogram (uint8 images)
- Iteratively refines the threshold using class means until convergence
- Binarizes the image (like MATLAB `im2bw`) and displays it

## Files
- `isodata_threshold.py` – main script with the algorithm
- `requirements.txt` – dependencies

## Setup
```bash
git clone https://github.com/<your-username>/isodata-thresholding-python.git
cd isodata-thresholding-python
pip install -r requirements.txt
