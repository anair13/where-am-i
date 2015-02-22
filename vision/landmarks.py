import csv
import source
import db
import detect

url_filter = set([
    "http://whc.unesco.org/en/list/252", # Taj Mahal
    "http://whc.unesco.org/en/list/86", # Pyramids at Giza
    "http://whc.unesco.org/en/list/373", # Stonehenge
    "http://whc.unesco.org/en/list/307", # Statue of liberty
    "http://whc.unesco.org/en/list/404", # Acropolis
    "http://whc.unesco.org/en/list/488", # Tower of London
])
# url_filter = [] # use this for no filter

def process_landmarks():
    with open('landmarks/landmarks.csv') as landmark_file:
        landmarks = csv.DictReader(landmark_file, delimiter=',', quotechar='"')

        counter = 0
        for row in landmarks:
            counter += 1

            if url_filter and not row['url'] in url_filter:
                # if filter is activated and url is not in the filter
                continue # skip
                
            print "fetching landmark " + str(counter) + ": " + row['name']

            metadata = row
            error = 0.001
            minx = float(row['longitude']) - error
            maxx = float(row['longitude']) + error
            miny = float(row['latitude']) - error
            maxy = float(row['latitude']) + error
            filenames = source.download_images(row['name'], 10, minx, miny, maxx, maxy)
            
            db.write_items([detect.get_descriptors(f) for f in filenames], metadata)

if __name__ == "__main__":
    process_landmarks()