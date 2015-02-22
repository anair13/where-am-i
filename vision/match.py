"""Finds matching features and pickles matching information to files"""
import detect
import numpy as np
import numpy.lib.scimath as npmath
import pickle
import cv2

def match_oneway(features_1, features_2):
    """One way descriptor matching image f1 to f2, adapted from Solem"""
    f1 = features_1
    f2 = features_2

    ratio = 0.7 # higher number means more matches
    size = f1.shape[0]

    scores = np.zeros((size, 1), 'int')

    for i in range(size):
        product = 0.9999 * np.dot(f1[i, :], f2)
        cosines = npmath.arccos(product)
        index = np.argsort(cosines)

        if cosines[index[0]] < ratio * cosines[index[1]]:
            scores[i] = int(index[0])

    return scores

def match(features_1, features_2):
    """Computes two way matches, removes matches that are not symmetric"""
    matches_12 = match_oneway(features_1[0], features_2[1])
    matches_21 = match_oneway(features_2[0], features_1[1])

    index_12 = matches_12.nonzero()[0]

    for n in index_12:
        if matches_21[int(matches_12[n])] != n:
            matches_12[n] = 0 # zero if not symmetric

    return matches_12

def _correlation(features_1, features_2):
    return sum(match(features_1, features_2) > 0)

def correlation(des1, des2):
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5) # 5
    search_params = dict(checks = 50) # 50

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)

    return len(good)

def get_normalized_features(filename):
    f = detect.get_features(filename)
    f_normalized = np.array([v/np.linalg.norm(v) for v in f[1]])
    return (f_normalized, f_normalized.T)

if __name__ == "__main__":
    names = ["img/test.jpg", "img/clock_tower_2.jpg", "img/campanile_2.jpg"]
    features = [detect.get_features(f) for f in names]

    norm_features = []
    for f in features:
        f_normalized = np.array([v/np.linalg.norm(v) for v in f[1]])
        norm_features.append((f_normalized, f_normalized.T))

    for i in range(len(norm_features)):
        for j in range(i, len(norm_features)):
            print names[i], names[j], _correlation(norm_features[i], norm_features[j])