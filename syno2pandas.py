import pandas as pd
import json
# import plotly.graph_objects as go
# import dash_core_components as dcc


def splitCol2Rows(dfIn, delim=',', filename='tmp.xlsx'):
    
  df2Split = dfIn.copy()
  df2Split.index.name = 'idx'
  sPlain = pd.DataFrame(
      df2Split.MatCitAccessionNumber.str.split(',').tolist(),
      index=df2Split.index).stack()
  # print('--------', sPlain)
  sPlain.rename('AccessionNumber', inplace=True)
  sPlain.index.rename(['idx', 'acc'], inplace=True)
  sPlain = sPlain.reset_index()

  # print(sPlain.index)
  # xlsxFile = filename[:-5] + 'Step1' + '.xlsx'
  # print(xlsxFile)
  # sPlain.to_excel(xlsxFile)

  dfOut = pd.merge(df2Split, sPlain,
                    how='right',
                    left_on='idx', right_on='idx')
  #xlsxFile = filename[:-5] + 'Step2' + '.xlsx'
  #print(xlsxFile)
  #dfOut.to_excel(xlsxFile)
  return dfOut


# def cleanAccessionVersioning(dfIn, accColumn='AccessionNumber'):
#   dfIn[accColumn] = dfIn[accColumn].str.replace(r'\.+\d', '')


#   # filename = 'tb-results-genus_and_species.json'
#   # with open(filename, 'r') as stream:
#   #     dJson = json.load(stream)
#   # print(dJson)
#   # dfGenSpec = pd.DataFrame.from_dict(dJson["data"])
#   # dfGenSpec.index.name = 'idx'

#   # print(dfGenSpec.columns)
#   genSpecColumns = ['DocCount', 'TaxKingdomEpithet', 'TaxPhylumEpithet',
#                     'TaxClassEpithet', 'TaxOrderEpithet', 'TaxFamilyEpithet',
#                     'TaxGenusEpithet', 'TaxSpeciesEpithet', 'MatCitCountry',
#                     'MatCitLongitude', 'MatCitLatitude', 'MatCitLongLatStatus',
#                     'MatCitYear', 'MatCitCollector', 'MatCitSpecimenCode',
#                     'MatCitAccessionNumber', 'MatCitTypeStatus']
#   print(dfGenSpec.describe())
#   for col in genSpecColumns:
#       print(col, len(dfGenSpec[col].unique()))

#   xlsxFile = filename[:-4] + 'xlsx'
#   print(xlsxFile)
#   dfGenSpec.to_excel(xlsxFile)

#   dfGenSpecPlain = splitCol2Rows(dfGenSpec)
#   cleanAccessionVersioning(dfGenSpecPlain)
#   xlsxFile = filename[:-5] +  'Plain' + '.xlsx'
#   print(xlsxFile)
#   dfGenSpecPlain.to_excel(xlsxFile)