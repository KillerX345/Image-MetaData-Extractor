# Image metadata extractor by Kush Janani
# Copyright (c) 2023 Kush Janani
# This code is provided as-is, with no warranty or guarantee of fitness for any purpose.
# Use at your own risk.

import csv
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(image):
    # Extract EXIF data from image
    image.verify()
    return image._getexif()

def get_metadata(image):
    # Get image format and select appropriate method for extracting metadata
    image_format = image.format
    if image_format == 'JPEG':
        exif = get_exif(image)
        metadata = {}
        if exif is not None:
            for tag, value in exif.items():
                tag_name = TAGS.get(tag, tag)
                metadata[tag_name] = value
        return metadata
    elif image_format in ['PNG', 'GIF', 'BMP']:
        return image.info
    else:
        return None

def export_metadata_to_csv(metadata, output_path):
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for key, value in metadata.items():
            writer.writerow([key, value])

# Example usage:
image_path = 'xxx_doge.jpg'
output_path = 'metadata.csv'
with Image.open(image_path) as image:
    metadata = get_metadata(image)
    if metadata is not None:
        export_metadata_to_csv(metadata, output_path)
        print(f"Metadata for {image_path} exported to {output_path}")
    else:
        print(f"Unsupported image format: {image_path}")
