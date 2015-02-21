import library
import match

def get_location(filename):
    """Extracts latitude, longitude, angle from filename like 123.01_54.64_330.jpg"""
    prefix = ".".join(filename.split(".")[:-1]) # get rid of suffix
    x = prefix.split("_")
    return float(x[0]), float(x[1]), float(x[2])

def max_index(values):
    return max(xrange(len(values)),key=values.__getitem__)

def find_match(filename):
    names, lib_features = zip(*library.load_library())
    x = match.get_normalized_features(filename)
    matches = [match.correlation(x, y) for y in lib_features]
    return names[max_index(matches)]

if __name__ == "__main__":
    print get_location("123.01_54.64_330.jpg")
    print find_match("img/test.jpg")