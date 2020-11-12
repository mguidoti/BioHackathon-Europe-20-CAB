import pandas as pd 
import logging

from source.connect_tb import get_data
from source.name_classifier import classify
from source.combine_tb import combine





if __name__ == "__main__":
  # execute only if run as a script
  
  logging.basicConfig(
  filename='tb-connection.log',
  level=logging.INFO,
  format='%(levelname)s:%(asctime)s:%(name)s:%(message)s',
  datefmt='%Y-%m-%d %H:%M:%S'
  )
  
  original_taxon_list = [
      "Pterovianaida duckensis",
      "Pterovianaida melchiori",
      "Rhinolophus",
      "Rhinolophys"
  ]

  taxon_list = classify(original_taxon_list)

  df = combine(taxon_list)
  
  print(df.shape)
  # Send the DF to your functions here, Dario
