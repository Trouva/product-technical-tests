import numpy as np
import pandas as pd
import json
import re

#Debugging tracking things
changeTracker = [];
classified_Total = 0;

def readJson(filename):
	# Get json
	data = [];
	with open(filename) as f:
	    content = f.readlines();
	for x in content:
		data.append(json.loads(x));
	return data;


def classifyMe(regexString, regex_Filters, currentDS):
	global changeTracker, classified_Total;

	print("Start classifying!");
	print(regexString);
	print(regex_Filters);

	for regex in regex_Filters:

		#only classify nulls
		data_current = currentDS.query('filter_label!=filter_label')

		#Get current string + filter
		curr_MatchStr = regex.get("matchStr","");
		curr_FilterStr = regex.get("filterStr","");


		# Replace all spaces with ( ?) (regex meaning 0 to 1 space)
		curr_MatchStr = curr_MatchStr.replace(" ", "( ?)");
		# Replace all dashes with (-|(to)) (regex meaning - or to)
		curr_MatchStr = curr_MatchStr.replace("-", "(-|(to))");

		currentRegex = regexString.replace("MATCHSTR", curr_MatchStr);

		# Filter based off regex
		data_result = data_current[data_current['label'].str.contains(currentRegex, flags=re.IGNORECASE, regex=True)];

		# Assign all rows that fit the regex to the filter
		data_result.filter_label = curr_FilterStr;

		# Append data_result (with new filters) to current data, and drop duplicates via ID
		currentDS = pd.concat([currentDS,data_result]).drop_duplicates('_id_Str',keep='last');


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
	return currentDS








data = readJson('../mongo-seed/sizes.json');

# Convert to DataFrame
data_original = pd.DataFrame.from_records(data);
# Add an ID string
data_original['_id_Str'] = data_original['_id'].astype(str);


#=====================MATCH TO FILTER





################## XS S M L XL XXL 
#Regex
regexString = r'(^|-|\/|\\| |\()(MATCHSTR)($|-|\/|\\| |\)|\()';
regex_Filters = [
			{"matchStr": "xx - s", "filterStr": "XXS"},
			{"matchStr": "xx s", "filterStr": "XXS"},
			{"matchStr": "xx - small", "filterStr": "xs"},
			{"matchStr": "xx small", "filterStr": "xs"},
			{"matchStr": "x - s", "filterStr": "XS"},
			{"matchStr": "x s", "filterStr": "XS"},
			{"matchStr": "x - small", "filterStr": "XS"},
			{"matchStr": "x small", "filterStr": "XS"},
			{"matchStr": "extra - small", "filterStr": "XS"},
			{"matchStr": "extra small", "filterStr": "XS"},
			{"matchStr": "s", "filterStr": "S"}, 
			{"matchStr": "small", "filterStr": "S"},
			{"matchStr": "medium", "filterStr": "M"},
			{"matchStr": "m", "filterStr": "M"},
			{"matchStr": "xxx - l", "filterStr": "XXXL"},
			{"matchStr": "xxx l", "filterStr": "XXXL"},
			{"matchStr": "xx - l", "filterStr": "XXL"},
			{"matchStr": "xx l", "filterStr": "XXL"},
			{"matchStr": "xx - large", "filterStr": "XXL"},
			{"matchStr": "xx large", "filterStr": "XXL"},
			{"matchStr": "x - l", "filterStr": "XL"},
			{"matchStr": "x l", "filterStr": "XL"},
			{"matchStr": "x - large", "filterStr": "XL"},
			{"matchStr": "x large", "filterStr": "XL"},
			{"matchStr": "extra - large", "filterStr": "XL"},
			{"matchStr": "extra large", "filterStr": "XL"},
			{"matchStr": "large", "filterStr": "L"},
			{"matchStr": "l", "filterStr": "L"}
			];

data_original = classifyMe(regexString, regex_Filters, data_original);





################## Babys (0 - 24 months)
#Regex
regexString_Baby = r'(^|[^0-9])(MATCHSTR)($|[ )/])';

