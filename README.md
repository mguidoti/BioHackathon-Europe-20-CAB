# BioHackathon-Europe #20 CAB - Task 3
> 9-13 November 2020, Virtual

This contains a series of scripts that queries Plazi's TreatmentBank based on a
provided list of taxa, in order to return information on materials citations.

This was Marcus Guidoti (@mguidoti) and Dario Pescini (@pescini) contribution to
project #20, "**_Computer Aided Biodiversity_**", led by Anna Sandionigi.

## how to run

You'll need [python](https://www.python.org/downloads/) and [pipenv](https://pypi.org/project/pipenv/).

- First, run `pipenv install`
- Then, run `pipenv run main` and voilá, you should be all set.

If you want to change the original list of taxa, change the content of the list
`original_taxon_list` on `./main.py`, and run `pipenv run main` again.


## file structure
```
|--source/
  |--combine_tb.py          Combine tb results into a pandas.DataFrame with additional info
  |--connect_tb.py          API calls to TB, returns list of dicts as results
  |--external_services.py   Not implemented yet
  |--name_classifier.py     Classifies taxa names into family, genus or species levels
|--tests/
  |--acc_number.py          Not implemented yet
  |--taxon_name.py          Tests name_classifier.py
|--.gitignore
|--LICENSE
|--Pipfile
|--README.md
|--**data.pkl**             All matCits of Rhinolophus in the system was saved here
|--main.py                  Call the other functions
|--syno2pandas.py           Split and rename AccessionNumber column
|--test.py                  Run test suites
```

## others
We tried to follow [Udacity's Git Commit Message Style Guide](https://udacity.github.io/git-styleguide/).

If you have any questions or wants to contribute, please do. No specific rules to write issues or PRs.


## license
[MIT](https://github.com/mguidoti/BioHackathon-Europe-20-CAB/blob/main/LICENSE).
