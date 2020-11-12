from .connect_tb import get_data

import pandas as pd
import logging, datetime

logger = logging.getLogger(__name__)

def combine(taxon_list):
  
  results = list()

  for taxon in taxon_list:
      
      taxon_results = get_data(taxon)

      if taxon_results != None:
          for hit in taxon_results:
              hit['query'] = taxon[0]
              hit['taxon_level'] = taxon[1]
              hit['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
              results.append(hit)

  try:
    logger.info('SUCCESS! Habemus a pandas.Dataframe from TB!')
    return pd.DataFrame(results)

  except:
    logger.error('Error converting TB results to a pandas.Dataframe')
    return None
    
    
