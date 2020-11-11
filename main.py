from source import connect_tb as tb
import pandas as pd 

if __name__ == "__main__":
  # execute only if run as a script
  tb.get_data('accession_number', 'JQ929234')
  
  
# taxon -> to query tb
# return df based on accesion numbers

# 80 000
# 1 call, get all accession numbers in the system

# if 1 word .split(' ')
# if ends on -idae, -inae or -ini -> Family field (Rhinolophidae)
# else if 2 words .split(' '), query genus and species (Rhinolophus mossambicus)
# else if 1 word and first letter capitilized -> genus (Rhinolophus, Tingis)

# 1 parameter, taxon name
# return df

# 'Binomial' -> Node

# ---

# links to ocellus, tb search, gbif, synospecies

# for the sake of data analyses
# create a timestamp based column on the returning df
# create a query string column, and a taxon status column, on the returning df

# how many entries were there? || how many data is in tb
# how many of these with accession numbers? || how many accession numbers were available in the taxonomy literature
# did it change over time? || measure progress of tb, maybe progress of specific tasks 