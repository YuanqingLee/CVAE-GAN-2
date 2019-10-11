import os
import sys
import re
import zipfile

import numpy as np
import h5py

import requests
from PIL import Image
'''
attr_file = 'list_attr_celeba.txt'

with open(attr_file, 'r') as lines:
    lines = [l.strip() for l in lines]
    num_images = int(lines[0])

    label_names = re.split('\s+', lines[1])
    label_names = np.array(label_names, dtype=object)
    #print(label_names)
    num_labels = len(label_names)

    lines = lines[2:]
    labels = np.ndarray((num_images, num_labels), dtype='uint8')
    for i in range(num_images):
        label = [int(l) for l in re.split('\s+', lines[i])[1:]]
        label = np.maximum(0, label).astype(np.uint8)
        labels[i] = label
'''

f = h5py.File('celebB.hdf5')
print(f['images'])
