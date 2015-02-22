import cv2
import numpy as np

def find_features(img, hessian_threshold=500):
    """Given a gray OpenCV image (such as from imread) return a list
    of OpenCV features and their descriptors as a tuple
    Params:
    img -- OpenCV image
    hessian_threshold -- threshold for feature selection
      (larger means fewer features)
    Returns:
    ([keypoints], [descriptors])
    """
    surf = cv2.SURF(hessian_threshold)
    kp, des = surf.detectAndCompute(img, None) # Second param is mask
    return (kp, des)

def display_features(img, kp):
    """Display window of image with feature keypoints superimposed
    The window closes on keypress
    Params:
    img -- OpenCV image
    kp -- list of keypoints outputted by surf.detect()
    Returns:
    None
    """
    kpimg = cv2.drawKeypoints(img, kp)
    cv2.imshow("Feature Keypoints", kpimg)
    cv2.waitKey(0)
    cv2.destroyWindow("Feature Keypoints")

def get_features(filename, hessian_threshold=500, sx=0.5, sy=0.5):
    """Loads an image from <filename>, performs preprocessing,
    and calls find_features() on it to retrieve features
    Preprocessing involves converting to grayscale and resizing
    Params:
    filename -- string indicating relative directory to file
    hessian_threshold -- threshold for feature selection (default 500)
    sx -- factor to resize in x (default 1)
    sy -- factor to resize in y (default 1)
    Returns:
    ([keypoints], [descriptors])
    """
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    resized_img = cv2.resize(gray, None, fx=sx, fy=sy, interpolation=cv2.INTER_NEAREST)
    return find_features(resized_img)

def get_normalized_features(filename):
    f = get_features(filename)
    f_normalized = np.array([v/np.linalg.norm(v) for v in f[1]])
    return (f_normalized, f_normalized.T)

sift = cv2.SIFT(500)

def get_descriptors(filename):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, des = sift.detectAndCompute(img, None)
    return des

if __name__ == "__main__":
    img = cv2.imread("img/test.jpg")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    (kp, _) = get_features("img/test.jpg")
    display_features(gray, kp)