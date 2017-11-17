# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 19:12:47 2016

@author: RatneshK
"""

#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

words_file = "C:\Users\RatneshK\Documents\Python Scripts\First1\final_project_dataset.pkl"
authors_file="C:\Users\RatneshK\Documents\Python Scripts\First1\email_authors.pkl"
output = open(words_file)
enron_data = pickle.load(output)
    
print enron_data
output.close