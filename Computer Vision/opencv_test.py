import cv2
import matplotlib.pyplot as plt
arr = cv2.imread("DATA/00-puppy.jpg")
arr = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)
plt.imshow(arr)
plt.show()
