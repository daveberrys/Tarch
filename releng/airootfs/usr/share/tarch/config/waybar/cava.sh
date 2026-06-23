#!/bin/bash

# We add 'bars = 10' (or 8) to keep it short
cava -p <(echo "[output]
method = raw
channels = mono
raw_target = /dev/stdout
data_format = ascii
ascii_max_range = 7
autosens = 0
[general]
bars = 10 
[resampling]
resampler = linear
[smoothing]
noise_reduction = 15
") | sed -u 's/;//g;s/0/▁/g;s/1/▂/g;s/2/▃/g;s/3/▄/g;s/4/▅/g;s/5/▆/g;s/6/▇/g;s/7/█/g'

