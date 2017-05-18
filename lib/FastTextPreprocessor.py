import csv
import os
import numpy as np
from shutil import copyfile

from .CSVReader import CSVReader
from .TxtManipulator import TxtManipulator
from .StringManipulator import StringManipulator

class FastTextPreprocessor:

	@ classmethod
	def normalize_content_data(cls, src, title, article):
		np_data = src + " " + title + " " + article
		np_data = np.array(np_data.split(" "))
		for i, dum in enumerate(np_data):
			np_data[i] = str(np_data[i])
			np_data[i] = StringManipulator.normalize_text(np_data[i], remove_stopword=True)

		return np_data
