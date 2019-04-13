import numpy as np
import pandas as pd
import json
import re

with open('jsonformatter.json', encoding = 'utf-8-sig') as json_file:
    data = json.load(json_file);

data_DF = pd.DataFrame.from_records(data)
data_DF['_id_Str'] = data_DF['_id'].astype(str)



data_NoFilterLabel = data_DF.query('filter_label!=filter_label')
regex_S = r'(^S{1}$)|(^S{1}\s{1})|(^small)|(\ssmall)'
data_S = data_NoFilterLabel[data_NoFilterLabel['label'].str.contains(regex_S, flags=re.IGNORECASE, regex=True)]
data_S.filter_label = 'S'


data_test = pd.concat([data_NoFilterLabel,data_S]).drop_duplicates('_id_Str',keep='last')
data_test.drop(columns=['_id_Str'])

data_json = json.loads(data_test.to_json(orient='records'))

print(type(data_json))
with open('data_clease.json', 'w') as outfile:
    json.dump(data_json, outfile, indent=4, sort_keys=True)