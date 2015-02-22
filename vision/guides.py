import csv
import source
import db
import detect
import os

def process_image_dataset():
    with open('sites/historical_sites.csv') as sites_file:
        sites = csv.DictReader(sites_file, delimiter=',', quotechar='"')
        filenames = []
        for row in sites:
            filenames.append('guide/' + row['Filename'])

    print filenames

    with open('sites/historical_sites.csv') as sites_file:
        sites = csv.DictReader(sites_file, delimiter=',', quotechar='"')
        for row, f in zip(sites, filenames):
            if os.path.exists(f):
                metadata = row
                db.write_item(detect.get_descriptors(f), metadata, db.db.guide)

if __name__ == "__main__":
    process_image_dataset()