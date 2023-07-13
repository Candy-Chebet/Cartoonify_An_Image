import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import *

photo = askopenfilename()
img = cv2.imread(photo)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey = cv2.medianBlur(grey, 5)
edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#cartoonize
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask = edges)

cv2.imshow("Image", img)
cv2.imshow("Cartoon", cartoon)

image_path = photo
# Display the original and cartoonified images
original_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB))
plt.title('Cartoonified Image')
plt.axis('off')
plt.show()

#save
cv2.imwrite("cartoon.jpg", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()