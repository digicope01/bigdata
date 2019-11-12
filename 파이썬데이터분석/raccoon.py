# raccoon.py
import scipy.misc
import matplotlib.pyplot as plt

face = scipy.misc.face()
face = face.copy()
acopy = face.copy()
aview = face.view()
# aview.flat = 0
plt.subplot(221)
plt.imshow(face)
plt.subplot(222)
plt.imshow(acopy)
plt.subplot(223)
plt.imshow(aview)
plt.show()