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
data_original = pd.DataFrame.from_records(data);
# Add an ID string
data_original['_id_Str'] = data_original['_id'].astype(str);


#==========MATCH TO FILTER

#Debugging tracking things
changeTracker = [];
classified_Total = 0;

#Regex
regexString = r'(^(MATCHSTR)$)|(^(MATCHSTR)[-\/\\ ])|([-\/\\ ](MATCHSTR)[-\/\\ ])|([-\/\\ ](MATCHSTR)$)|([-\/\\ ](MATCHSTR)[-\/\\ ])';
regex_Filters = [
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

data_current = data_original

for regex in regex_Filters:
	#Get all rows where there is no filters already assigned
	data_noFilter = data_current.query('filter_label!=filter_label')

	#Get current string + filter
	curr_MatchStr = regex.get("matchStr","");
	curr_FilterStr = regex.get("filterStr","");


	# Filter based off regex 
	currentRegex = regexString.replace("MATCHSTR", curr_MatchStr);
	data_result = data_noFilter[data_noFilter['label'].str.contains(currentRegex, flags=re.IGNORECASE, regex=True)];

	# Assign all rows that fit the regex to the filter
	data_result.filter_label = curr_FilterStr;

	# Append data_result (with new filters) to current data, and drop duplicates via ID
	data_current = pd.concat([data_current,data_result]).drop_duplicates('_id_Str',keep='last');


	####### DEBUGGING

	# Write all matches to a filter file to analyse
	print("Write " + curr_MatchStr + " filter to file");
	data_debug = json.loads(data_result.to_json(orient='records'));

	with open('debugFiles/' + curr_MatchStr+'.json', 'w') as outfile:
		json.dump(data_debug, outfile, indent=4, sort_keys=True);

	# Update counts to the overall results count file
	noOfClassified = len(data_result)
	changeTracker.append({"matchStr": curr_MatchStr, "filterStr": curr_FilterStr, "count":noOfClassified});
	classified_Total = classified_Total + noOfClassified;

	####### END DEBUGGING



######### OUTPUT TO FILE


# Convert from DF to json
data_current.drop(columns=['_id_Str']);
data_JSONoutput = json.loads(data_current.to_json(orient='records'));


# Save to file
with open('data_cleanse.json', 'w') as outfile:
    json.dump(data_JSONoutput, outfile, indent=4, sort_keys=True);


####### DEBUGGING

# Save unclassified to file
data_unclassified = data_current.query('filter_label!=filter_label');
data_JSONunclassified = json.loads(data_unclassified.to_json(orient='records'));
with open('debugFiles/' + 'data_unclassified.json', 'w') as outfile:
    json.dump(data_JSONunclassified, outfile, indent=4, sort_keys=True);

# Append remaining data to results count file
changeTracker.append({"matchStr": 'unclassified', "filterStr": 'na', "count":len(data_unclassified)});
changeTracker.append({"matchStr": 'total classified', "filterStr": 'na', "count":classified_Total });

# print results to file
print(changeTracker);
with open('debugFiles/' + 'ResultCounts.json', 'w') as outfile:
    json.dump(changeTracker, outfile, indent=4, sort_keys=True);


