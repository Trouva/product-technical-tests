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


def classifyMe(regexString, regex_Filters, currentDS, excludeRowsWithExistingFilter=True):
	global changeTracker, classified_Total;

	print("Start classifying!");
	print(regexString);
	print(regex_Filters);

	for regex in regex_Filters:

		#only classify nulls
		if(excludeRowsWithExistingFilter):
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
        
        
        
		with open('debugFiles/' + curr_FilterStr  + '.json', 'w') as outfile:
			json.dump(data_debug, outfile, indent=4, sort_keys=True);

		# Update counts to the overall results count file
		noOfClassified = len(data_result.index)
		changeTracker.append({"matchStr": curr_MatchStr, "filterStr": curr_FilterStr, "count":noOfClassified});
		classified_Total = classified_Total + noOfClassified;
	return currentDS







#############INGEST FILE

#data = readJson('../mongo-seed/sizes.json');
with open('debugFiles/000 - data_unclassified.json', encoding = 'utf-8-sig') as json_file:
    data = json.load(json_file);
    
    
#
# Convert to DataFrame
data_original = pd.DataFrame.from_records(data);
print(len(data_original.index))
## Add an ID string
#data_original['_id_Str'] = data_original['_id'].astype(str);
#
#
##############################################################################################################
##
##							BUCKET FILTERS BY LABEL
##
#############################################################################################################
#
################### XS S M L XL XXL 
##Regex
#regexString = r'(^|-|\/|\\| |\()(MATCHSTR)($|-|\/|\\| |\)|\()';
#regex_Filters = [
#			{"matchStr": "xx - s", "filterStr": "XXS"},
#			{"matchStr": "xx s", "filterStr": "XXS"},
#			{"matchStr": "xx - small", "filterStr": "xs"},
#			{"matchStr": "xx small", "filterStr": "xs"},
#			{"matchStr": "x - s", "filterStr": "XS"},
#			{"matchStr": "x s", "filterStr": "XS"},
#			{"matchStr": "x - small", "filterStr": "XS"},
#			{"matchStr": "x small", "filterStr": "XS"},
#			{"matchStr": "extra - small", "filterStr": "XS"},
#			{"matchStr": "extra small", "filterStr": "XS"},
#			{"matchStr": "s", "filterStr": "S"}, 
#			{"matchStr": "small", "filterStr": "S"},
#			{"matchStr": "medium", "filterStr": "M"},
#			{"matchStr": "m", "filterStr": "M"},
#			{"matchStr": "xxx - l", "filterStr": "XXXL"},
#			{"matchStr": "xxx l", "filterStr": "XXXL"},
#			{"matchStr": "xx - l", "filterStr": "XXL"},
#			{"matchStr": "xx l", "filterStr": "XXL"},
#			{"matchStr": "xx - large", "filterStr": "XXL"},
#			{"matchStr": "xx large", "filterStr": "XXL"},
#			{"matchStr": "x - l", "filterStr": "XL"},
#			{"matchStr": "x l", "filterStr": "XL"},
#			{"matchStr": "x - large", "filterStr": "XL"},
#			{"matchStr": "x large", "filterStr": "XL"},
#			{"matchStr": "extra - large", "filterStr": "XL"},
#			{"matchStr": "extra large", "filterStr": "XL"},
#			{"matchStr": "large", "filterStr": "L"},
#			{"matchStr": "l", "filterStr": "L"}
#			];
#
#data_original = classifyMe(regexString, regex_Filters, data_original);
#
#
#
#
#
#
################### Babys (0 - 24 months)
##Regex
#regexString_Baby = r'(^|[^0-9])(MATCHSTR)($|[ )/])';
#
#regex_Filters_Baby = [
#			{"matchStr": "24 - 36", "filterStr": "2 - 3 Years"},
#			{"matchStr": "24 - 36", "filterStr": "2 - 3 Years"},
#			{"matchStr": "12 - 24", "filterStr": "1 - 2 Years"},
#
#			{"matchStr": "0 - 3", "filterStr": "0 - 3 Months"},
#			{"matchStr": "0 - 6", "filterStr": "0 - 6 Months"},
#			{"matchStr": "0 - 12", "filterStr": "0 - 12 Months"},
#			{"matchStr": "0 - 1", "filterStr": "0 - 3 Months"}, 
#			{"matchStr": "0 - 2", "filterStr": "0 - 3 Months"},
#
#
#			{"matchStr": "3 - 6", "filterStr": "3 - 6 Months"},
#			{"matchStr": "4 - 6", "filterStr": "3 - 6 Months"},
#			{"matchStr": "5 - 6", "filterStr": "3 - 6 Months"},
#
#			{"matchStr": "6 - 9", "filterStr": "6 - 9 Months"}, 
#			{"matchStr": "6 - 7", "filterStr": "6 - 9 Months"},
#			{"matchStr": "6 - 8", "filterStr": "6 - 9 Months"},
#
#			{"matchStr": "9 - 12", "filterStr": "9 - 12 Months"},
#			{"matchStr": "9 - 10", "filterStr": "9 - 12 Months"},
#			{"matchStr": "9 - 11", "filterStr": "9 - 12 Months"}];
#
#data_Baby = data_original[data_original['label'].str.contains("(month)|(mth)", flags=re.IGNORECASE, regex=True)];
#data_BabyResults = classifyMe(regexString_Baby, regex_Filters_Baby, data_Baby);
#data_original =  pd.concat([data_original,data_BabyResults]).drop_duplicates('_id_Str',keep='last');
#
#
##Perform remaining search and classification of months
#						#Match start of sentence, space or bracket followed by the string and then 0-1 bracket or space, followed by m
#regexString_BabyLoose = r'((^|\s|\(|\-)+(MATCHSTR)(\)|\s)*(m))';
#regex_Filters_Loose = [
#			{"matchStr": "0", "filterStr": "0 - 3 Months"},
#			{"matchStr": "1", "filterStr": "0 - 3 Months"},
#			{"matchStr": "2", "filterStr": "0 - 3 Months"},
#			{"matchStr": "3", "filterStr": "3 - 6 Months"},
#			{"matchStr": "4", "filterStr": "3 - 6 Months"},
#			{"matchStr": "5", "filterStr": "3 - 6 Months"},
#			{"matchStr": "6", "filterStr": "3 - 6 Months"},
#			{"matchStr": "6", "filterStr": "6 - 9 Months"},
#			{"matchStr": "7", "filterStr": "6 - 9 Months"},
#			{"matchStr": "8", "filterStr": "6 - 9 Months"},
#			{"matchStr": "9", "filterStr": "9 - 12 Months"},
#			{"matchStr": "10", "filterStr": "9 - 12 Months"},
#			{"matchStr": "11", "filterStr": "9 - 12 Months"},
#			{"matchStr": "12", "filterStr": "1 - 2 Years"},
#			{"matchStr": "24", "filterStr": "2 - 3 Years"},
#			{"matchStr": "36", "filterStr": "2 - 3 Years"}];
#
#data_BL = data_original[data_original['label'].str.contains("(month)|(mth)", flags=re.IGNORECASE, regex=True)];
#data_BL = data_BL.query('filter_label!=filter_label')
#data_BabyLooseResults = classifyMe(regexString_BabyLoose, regex_Filters_Loose, data_BL);
#
##throw any remaining unclassified things into 0-3 years filter
#data_Babyunclassified = data_BabyLooseResults.query('filter_label!=filter_label')
#data_Babyunclassified.filter_label = "0 - 3 Years";
#
#data_Babyunclassified = pd.concat([data_BabyLooseResults,data_Babyunclassified]).drop_duplicates('_id_Str',keep='last');
#
#
##add results to main
#data_original =  pd.concat([data_original,data_BabyLooseResults]).drop_duplicates('_id_Str',keep='last');
#
#
################### Babys (0 - 16 Years)
##Peform remaining search and classification of years
#regexString_Youth = r'(^|[^0-9])(MATCHSTR)($|[ )/])';
#regex_Filters_Youth = [
#			{"matchStr": "0 - 1", "filterStr": "0 - 3 Years"},
#			{"matchStr": "1 - 2", "filterStr": "0 - 3 Years"},
#			{"matchStr": "2 - 3", "filterStr": "0 - 3 Years"},
#
#			{"matchStr": "3 - 4", "filterStr": "4 - 6 Years"},
#			{"matchStr": "4 - 5", "filterStr": "4 - 6 Years"},
#			{"matchStr": "5 - 6", "filterStr": "4 - 6 Years"},
#
#			{"matchStr": "6 - 7", "filterStr": "7 - 9 Years"}, 
#			{"matchStr": "7 - 8", "filterStr": "7 - 9 Years"},
#			{"matchStr": "8 - 9", "filterStr": "7 - 9 Years"},
#
#			{"matchStr": "9 - 10", "filterStr": "10 - 12 Years"},
#			{"matchStr": "10 - 11", "filterStr": "10 - 12 Years"}, 
#			{"matchStr": "11 - 12", "filterStr": "10 - 12 Years"},  
#
#			{"matchStr": "12 - 13", "filterStr": "13 - 16 Years"}, 
#			{"matchStr": "13 - 14", "filterStr": "13 - 16 Years"},
#			{"matchStr": "14 - 15", "filterStr": "13 - 16 Years"},
#			{"matchStr": "15 - 16", "filterStr": "13 - 16 Years"}];
#
#
#data_Youth = data_original[data_original['label'].str.contains("(year)|(yr)", flags=re.IGNORECASE, regex=True)];
#
#
#data_YouthResults = classifyMe(regexString_Youth, regex_Filters_Youth, data_Youth);
#data_original =  pd.concat([data_original,data_YouthResults]).drop_duplicates('_id_Str',keep='last');
#
#
#
#regexString_YouthLoose = r'((^|\s|\(|\-)+(MATCHSTR)(\)|\s)*(y))';
#regex_Filters_YouthLoose = [
#			{"matchStr": "10", "filterStr": "10 - 12 Years"},
#			{"matchStr": "11", "filterStr": "10 - 12 Years"}, 
#			{"matchStr": "12", "filterStr": "10 - 12 Years"},  
#
#			{"matchStr": "13", "filterStr": "13 - 16 Years"}, 
#			{"matchStr": "14", "filterStr": "13 - 16 Years"},
#			{"matchStr": "15", "filterStr": "13 - 16 Years"},
#			{"matchStr": "16", "filterStr": "13 - 16 Years"},
#			{"matchStr": "0", "filterStr": "0 - 3 Years"},
#			{"matchStr": "1", "filterStr": "0 - 3 Years"},
#			{"matchStr": "2", "filterStr": "0 - 3 Years"},
#			{"matchStr": "3", "filterStr": "0 - 3 Years"},
#
#			{"matchStr": "4", "filterStr": "4 - 6 Years"},
#			{"matchStr": "5", "filterStr": "4 - 6 Years"},
#			{"matchStr": "6", "filterStr": "4 - 6 Years"},
#
#			{"matchStr": "7", "filterStr": "7 - 9 Years"}, 
#			{"matchStr": "8", "filterStr": "7 - 9 Years"},
#			{"matchStr": "9", "filterStr": "7 - 9 Years"},
#
#			];
#
#data_YL = data_original[data_original['label'].str.contains("((year)|(yr))", flags=re.IGNORECASE, regex=True)];
#data_YL = data_BL.query('filter_label!=filter_label')
#data_YouthLooseResults = classifyMe(regexString_YouthLoose, regex_Filters_YouthLoose, data_YL);
#data_original =  pd.concat([data_original,data_YouthLooseResults]).drop_duplicates('_id_Str',keep='last');
#
#
#
########################## UK SIZE
#regexString = r'(^|-|\/|\\| |\()(MATCHSTR)($|-|\/|\\| |\)|\()';
#regex_Filters = [
#			{"matchStr": "1", "filterStr": "UK1"},
#			{"matchStr": "xx s", "filterStr": "UK2"},
#			{"matchStr": "xx - small", "filterStr": "UK3"},
#			{"matchStr": "xx small", "filterStr": "UK4"},
#			{"matchStr": "x - s", "filterStr": "UK5"},
#			{"matchStr": "x s", "filterStr": "UK6"},
#			{"matchStr": "x - small", "filterStr": "UK7"},
#			{"matchStr": "x small", "filterStr": "UK8"},
#			{"matchStr": "extra - small", "filterStr": "UK9"},
#			{"matchStr": "extra small", "filterStr": "UK10"},
#			{"matchStr": "s", "filterStr": "UK11"}, 
#			{"matchStr": "small", "filterStr": "UK12"},
#			{"matchStr": "medium", "filterStr": "UK13"},
#			{"matchStr": "m", "filterStr": "UK14"},
#			{"matchStr": "xxx - l", "filterStr": "UK15"},
#			{"matchStr": "xxx l", "filterStr": "U"},
#			{"matchStr": "xx - l", "filterStr": "XXL"},
#			{"matchStr": "xx l", "filterStr": "XXL"},
#			{"matchStr": "xx - large", "filterStr": "XXL"},
#			{"matchStr": "xx large", "filterStr": "XXL"},
#			{"matchStr": "x - l", "filterStr": "XL"},
#			{"matchStr": "x l", "filterStr": "XL"},
#			{"matchStr": "x - large", "filterStr": "XL"},
#			{"matchStr": "x large", "filterStr": "XL"},
#			{"matchStr": "extra - large", "filterStr": "XL"},
#			{"matchStr": "extra large", "filterStr": "XL"},
#			{"matchStr": "large", "filterStr": "L"},
#			{"matchStr": "l", "filterStr": "L"}
#			];
#
#data_original = classifyMe(regexString, regex_Filters, data_original);
#
#
#
#
#
#
#
#
#
########## OUTPUT TO FILE
#
#
## Convert from DF to json
#data_original.drop(columns=['_id_Str']);
#data_JSONoutput = json.loads(data_original.to_json(orient='records'));
#
#
## Save to file
#with open('data_cleanse.json', 'w') as outfile:
#    json.dump(data_JSONoutput, outfile, indent=4, sort_keys=True);
#
#
######## DEBUGGING
#
## Save unclassified to file
#data_unclassified = data_original.query('filter_label!=filter_label');
#data_JSONunclassified = json.loads(data_unclassified.to_json(orient='records'));
#with open('debugFiles/' + '000 - data_unclassified.json', 'w') as outfile:
#    json.dump(data_JSONunclassified, outfile, indent=4, sort_keys=True);
#
## Append remaining data to results count file
#changeTracker.append({"matchStr": 'unclassified', "filterStr": 'na', "count":len(data_unclassified)});
#changeTracker.append({"matchStr": 'total classified', "filterStr": 'na', "count":classified_Total });
#
## print results to file
#print(changeTracker);
#with open('debugFiles/' + 'ResultCounts.json', 'w') as outfile:
#    json.dump(changeTracker, outfile, indent=4, sort_keys=True);


