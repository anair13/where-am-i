import csv
import source
import db
import detect

def process_image_dataset():
	with open('sites/sites.csv') as sites_file:
		sites = csv.DictReader(sites_file, delimiter=',', quotechar='"')
		filenames = []
		for row in sites:
			filenames += row['Filename']

		sites = csv.DictReader(sites_file, delimiter=',', quotechar='"')

		for row in sites:
			metadata = row
			db.write_items([detect.get_descriptors(f) for f in filenames], metadata)