import numpy as np
import pandas as pd
import json
import re

def readJson(filename):
	# Get json
	data = [];
	with open(filename) as f:
	    content = f.readlines();
	for x in content:
		data.append(json.loads(x));
	return data;




data = readJson('../mongo-seed/sizes.json');

# Convert to DataFrame
data_DF = pd.DataFrame.from_records(data);
data_DF['_id_Str'] = data_DF['_id'].astype(str);



regexString = r'(^(MATCHSTR)$)|(^(MATCHSTR)[-\/\\h])|([-\/\\h](MATCHSTR)[-\/\\h])|([-\/\\h](MATCHSTR)$)|([-\/\\h](MATCHSTR)[-\/\\h])';
regexArr = [
			{"matchStr": "xxs", "filterStr": "XXS"},
			{"matchStr": "xxsmall", "filterStr": "xs"},
			{"matchStr": "xs", "filterStr": "XS"},
			{"matchStr": "xsmall", "filterStr": "XS"},
			{"matchStr": "s", "filterStr": "S"}, 
			{"matchStr": "small", "filterStr": "S"},
			{"matchStr": "medium", "filterStr": "M"},
			{"matchStr": "m", "filterStr": "M"},
			{"matchStr": "xxl", "filterStr": "XXL"},
			{"matchStr": "xxlarge", "filterStr": "XXL"},
			{"matchStr": "xl", "filterStr": "XL"},
			{"matchStr": "xlarge", "filterStr": "XL"},
			{"matchStr": "large", "filterStr": "L"},
			{"matchStr": "l", "filterStr": "L"}
			];

changeTracker = [];
classified_Count = 0;
for regex in regexArr:
	data_NoFilterLabel = data_DF.query('filter_label!=filter_label')

	curr_MatchStr = regex.get("matchStr","");
	curr_FilterStr = regex.get("filterStr","");


	# Filter based off regex 
	currentRegex = regexString.replace("MATCHSTR", curr_MatchStr);
	data_result = data_NoFilterLabel[data_NoFilterLabel['label'].str.contains(currentRegex, flags=re.IGNORECASE, regex=True)];

	# Set filter to a string
	data_result.filter_label = curr_FilterStr;

	#Output Filter files
	print("Write " + curr_MatchStr + " filter to file");
	data_json = json.loads(data_result.to_json(orient='records'));

	with open('debugFiles/' + curr_MatchStr+'.json', 'w') as outfile:
		json.dump(data_json, outfile, indent=4, sort_keys=True);


	# Track rows changed
	noOfClassified = len(data_result)
	changeTracker.append({"matchStr": curr_MatchStr, "filterStr": curr_FilterStr, "count":noOfClassified});
	classified_Count = classified_Count + noOfClassified;

	# Update the whole schema
	data_DF = pd.concat([data_DF,data_result]).drop_duplicates('_id_Str',keep='last');



	


# Convert from DF to json
data_DF.drop(columns=['_id_Str']);
data_json = json.loads(data_DF.to_json(orient='records'));



# Save to file
with open('data_cleanse.json', 'w') as outfile:
    json.dump(data_json, outfile, indent=4, sort_keys=True);


# Save unclassified to file
data_unclassified = data_DF.query('filter_label!=filter_label');
data_json = json.loads(data_DF.to_json(orient='records'));
with open('debugFiles/' + 'data_unclassified.json', 'w') as outfile:
    json.dump(data_json, outfile, indent=4, sort_keys=True);


changeTracker.append({"matchStr": 'unclassified', "filterStr": 'na', "count":len(data_unclassified)});
changeTracker.append({"matchStr": 'total classified', "filterStr": 'na', "count":classified_Count });

# print results to file
print(changeTracker);
with open('debugFiles/' + 'results.json', 'w') as outfile:
    json.dump(data_json, outfile, indent=4, sort_keys=True);


