import numpy as np
import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime, date
from get_games import get_games

years = [2012, 2013, 2014, 2015, 2016]

for year in years:
	print(year)
	df = get_games(year)

	directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), str(year))
	if not os.path.exists(directory):
	    os.makedirs(directory)

	df.reset_index().to_csv(os.path.join(directory,'games.csv'), index=False, sep="|")