def InflectionPoints(x):

    smooth = gaussian_filter1d(x, 900) # change the gauss window
    second_deravitive = np.gradient(np.gradient(smooth))
    inflec_Points = np.where(np.diff(np.sign(second_deravitive)))[0]

    return inflec_Points
