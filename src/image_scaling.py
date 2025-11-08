import numpy as np

def interpolation_kernel(x):
    x = abs(x)
    if (x < 1):
        return (3/2) * x**3 - (5/2) * x**2 + (1)
    if (x < 2):
        return (-1/2) * x**3 + (5/2) * x**2 - (4) * x + (2)
    return 0

def bspline_kernel(x):
    x = abs(x)
    if (x < 1):
        return (1/2) * x**3 - x**2 + (2/3)
    if (x < 2):
        return (-1/6) * x**3 + x**2 - (2) * x + (4/3)
    return 0


def scale(image, new_resolution, kernel, kernel_radius=2):
    old_resolution = image.shape[0]
    new_image = np.zeros((new_resolution, new_resolution), dtype=np.float32)
    scale_factor = old_resolution / new_resolution
    
    for x_new in range(new_resolution):
        for y_new in range(new_resolution):
            x_old = x_new * scale_factor
            y_old = y_new * scale_factor
            
            x_start = int(np.floor(x_old - kernel_radius))
            x_end   = int(np.ceil(x_old + kernel_radius))
            y_start = int(np.floor(y_old - kernel_radius))
            y_end   = int(np.ceil(y_old + kernel_radius))
            
            summation = 0.0
            for m in range(x_start, x_end + 1):
                if m < 0 or m >= old_resolution: 
                    continue
                for n in range(y_start, y_end + 1):
                    if n < 0 or n >= old_resolution: 
                        continue
                    summation += image[m, n] * kernel(x_old - m) * kernel(y_old - n)
                    
            new_image[x_new, y_new] = summation
            
    return new_image