family_group = ['idae', 'inae']

def check_family_names(taxon_name, taxon_status):
  """test suit to check if family names are being correctly identified

  Args:
      taxon_name (str): the taxon name to be queried
      taxon_status (str): the taxonomic status of that name
  """
  
  try:
    assert(taxon_name[-4:] in family_group or taxon_name[-3:] == 'ini')
    assert(taxon_status == 'family')
    print('(o) Cool! Correctly identified as family.')
    
  except:
    print('(x) WRONG! Not a family!')


def check_genus_names(taxon_name, taxon_status):
  """test suit to check if genus names are being correctly identified

  Args:
      taxon_name (str): the taxon name to be queried
      taxon_status (str): the taxonomic status of that name
  """
  
  try:
    assert(taxon_name[-4:] not in family_group or taxon_name[-3:] != 'ini')
    assert(len(taxon_name.split(' ')) == 1)
    assert(taxon_status == 'genus')
    print('(o) Cool! Correctly identified as a genus.')

  except:
    print('(x) WRONG! Not a genus!')
    
    
def check_species_names(taxon_name, taxon_status):
  """test suit to check if species names are being correctly identified

  Args:
      taxon_name (str): the taxon name to be queried
      taxon_status (str): the taxonomic status of that name
  """
  
  try:
    assert(len(taxon_name.split(' ')) == 2)
    assert(taxon_status == 'species')
    print('(o) Cool! Correctly identified as a species.')

  except:
    print('(x) WRONG! Not a species!')