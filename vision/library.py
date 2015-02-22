"""Extract features from all images in library/* and pickle to library.features"""

import glob
import detect
import numpy as np
import numpy.lib.scimath as npmath
import cv2
import db
import guides
import landmarks

def process_library(ims = 'library/*'):
    image_names = glob.glob(ims) # assume locations are encoded in these image filenames

    norm_features = []
    for name in image_names:
        print("extracting features of " + name)
        f = detect.get_features(name)
        f_normalized = np.array([v/np.linalg.norm(v) for v in f[1]])
        norm_features.append((f_normalized, f_normalized.T))

    for name, feature in zip(image_names, norm_features):
        print "writing " + name + " into mongo"
        metadata = {"name": name}
        db.write_item(feature, metadata)

def process_library(ims = 'library/*'):
    image_names = glob.glob(ims) # assume locations are encoded in these image filenames

    for name in image_names:
        metadata = {"name": name}
        db.write_item(detect.get_descriptors(name), metadata)

if __name__ == "__main__":
    db.client.drop_database('localize')
    process_library()
    landmarks.process_landmarks()
    guides.process_image_dataset()