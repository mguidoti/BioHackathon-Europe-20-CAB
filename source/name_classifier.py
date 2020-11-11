import logging

logger = logging.getLogger(__name__)

def classify(taxon_names):
  """Classifies taxons names into family, genus, species statuses

  Args:
      name (list): List of strings containing all desired taxon names

  Returns:
      list: list of tuples containing a taxon name and its respective status
  """
  
  family_group = ['idae', 'inae']
  
  resulting_list = list()
  
  for name in taxon_names:
  
    # avoids for empty queries and genera names with less than two chars
    if name not in ['', ' '] and len(name.split(' ')[0]) >= 2:  
      
      taxon_status = ''
      
      # check for family-group level names
      if (len(name.split(' ')) == 1 
            and name[-4:] in family_group
            or name[-3:] == 'ini'):
        
        taxon_status = 'family'
        logger.info('Provided taxon name is at family level: {}'.format(name))
        
      # fast-check for genus-level names
      elif len(name.split(' ')) == 1:
        
        taxon_status = 'genus'
        logger.info('Provided taxon name is at genus level: {}'.format(name))
        
      # fast-check for binomial names
      elif len(name.split(' ')) == 2:
        
        taxon_status = 'species'
        logger.info('Provided taxon name is at species level: {}'.format(name))
      
      # anything else will be avoided
      else:
        logger.error('Provided query is possibly a INVALID taxon: {}'.format(name))
        continue
    
      resulting_list.append((name, taxon_status))
  
  return resulting_list