# from sewar.full_ref import uqi
# from PIL import Image
# import numpy as np

# # Load grayscale images
# img_ref = np.array(Image.open('img006.jpg').convert('L'))
# img_a = np.array(Image.open('img010.jpg').convert('L'))
# img_b = np.array(Image.open('img006.jpg').convert('L'))


# # Compute UQI
# score_dark = uqi(img_ref, img_a)
# print("Score of A image:", score_dark)

# score_dark = uqi(img_ref, img_b)
# print("Score of B image:", score_dark)

from image_scaling import bspline_kernel
from image_scaling import interpolation_kernel
from image_scaling import scale

from PIL import Image
import numpy as np

img_ref = np.array(Image.open('img006.jpg').convert('L'), dtype=np.float32)
img_a = np.array(Image.open('img010.jpg').convert('L'), dtype=np.float32)

img_b = scale(img_ref, 128, bspline_kernel)
img_b = scale(img_b, 256, bspline_kernel)

img_c = scale(img_ref, 64, bspline_kernel)
img_c = scale(img_c, 256, bspline_kernel)

from sewar.full_ref import uqi

# Compute UQI
score_a = uqi(img_ref, img_a)
print("Score of A image:", score_a)

score_b = uqi(img_ref, img_b)
print("Score of B image:", score_b)

score_c = uqi(img_ref, img_c)
print("Score of C image:", score_c)








img_b_uint8 = np.clip(img_b, 0, 255).astype(np.uint8)
# Convert to PIL grayscale image
image_b_pil = Image.fromarray(img_b_uint8, mode='L')  # 'L' = grayscale
# Save or show
image_b_pil.save('img_b_scaled.jpg')

img_c_uint8 = np.clip(img_c, 0, 255).astype(np.uint8)
# Convert to PIL grayscale image
image_c_pil = Image.fromarray(img_c_uint8, mode='L')  # 'L' = grayscale
# Save or show
image_c_pil.save('img_c_scaled.jpg')