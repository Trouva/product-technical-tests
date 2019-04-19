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

def joinData(currentData, originalData):
	return pd.concat([originalData,currentData]).drop_duplicates('_id_Str',keep='last');

def debugPrint(currentData, fileName):
	####### DEBUGGING

	# Write all matches to a filter file to analyse
	print("Write " + fileName + " filter to file");
	data_debug = json.loads(currentData.to_json(orient='records'));

	with open('debugFiles/'+fileName+'.json', 'w') as outfile:
		json.dump(data_debug, outfile, indent=4, sort_keys=True);

	# Update counts to the overall results count file
	noOfClassified = len(currentData)
	print("Classified: " + str(noOfClassified));


def getSubGroup(currentData, currentRegex):

	returnData = currentData.query('filter_label!=filter_label')
	returnData = returnData[returnData['label'].str.contains(currentRegex, flags=re.IGNORECASE, regex=True)];
	returnData['filter_label'] = returnData['label'].str.extract(currentRegex, expand=True, flags=re.IGNORECASE)[0].str.replace(' ', '')
	return returnData;



####Initial readin of file
data = readJson('../mongo-seed/sizes.json');

# Convert to DataFrame
data_original = pd.DataFrame.from_records(data);
# Add an ID string
data_original['_id_Str'] = data_original['_id'].astype(str);




#############################################################################################################
#
#							ASSIGNING FILTERS AUTOMATICALLY
#
############################################################################################################


#=====================MATCH UK/EU to FILTER

######MATCH ANYTHING OF THESE PATTERNS:
######			EU40
######			EU 40
######			UK40
######			UK 40
currentRegex = r"(((UK)|(EU))( )*[0-9]{1,2}((\.)[0-9])?)";
data_EUUK = getSubGroup(data_original, currentRegex)



data_original = joinData(data_EUUK, data_original);
debugPrint(data_EUUK, 'data_EUUK');


######MATCH ANYTHING OF THESE PATTERNS:
######			45EU
######			45 EU
######			45UK
######			45 UK
currentRegex = r"([0-9]{1,2}((\.)[0-9])?( )*((UK)|(EU)))";
data_EUUKV2 = getSubGroup(data_original, currentRegex)

#Formatting step
data_EUUKV2['filter_label'] = data_EUUKV2['filter_label'].str[-2:] + data_EUUK['filter_label'].str[:-2];

#Add back to main results
data_original = joinData(data_EUUKV2, data_original);
debugPrint(data_EUUKV2, 'data_EUUK_2');



#================MATCH BABY THINGS

#######MATCH Youth and baby
currentRegex = r'([0-9]{1,2}(\s)*(\-|(to))(\s)*[0-9]{1,2}(\s)*((years)|yrs|(year)|(yr)|(months)|(mths)|(mth)|(month)))';
data_Youth = getSubGroup(data_original, currentRegex)

#Formatting Step

regex_baby = re.compile(r'yrs', flags=re.IGNORECASE)
data_Youth['filter_label']=data_Youth['filter_label'].str.replace(regex_baby, 'Years')

regex_baby = re.compile(r'years', flags=re.IGNORECASE)
data_Youth['filter_label']=data_Youth['filter_label'].str.replace(regex_baby, 'Years')

regex_baby = re.compile(r'yr', flags=re.IGNORECASE)
data_Youth['filter_label']=data_Youth['filter_label'].str.replace(regex_baby, 'Year')

regex_baby = re.compile(r'year', flags=re.IGNORECASE)
data_Youth['filter_label']=data_Youth['filter_label'].str.replace(regex_baby, 'Year')

regex_baby = re.compile(r'to', flags=re.IGNORECASE)
data_Youth['filter_label']=data_Youth['filter_label'].str.replace(regex_baby, '-')


regex_baby = re.compile(r'month', flags=re.IGNORECASE)
data_Youth['filter_label']=data_Youth['filter_label'].str.replace(regex_baby, 'Month')

regex_baby = re.compile(r'months', flags=re.IGNORECASE)
data_Youth['filter_label']=data_Youth['filter_label'].str.replace(regex_baby, 'Months')

regex_baby = re.compile(r'mths', flags=re.IGNORECASE)
data_Youth['filter_label']=data_Youth['filter_label'].str.replace(regex_baby, 'Months')

regex_baby = re.compile(r'mth', flags=re.IGNORECASE)
data_Youth['filter_label']=data_Youth['filter_label'].str.replace(regex_baby, 'Month')

#Add back to main results
data_original = joinData(data_Youth, data_original);
debugPrint(data_Youth, 'data_Youth');


#######MATCH newborn
currentRegex = r"(new)( )?(born)";
data_NewBorn = getSubGroup(data_original, currentRegex)

#Formatting Step
regex_baby = re.compile(r'newborn', flags=re.IGNORECASE)
data_NewBorn['filter_label']=data_NewBorn['filter_label'].str.replace(regex_baby, 'Newborn')


#Add back to main results
data_original = joinData(data_NewBorn, data_original);
debugPrint(data_NewBorn, 'data_NewBorn');





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
with open('debugFiles/' + '000 - data_unclassified.json', 'w') as outfile:
    json.dump(data_JSONunclassified, outfile, indent=4, sort_keys=True);

# Append remaining data to results count file
changeTracker.append({"matchStr": 'unclassified', "filterStr": 'na', "count":len(data_unclassified)});
changeTracker.append({"matchStr": 'total classified', "filterStr": 'na', "count":classified_Total });

# print results to file
print(changeTracker);
with open('debugFiles/' + 'ResultCounts.json', 'w') as outfile:
    json.dump(changeTracker, outfile, indent=4, sort_keys=True);


