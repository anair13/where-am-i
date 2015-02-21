import library
import match
import db

def get_location(filename):
    """Extracts latitude, longitude, angle from filename like 123.01_54.64_330.jpg"""
    prefix = ".".join(filename.split(".")[:-1]) # get rid of suffix
    x = prefix.split("_")
    return float(x[0]), float(x[1]), float(x[2])

def max_index(values):
    return max(xrange(len(values)),key=values.__getitem__)

def find_match(filename):
    feature_iterator = db.get_all_images()
    x = match.get_normalized_features(filename)
    matches = [(match.correlation(x, y), metaID) for y, metaID in feature_iterator]
    correlation, metaID = max(matches)
    return db.get_meta(metaID)

if __name__ == "__main__":
    print get_location("123.01_54.64_330.jpg")
    print find_match("img/test.jpg")