import library
import match

def max_index(values):
    return max(xrange(len(values)),key=values.__getitem__)

def find_match(filename):
    names, lib_features = zip(*library.load_library())
    x = match.get_normalized_features(filename)
    matches = [match.correlation(x, y) for y in lib_features]
    return names[max_index(matches)]

if __name__ == "__main__":
    print find_match("img/test.jpg")