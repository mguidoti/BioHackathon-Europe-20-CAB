import pandas, logging

from source.connect_tb import get_data
from source.name_classifier import classify

if __name__ == "__main__":
  # execute only if run as a script
  
  logging.basicConfig(
  filename='tb-connection.log',
  level=logging.INFO,
  format='%(levelname)s:%(asctime)s:%(name)s:%(message)s',
  datefmt='%Y-%m-%d %H:%M:%S'
  )
  
  original_taxon_list = [
    "Pterovianaida duckensis"
  ]
  
  taxon_list = classify(original_taxon_list)
  
  for taxon in taxon_list:
    print(get_data(taxon))
    