regex_Filters_Baby = [
			{"matchStr": "24 - 36", "filterStr": "2 - 3 Years"},
			{"matchStr": "24 - 36", "filterStr": "2 - 3 Years"},
			{"matchStr": "12 - 24", "filterStr": "1 - 2 Years"},

			{"matchStr": "0 - 3", "filterStr": "0 - 3 Months"},
			{"matchStr": "0 - 6", "filterStr": "0 - 6 Months"},
			{"matchStr": "0 - 12", "filterStr": "0 - 12 Months"},
			{"matchStr": "0 - 1", "filterStr": "0 - 3 Months"}, 
			{"matchStr": "0 - 2", "filterStr": "0 - 3 Months"},


			{"matchStr": "3 - 6", "filterStr": "3 - 6 Months"},
			{"matchStr": "4 - 6", "filterStr": "3 - 6 Months"},
			{"matchStr": "5 - 6", "filterStr": "3 - 6 Months"},

			{"matchStr": "6 - 9", "filterStr": "6 - 9 Months"}, 
			{"matchStr": "6 - 7", "filterStr": "6 - 9 Months"},
			{"matchStr": "6 - 8", "filterStr": "6 - 9 Months"},

			{"matchStr": "9 - 12", "filterStr": "9 - 12 Months"},
			{"matchStr": "9 - 10", "filterStr": "9 - 12 Months"},
			{"matchStr": "9 - 11", "filterStr": "9 - 12 Months"}];

data_Baby = data_original[data_original['label'].str.contains("(month)|(mth)", flags=re.IGNORECASE, regex=True)];
data_BabyResults = classifyMe(regexString_Baby, regex_Filters_Baby, data_Baby);
data_original =  pd.concat([data_original,data_BabyResults]).drop_duplicates('_id_Str',keep='last');


#Perform remaining search and classification of months
						#Match start of sentence, space or bracket followed by the string and then 0-1 bracket or space, followed by m
regexString_BabyLoose = r'((^| |\()(MATCHSTR)(\)| )?(m))';
regex_Filters_Loose = [
			{"matchStr": "0", "filterStr": "0 - 3 Months"},
			{"matchStr": "1", "filterStr": "0 - 3 Months"},
			{"matchStr": "2", "filterStr": "0 - 3 Months"},
			{"matchStr": "3", "filterStr": "3 - 6 Months"},
			{"matchStr": "4", "filterStr": "3 - 6 Months"},
			{"matchStr": "5", "filterStr": "3 - 6 Months"},
			{"matchStr": "6", "filterStr": "3 - 6 Months"},
			{"matchStr": "6", "filterStr": "6 - 9 Months"},
			{"matchStr": "7", "filterStr": "6 - 9 Months"},
			{"matchStr": "8", "filterStr": "6 - 9 Months"},
			{"matchStr": "9", "filterStr": "9 - 12 Months"},
			{"matchStr": "10", "filterStr": "9 - 12 Months"},
			{"matchStr": "11", "filterStr": "9 - 12 Months"},
			{"matchStr": "12", "filterStr": "1 - 2 Years"},
			{"matchStr": "24", "filterStr": "2 - 3 Years"},
			{"matchStr": "36", "filterStr": "2 - 3 Years"}];

data_BL = data_original[data_original['label'].str.contains("(month)|(mth)", flags=re.IGNORECASE, regex=True)];
data_BL = data_BL.query('filter_label!=filter_label')
data_BabyLooseResults = classifyMe(regexString_BabyLoose, regex_Filters_Loose, data_BL);
data_original =  pd.concat([data_original,data_BabyLooseResults]).drop_duplicates('_id_Str',keep='last');







######### OUTPUT TO FILE


# Convert from DF to json
data_original.drop(columns=['_id_Str']);
data_JSONoutput = json.loads(data_original.to_json(orient='records'));


# Save to file
with open('data_cleanse.json', 'w') as outfile:
    json.dump(data_JSONoutput, outfile, indent=4, sort_keys=True);


####### DEBUGGING

# Save unclassified to file
data_unclassified = data_original.query('filter_label!=filter_label');
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


