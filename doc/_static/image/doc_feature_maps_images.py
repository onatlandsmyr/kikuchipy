import os

import matplotlib

matplotlib.rcParams["backend"] = "qt5agg"
import matplotlib.pyplot as plt
import numpy as np
import scipy

import kikuchipy as kp

data = "/home/hakon/kode/kikuchipy/kikuchipy/data/kikuchipy/patterns.h5"
data2 = "/home/hakon/phd/data/ni/2020/1/nordif/Pattern.dat"
outdir = "/home/hakon/kode/kikuchipy/doc/_static/image"
featdir = os.path.join(outdir, "feature_maps")

datadir, fname = os.path.split(data)
fname, ext = os.path.splitext(fname)
s = kp.load(data, lazy=False)
s2 = kp.load(data2, lazy=False)

# Image quality
s3 = s2.deepcopy()
s3.remove_static_background()
s3.remove_dynamic_background()
# Image quality map
iq = s3.get_image_quality()
x, y = 157, 80
iq_perc = np.percentile(iq, q=(0, 99.8))
plt.figure()
plt.imshow(iq, vmin=iq_perc[0], vmax=iq_perc[1])
plt.colorbar(label="Image quality")
plt.savefig(
    os.path.join(featdir, "iq.png"), bbox_inches="tight", pad_inches=0,
)
# Pattern
p = s3.inav[x, y].data
plt.figure()
plt.imshow(p)
plt.colorbar()
plt.savefig(
    os.path.join(featdir, "image_quality_pattern.png"),
    bbox_inches="tight",
    pad_inches=0,
)
# Pattern FFT
p_fft = kp.util.pattern.fft(p, shift=True)
p_spec = kp.util.pattern.fft_spectrum(p_fft)
plt.figure()
plt.imshow(np.log(p_spec))
plt.colorbar()
plt.savefig(
    os.path.join(featdir, "fft_spectrum.png"),
    bbox_inches="tight",
    pad_inches=0,
)
# Frequency vectors
q = kp.util.pattern.fft_frequency_vectors(shape=p.shape)
plt.figure()
plt.imshow(scipy.fft.fftshift(q))
plt.colorbar()
plt.savefig(
    os.path.join(featdir, "fft_frequency_vectors.png"),
    bbox_inches="tight",
    pad_inches=0,
)