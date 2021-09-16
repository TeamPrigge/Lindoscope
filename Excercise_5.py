def func_exp_1(x, a, b, c):
   return a * np.exp(-x / b) + c

def smooth(x, win):
    smooth = gaussian_filter1d(x, win) # change the gauss window
    return smooth 
