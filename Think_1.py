
# source extraction finds the spacial footprint of neurons
# and deconvolution finds the denoised version of the signal using the autoregressive model


# in general 
# Motion correction has generally two steps:
# a.
# find the spacial footprint of the signal not so carefully, hence doing it in patches 
# b.
# we find roughly where the spacial footprint is, then we do the second time of source extraction and this time we refine the spacial footprint

