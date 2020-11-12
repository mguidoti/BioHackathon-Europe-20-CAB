import requests, logging

logger = logging.getLogger(__name__)


def get_data (taxon):
  """Query TB for a particular taxon of level family, genus or species. Returns
    response['data'] with these specific fields:
    
    DocCount,
    TaxKingdomEpithet,
    TaxPhylumEpithet,
    TaxClassEpithet,
    TaxOrderEpithet,
    TaxFamilyEpithet,
    TaxGenusEpithet,
    TaxSpeciesEpithet,
    MatCitCountry,
    MatCitLongitude,
    MatCitLatitude,
    MatCitLongLatStatus,
    MatCitYear,
    MatCitCollector,
    MatCitSpecimenCode,
    MatCitAccessionNumber,
    MatCitTypeStatus

  Args:
      taxon (tuple): Tuple containing taxon name and taxon status strings

  Returns:
      [list]: List of dicts with TB response, None when the response['data'] 
              is empty
  """
  # Decouple taxon info
  taxon_name, taxon_status = taxon
  
  try: 
    
    # Species TB API Call
    if taxon_status == 'species':

      r = requests.get("http://tb.plazi.org/GgServer/srsStats/stats"
                        "?outputFields=tax.kingdomEpithet+tax.phylumEpithet"
                        "+tax.classEpithet+tax.orderEpithet+tax.familyEpithet"
                        "+tax.genusEpithet+tax.speciesEpithet+matCit.country"
                        "+matCit.longitude+matCit.latitude+matCit.longLatStatus"
                        "+matCit.year+matCit.collector+matCit.specimenCode"
                        "+matCit.accessionNumber+matCit.typeStatus"
                        "&groupingFields=tax.kingdomEpithet+tax.phylumEpithet"
                        "+tax.classEpithet+tax.orderEpithet+tax.familyEpithet"
                        "+tax.genusEpithet+tax.speciesEpithet+matCit.country"
                        "+matCit.longitude+matCit.latitude+matCit.longLatStatus"
                        "+matCit.year+matCit.collector+matCit.specimenCode"
                        "+matCit.accessionNumber+matCit.typeStatus"
                        "&FP-tax.genusEpithet={}"
                        "&FP-tax.speciesEpithet={}&format=JSON"
                        .format(taxon_name.split(' ')[0], 
                          taxon_name.split(' ')[1]))
                                                        
    # Genus TB API Call
    elif taxon_status == 'genus':
      
      r = requests.get("http://tb.plazi.org/GgServer/srsStats/stats"
                      "?outputFields=tax.kingdomEpithet+tax.phylumEpithet"
                      "+tax.classEpithet+tax.orderEpithet+tax.familyEpithet"
                      "+tax.genusEpithet+tax.speciesEpithet+matCit.country"
                      "+matCit.longitude+matCit.latitude+matCit.longLatStatus"
                      "+matCit.year+matCit.collector+matCit.specimenCode"
                      "+matCit.accessionNumber+matCit.typeStatus"  
                      "&groupingFields=tax.kingdomEpithet+tax.phylumEpithet"
                      "+tax.classEpithet+tax.orderEpithet+tax.familyEpithet"
                      "+tax.genusEpithet+tax.speciesEpithet+matCit.country"
                      "+matCit.longitude+matCit.latitude+matCit.longLatStatus"
                      "+matCit.year+matCit.collector+matCit.specimenCode"
                      "+matCit.accessionNumber+matCit.typeStatus"
                      "&FP-tax.genusEpithet={}&format=JSON"
                      .format(taxon_name))
    
    # Family TB API Call
    elif taxon_status == 'family':
      
      r = requests.get("http://tb.plazi.org/GgServer/srsStats/stats"
                      "?outputFields=tax.kingdomEpithet+tax.phylumEpithet"
                      "+tax.classEpithet+tax.orderEpithet+tax.familyEpithet"
                      "+tax.genusEpithet+tax.speciesEpithet+matCit.country"
                      "+matCit.longitude+matCit.latitude+matCit.longLatStatus"
                      "+matCit.year+matCit.collector+matCit.specimenCode"
                      "+matCit.accessionNumber+matCit.typeStatus"
                      "&groupingFields=tax.kingdomEpithet+tax.phylumEpithet"
                      "+tax.classEpithet+tax.orderEpithet+tax.familyEpithet"
                      "+tax.genusEpithet+tax.speciesEpithet+matCit.country"
                      "+matCit.longitude+matCit.latitude+matCit.longLatStatus"
                      "+matCit.year+matCit.collector+matCit.specimenCode"
                      "+matCit.accessionNumber+matCit.typeStatus"
                      "&FP-tax.familyEpithet={}&format=JSON"
                      .format(taxon_name))
    
    else:
      logger.error("Taxon {} doesn't belong to family, "
                    "genus or species groups"
                    .format(taxon_name.upper()))
    
    
  except:
    logger.error("Couldn't request any data for taxon {}, status code: {}, {}"
                  .format(taxon_name.upper(), r.status_code, r.reason))
    return None
    
  
  if r.status_code == 200:
    logger.info("Retrieved data from Tb for {}"
                  .format(taxon_name.upper()))
    
    data = r.json()['data']
    
    if len(data) > 0: 
      return r.json()['data']
    
    else:
      logger.warn('The taxon {} has no results'
                  .format(taxon_name.upper()))
      
      return None
  
  else: 
    logger.error("Connection problem for taxon {}, status code: {}, {}"
                  .format(taxon_name.upper(), r.status_code, r.reason))
  return None

    
    

    
    