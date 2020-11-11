from source import name_classifier
from tests import taxon_name as tester

import logging

logging.basicConfig(
  filename='test.log',
  level=logging.INFO,
  format='%(levelname)s:%(asctime)s:%(name)s:%(message)s',
  datefmt='%Y-%m-%d %H:%M:%S'
  )

# Data entry
list_of_names = ['Tingini', 'Tingis americana', 'Tingis', 'Tingis ipsi dipsi', ' ', '', ' ', 'Sphaerocysta', 'A asd']

### TESTING NAME CLASSIFIER ###

resulting_names = name_classifier.classify(list_of_names)

print(resulting_names)

for each in resulting_names:
  taxon_name, taxon_status = each
  print('===============================')
  print('Testing for {}, with {} status'.format(taxon_name.upper(), taxon_status.upper()))
  print('-------------------------------')
  tester.check_family_names(taxon_name, taxon_status)
  tester.check_genus_names(taxon_name, taxon_status)
  tester.check_species_names(taxon_name, taxon_status)
  print('===============================\n')

