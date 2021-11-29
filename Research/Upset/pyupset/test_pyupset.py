import pyupset as pyu
from pickle import load

with open('./test_data_dict.pckl','rb') as f:
	data_dict = load(f)
pyu.plot(data_dict)
