import requests

accepted_types = ['accession_number', 'taxonomic_name']

def get_data (type_of, query_string):
  """[summary]

  Args:
      type_of ([type]): [description]
      query_string ([type]): [description]
  """

  if type_of not in accepted_types:
    print('Please, provide a valid type_of')
    return None

  try: 
    
    r = requests.get("http://tb.plazi.org/GgServer/srsStats/stats?outputFields"
                     "=doc.articleUuid+tax.classEpithet+tax.orderEpithet+"
                     "tax.familyEpithet+tax.genusEpithet+tax.speciesEpithet"
                     "+matCit.country+matCit.longLatStatus+matCit.collector"
                     "+matCit.accessionNumber+matCit.typeStatus&groupingFields"
                     "=doc.articleUuid+tax.classEpithet+tax.orderEpithet+"
                     "tax.familyEpithet+tax.genusEpithet+tax.speciesEpithet"
                     "+matCit.country+matCit.longLatStatus+matCit.collector+"
                     "matCit.accessionNumber+matCit.typeStatus"
                     "&FP-matCit.accessionNumber=%25{}%25&format=JSON"
                     .format(query_string))
    
    if r.status_code == 200:
      print("Test passed")
      print(r.json())

    else: 
      print(f"Connection problem: {r.status_code}, ")
  
  except:
    print('An exception occurred')
    
    

    
    