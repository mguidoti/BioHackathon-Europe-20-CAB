import pandas as pd 
import logging

from source.connect_tb import get_data
from source.name_classifier import classify
from source.combine_tb import combine

from syno2pandas import splitCol2Rows


if __name__ == "__main__":
  # execute only if run as a script
  
  logging.basicConfig(
  filename='tb-connection.log',
  level=logging.INFO,
  format='%(levelname)s:%(asctime)s:%(name)s:%(message)s',
  datefmt='%Y-%m-%d %H:%M:%S'
  )
  
  original_taxon_list = [
      "Rhinolophus"
  ]

  taxon_list = classify(original_taxon_list)

  df = combine(taxon_list)
  
  # Attempt to split accession numbers
  try:
    df_split = splitCol2Rows(df)
    logging.info('Accession Numbers successfully splited!')
  except:
    logging.error('Problem while spliting accession numbers.')
  
  # Attempt to remove version digit from accession numbers
  try:
    df_split['AccessionNumber'] = df_split['AccessionNumber'].str.replace(
                                                                r'\.+\d', '')
    logging.info('Version digit correctly removed from all accession numbers!')
  except:
    logging.error('Problem while removing version digit from accession numbers.')
  
  # Attempt to save pickle file
  try: 
    df_split.to_pickle('data.pkl')
    logging.info('Pickle file successfully saved!')
    
  except:
    logging.error('Problem saving pickle file.')