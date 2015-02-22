import library
import match
import db
import glob
import detect

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
    def get_name(id):
        return db.get_meta(id)['name']
    matches = [(int(match.correlation(x, y)), metaID) for y, metaID in feature_iterator]
    for x, i in sorted(matches):
        if x:
            print x, get_name(i)
    correlation, metaID = max(matches)
    return db.get_meta(metaID)

def find_match(filename):
    feature_iterator = db.get_all_images()
    x = detect.get_descriptors(filename)
    def get_name(id):
        return db.get_meta(id)['name']
    matches = [(int(match.correlation(x, y)), metaID) for y, metaID in feature_iterator]
    # for x, i in sorted(matches):
    #     if x:
    #         print x, get_name(i)
    correlation, metaID = max(matches)
    return db.get_meta(metaID)

if __name__ == "__main__":
    print get_location("123.01_54.64_330.jpg")
    for name in glob.glob("img/*.jpg"):
        des1 = detect.get_descriptors(name)
        # for img in glob.glob("img/*/*.jpg"):
        #     des2 = detect.get_descriptors(img)
        #     print name, img, match.correlation_files(des1, des2)
        print name
        print find_match(name)
        print "---"