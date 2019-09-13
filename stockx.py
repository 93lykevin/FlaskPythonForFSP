import json
import pandas as pd
# import matplotlib as plt
import numpy
from stockxsdk import Stockx
stockx = Stockx()

supreme = stockx.search('supreme')
print(supreme[0].keys())
supreme = pd.DataFrame(supreme)
# print(supreme.head())