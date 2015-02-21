"""Extract features from all images in library/* and pickle to library.features"""

import glob
import detect
import numpy as np
import numpy.lib.scimath as npmath
import cPickle
import cv2

def process_library(ims = 'library/*'):
    images = glob.glob(ims) # assume locations are encoded in these image filenames

    norm_features = []
    for name in images:
        print("extracting features of " + name)
        f = detect.get_features(name)
        f_normalized = np.array([v/np.linalg.norm(v) for v in f[1]])
        norm_features.append((f_normalized, f_normalized.T))

    tagged_features = list(zip(images, norm_features))

    cPickle.dump(tagged_features, open('library.features', 'w+'))

def load_library(library_file = 'library.features'):
    return cPickle.load(open(library_file))

if __name__ == "__main__":
    process_library()

    