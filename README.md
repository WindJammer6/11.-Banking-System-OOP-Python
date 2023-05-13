# 11.-Banking-System-OOP-Python :bank::desktop_computer:
A personal project to analyse data from a Employee Exit survey from the Department of Education, Training and Employment (DETE) and the 
Technical and Further Education (TAFE) institute in Queensland, Australia. Python Libraries used: Numpy, Pandas, Matplotlib

## Thoughts on starting this project
My eighth programming project, in Python. 

After my previous programming project on data analysis (8. Star-Wars-Data-Analysis-Python), I wanted to further familiarise myself on the data analysis aspect of
Python programming and its commonly used Python libraries. I spent significantly less time on analysing this dataset and was able to complete more complex tasks such as combining the DETE and TAFE datasets after cleaning them to create a new dataset to use for further data analysis, with more resources to refer on from both the
7.-NumPy-Pandas-Matplotlib-Learning-and-Practice-Python and 8. Star-Wars-Data-Analysis-Python and that I have more tools under my belt for data analysis. (more knowledge of different functions)

<br>

For this Employee Exit Data Analysis Project, we will answer in the guided aspect: **'Are employees who only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been there longer?'** and
**'Are younger employees resigning due to some kind of dissatisfaction? What about older employees?'**. For the non-guided aspect, we will answer **'How many people in each age group resgined due to some kind of dissatisfaction?'**

<br>

Computer program used for coding: VS Code

## Repository directory description:
Let's start with:
1. Sources and Context
2. Cleaning and Preparing Data
3. Data Modelling and Analysis
4. Analysing Other Aspects of the Dataset

<br>

<br>

**1. Sources and Context**

The Dataquest website provides some guidance and provides the tasks in order to analyse some of the data in the dataset. The 'Employeeexit_data_analysis_project' folder is organised to tasks from the website. '1.Task1.py' to '9.Task9.py' is on Cleaning and Preparing the data while '10.Task10.py' is on Data Modelling and Analysis. '11.Task11.py' is to analyse another aspect of data from the dataset.

I have transferred the tasks from the website as instructions into my respective code files.

Took reference from another sample attempt on the guided question in the Dataquest guide community discussion. Some of my code (labelled in comment 'Copied from online') are from this sample. (in source(s))

Source(s): https://app.dataquest.io/c/60/m/348/guided-project%3A-clean-and-analyze-employee-exit-surveys/1/introduction (Dataquest (main project guide)), https://community.dataquest.io/t/guided-project-clean-and-analyze-employee-exit-surveys-by-feelingcxld/568982 (Dataquest sample attempt from the community discussion page)

Datasets analysed [here](https://github.com/plasmagirl/Clean-And-Analyze-Employee-Exit-Surveys/blob/master/dete_survey.csv) (DETE Survey) and [here](https://github.com/plasmagirl/Clean-And-Analyze-Employee-Exit-Surveys/blob/master/tafe_survey.csv) (TAFE Survey)

<br>

<br>

**2.Cleaning and Preparing Data**

_Task 1_
```python
import pandas as pd

dete_survey = pd.read_csv('dete_survey.csv')
tafe_survey = pd.read_csv('tafe_survey.csv')
```
Not much for Task 1, just to load the dataset into the file.(more explanation of the code in comments in the code)

```python
#'.info()' print a concise summary of a DataFrame.
#This method prints information about a DataFrame including the index dtype and columns, 
#non-null values and memory usage.
print(dete_survey.info())
print(dete_survey.head(5))
print(tafe_survey.info())
print(tafe_survey.head(5))
```
To print out the dete_survey and tafe_survey datasets out for checking. Used the '.head(5)' function to only print out the top 5 rows to not flood the output.

'.info()' prints out a concise summary of a DataFrame containing the different names of the column titles, number of non-null values per column, and the data type each column is holding.

<br>

_Task 2_
```python
import pandas as pd

#The 'read_csv()' function actually accepts a lot of different parameters (see documentation), one
#of whuich is 'na_values='
dete_survey = pd.read_csv('dete_survey.csv', na_values='Not Stated')
tafe_survey = pd.read_csv('tafe_survey.csv')

#To check if 'Not Stated' inputs are now NAN
print(dete_survey)
```
For Task 2, the task is to clean the datasets and removing any excess columns that we will not need in this data analysis project. 'na_values='Not Stated'' is to recognise any strings in the dete_survey dataset that has 'Not Stated' as NaN. 

```python
#Dropping columns of index 28 to 49 from the dete_survey dataset
dete_survey_updated = dete_survey.drop(dete_survey.iloc[:, 28:49], axis=1)
print(dete_survey_updated)

#Dropping columns of index 17 to 66 from the dete_survey dataset
tafe_survey_updated = tafe_survey.drop(tafe_survey.iloc[:, 17:66], axis=1)
print(tafe_survey_updated)
```
These lines of code is to remove the indexed columns in the dataset. The indexing for the columns to be removed is provided in the Dataquest guide for this project.

```python
#'index=False' to prevent creating a new column of new indexes in the new csv file
dete_survey_updated.to_csv('dete_survey2.csv', index=False)
tafe_survey_updated.to_csv('tafe_survey2.csv', index=False)
```
Loaded edited dataset into a new file so I can load it into the next code file. And so I can view the dataset as a whole as VS Code dosen't allow me to see the full thing in its terminal. 

As stated in the comment in the code, to prevent new indexes from being added into the dataset everytime a new copy of the dataset is made, in this task and all the other tasks I included the 'index=False' parameter in the '.to_csv()' function.

<br>

_Task 3_
```python
import pandas as pd

dete_survey_updated = pd.read_csv('dete_survey2.csv')
tafe_survey_updated = pd.read_csv('tafe_survey2.csv')

#Taking out the headers as an array in the dete_survey dataset, and changing all the headers to lowercase
dete_columns = list(dete_survey_updated.columns)
dete_columns_lower = []
for element in dete_columns:
    dete_columns_lower.append(element.lower())

#Changing all the headers' spaces into underscore
dete_columns_lower_underscore = []
for element in dete_columns_lower:
    dete_columns_lower_underscore.append(element.replace(' ', '_')) 

#Removing any spaces at the front and end of the headers
dete_columns_lower_underscore_stripped = []
for element in dete_columns_lower_underscore:
    dete_columns_lower_underscore_stripped.append(element.strip())

```
For task 3, the task is to rename the column titles to something more understandable and standardised.

For the dete_survey dataset:

I made a new list storing all the column titles and working on this new list seperately from the main dataset. I will then later piece the updated column names back into the dataset. 

For renaming of the column titles in the new list, I first changed all the column titles to lowercase (in first for loop), then replacing any spaces into underscore (in second for loop) and lastly removing any spaces at the front and end (in third for loop).

```python
#(Copied from online) To add the edited headers array into the dete_survey_updated dataset as top row 
#(below headers)

#Adding a row assigning it with index of -1 and will appear at the bottom of the dataset
dete_survey_updated.loc[-1] = dete_columns_lower_underscore_stripped
#Shifting index causing the newly assigned row to be now of index 0
dete_survey_updated.index = dete_survey_updated.index + 1
#Re-sorting by index so the new row will appear at the top as it is index 0 now
dete_survey_updated = dete_survey_updated.sort_index()

#(Copied from online) To replace headers with top row as the new headers

#Store the first row after the header in a variable
new_header = dete_survey_updated.iloc[0]
#Take all the data less the first row after the header
dete_survey_updated = dete_survey_updated[1:]
#Set the first row as the new dete_survey_updated header
dete_survey_updated.columns = new_header

print(dete_survey_updated.head(5))
```
For adding the new list of renamed column title back into the existing dataset, I had first attached the new list of column titles as the top row of the existing dataset (below the existing/old column titles) from the first chunk of code above (exact description of how each line works is in the code). Then I stored the rest of the dataset minus the top row (the new list of column titles) into a new variable, before declaring the new list of column titles as the headers for the dataset stored in the new variable hence replacing the existing/old column titlesfrom the second chunk of code above(exact description of how each line works is in the code).

```python
#Renaming the column names for the tafe_survey_updated dataset as per requested in Dataquest
tafe_survey_updated = tafe_survey_updated.rename(columns={'Record ID': 'id','CESSATION YEAR': 'cease_date','Reason for ceasing employment': 'separationtype', 'Gender. What is your Gender?': 'gender', 'CurrentAge. Current Age': 'age', 'Employment Type. Employment Type': 'employment_status', 'Classification. Classification': 'position', 'LengthofServiceOverall. Overall Length of Service at Institute (in years)': 'institute_service', 'LengthofServiceCurrent. Length of Service at current workplace (in years)': 'role_service'})

print(tafe_survey_updated.head(5))
```
For tafe_survey dataset:

The Dataquest guide provide the desired column titles for the tafe_survey which I simply used the 'rename()' function that will individually substitute the new titles with the old ones using a dictionary input.

<br>

_Task 4_
```python
import pandas as pd

dete_survey= pd.read_csv('dete_survey3.csv')
tafe_survey = pd.read_csv('tafe_survey3.csv')

print(dete_survey['separationtype'].value_counts())
print(tafe_survey['separationtype'].value_counts())

#To select all the rows with people that has indicated resignation (all 3 types) in the 
#'seperationtype' column in dete_survey
dete_resignations = dete_survey.loc[(dete_survey['separationtype'] == 'Resignation-Other reasons') | (dete_survey['separationtype'] == 'Resignation-Other employer') | (dete_survey['separationtype'] == 'Resignation-Move overseas/interstate')]
print(dete_resignations)

#To select all the rows with people that has indicated resignation in the 
#'seperationtype' column in tafe_survey
tafe_resignations = tafe_survey.loc[tafe_survey['separationtype'] == 'Resignation']
print(tafe_resignations)
```
For Task 4, the task is to filter out rows/respondants that indicated they exited the organisation by resignation in both the dete_survey and tafe_survey datasets. 

From '.value_counts()' function we can see there are 3 types of resignation indicated by respondants in the dete_survey ('Resignation-Other reasons', 'Resignation-Other employer' and 'Resignation-Move overseas/interstate'), all of which we will consider as resignation and will filter all 3 of them into consideration.

From '.value_counts()' function we can see there is only 1 type of resignation indicated by respondants in the tafe_survey ('Resignation') which is the only type of respondants we will take into consideration.

<br>

_Task 5_
```python
import pandas as pd

dete_survey= pd.read_csv('dete_survey4(resignations).csv')
tafe_survey = pd.read_csv('tafe_survey4(resignations).csv')

#The 'cease_date' column for dete_survey is currently an object datatype as seen using the 'info()' 
#function and not float so we'll need to convert it so it can more easily used later on in data analysis
print(dete_survey.info())

#The 'cease_date' column for tafe_survey is already a float datatype as seen using the 'info()' 
#function so there is no need for us to convert its data type
print(tafe_survey.info())

#Need to add 'dropna=False' as by default 'dropna=True' which ignores counts of NAN inputs which we do
#not want, as we want to consider them in the counts as well to see the full picture for both dete_survey
#and tafe_survey. 

#We can see there is some issue with dete_survey's 'cease_date' column while tafe_survey's 'cease_date'
#column has no issue. We need to tackle the column for dete_survey
print(dete_survey['cease_date'].value_counts(dropna=False))
print(tafe_survey['cease_date'].value_counts(dropna=False))
```
For task 5, the task is to clean the 'cease_date' column in the dete_survey dataset so that it can be used for later's of calculating the duration of service for respondants in the dete_survey for data analysis. Technically there is no need to check that for the tafe_survey dataset as it already has a duration of service column but we checked its data type anyway.

To check the data type of the 'cease_date' column for both datasets, we used the '.info()' function.

To check the type of values under the 'cease_date' column for both datasets, we used the 'value_counts()' function. 

We discovered that the 'cease_date' column in dete_survey has undesired inputs (strings) that we need to change to floats while the 'cease_date' column in tafe_survey already has the desired data type (float) and no unusual inputs.

```python
#(Copied from online) It can split the string using the slash as the delimiter into 2 elements 
#in a list and only selecting the last element (from the '.str[-1]' function from the list as the input 
#(which will always be the year be it the list has one or two elements as the year will always be the 
#first element from the back (last element))
dete_survey['cease_date'] = dete_survey['cease_date'].str.split('/').str[-1]

#By checking here we can see that we removed the inputs with months and gave us a more accurate number of 
#the counts of how many people resigned from the dete_survey per year
print(dete_survey['cease_date'].value_counts(dropna=False))

#Converting data type of the 'cease_date' column for the dete_survery from object to a float
dete_survey['cease_date'] = dete_survey['cease_date'].astype(float)

#To check if the data type for the 'cease_date' column for the dete_survery has indeed changed 
print(dete_survey.info())


#To print out final dete_survey's and tafe_survey's value counts
print(dete_survey['cease_date'].value_counts(dropna=False).sort_index(ascending=True))
print(tafe_survey['cease_date'].value_counts(dropna=False).sort_index(ascending=True))
```
For dete_survey dataset:

To tackle the unusual inputs, it is covered by the comment in the code, using functions such as '.str.split()' and '.str[]' (vectorized string methods)

To tackle the wrong data type, we use the '.astype()' function to convert the data type from object to float.

<br>

_Task 6_
```python
import pandas as pd

#We need an 'institute_service' column in dete_survey so we can compare with its corresponding column
#in the tafe_survey dataset
dete_survey= pd.read_csv('dete_survey5(resignations).csv')

#Subtracting the dete_start_date from the cease_date and assign the result to a new column named 
#institute_service.
dete_survey['institute_service'] = dete_survey['cease_date'] - dete_survey['dete_start_date']

print(dete_survey.head(5))
```
For task 6, the task is to create the 'institute_service' column representing how long the respondant has been with the institute/organisation in the dete_survey dataset as it is missing in this dataset, which we need to compare to the corresponding column in the tafe_survey dataset.

We do this by subtracting the 'dete_start_date' inputs from the 'cease_date' inputs and putting the result in a newly created 'institute_service' column in the dete_survey dataset.

<br>

_Task 7_
```python
import pandas as pd
import numpy as np

dete_survey= pd.read_csv('dete_survey6(resignations).csv')
tafe_survey = pd.read_csv('tafe_survey5(resignations).csv')

def main():
    #1. To check the value counts for some of the columns we deem that the employee is dissatisfied such as the
    #   'job_dissatisfaction' and 'dissatisfaction_with_the_department' columns in the dete_survey dataset.
    #   As we can see, it is already all in Boolean marking (True, False, NaN)
    print(dete_survey['job_dissatisfaction'].value_counts(dropna=False))
    print(dete_survey['dissatisfaction_with_the_department'].value_counts(dropna=False))

    #To check the value counts for the 'Contributing Factors. Dissatisfaction' and 'Contributing Factors. 
    #Job Dissatisfaction' columns in the tafe_survey dataset.
    #As we can see, they are not yet in Boolean hence we need to first change that
    print(tafe_survey['Contributing Factors. Dissatisfaction'].value_counts(dropna=False))
    print(tafe_survey['Contributing Factors. Job Dissatisfaction'].value_counts(dropna=False))

    #2. Making the columns in tafe_survey to only contains True, False or NaN values

    #Note: The usual brute force method
    #tafe_survey.loc[tafe_survey['Contributing Factors. Dissatisfaction'] == 'Contributing Factors. Dissatisfaction ', 'Contributing Factors. Dissatisfaction'] = True
    #tafe_survey.loc[tafe_survey['Contributing Factors. Dissatisfaction'] == '-', 'Contributing Factors. Dissatisfaction'] = False
    #tafe_survey.loc[tafe_survey['Contributing Factors. Job Dissatisfaction'] == 'Job Dissatisfaction', 'Contributing Factors. Job Dissatisfaction'] = True
    #tafe_survey.loc[tafe_survey['Contributing Factors. Job Dissatisfaction'] == '-', 'Contributing Factors. Job Dissatisfaction'] = False
    

    #'apply()', 'map()' and 'applymap()' functions  all works in the same way to applying a function to 
    #each element in a Data Structure. The difference in these functions is to which type of 
    #Data Structure they work for.

    #- 'apply()' works for both DataFrames and Series
    #- 'map()' only works for Series
    #- 'applymap()' only works for DataFrames

    #In this case, we are dealing with a Series so 'applymap()' dosen't work, only 'apply()' and 'map()'
    #works.
    #Using the self made 'update_val' and 'apply()' function
    tafe_survey['Contributing Factors. Dissatisfaction'] = tafe_survey['Contributing Factors. Dissatisfaction'].apply(update_val)
    tafe_survey['Contributing Factors. Job Dissatisfaction'] = tafe_survey['Contributing Factors. Job Dissatisfaction'].apply(update_val)
    print(tafe_survey['Contributing Factors. Dissatisfaction'].value_counts(dropna=False))
    print(tafe_survey['Contributing Factors. Job Dissatisfaction'].value_counts(dropna=False))


    #3. Using the '.any()' function, to create a new column with input True if any of the column (of the same row) 
    #   is True, or False if all the columns (of the same row) is False. (I treated if all NaN or False it will be 
    #   False)
    #(The opposite function of this is '.all()' where if all columns needs to be True for the output to be True
    #and if any 1 is False, the resulting output will be False)
    tafe_survey['dissatisfied'] = tafe_survey[tafe_survey.columns[10:12]].any(axis=1)
    dete_survey['dissatisfied'] = dete_survey.iloc[: , [13,14,15,16,17,18,19,25,26]].any(axis=1)
    print(dete_survey['dissatisfied'].value_counts(dropna=False))
    print(tafe_survey['dissatisfied'].value_counts(dropna=False))

    dete_survey.to_csv('dete_survey7(resignations).csv', index=False)
    tafe_survey.to_csv('tafe_survey6(resignations).csv', index=False)
```
For task 7, the task is to create a 'dissatisfied' column that shows if a respondant has resigned due to dissatisfaction (apart from any other reasons). In the Dataquest guide, we have already identify some factors (as column titles) that we deem as the respondant showing they have exited due to dissatisfaction. Hence, in both datasets, as long as the respondant declared at least one factor (that we deem as a sign of dissatisfaction) a reason for exit, we will show they have resigned due to dissatisfaction and will mark it as True in the 'dissatisfied' column. If none of the factors (that we deem as a sign of dissatisfaction) are a reason for exit, we will show that they did not resign due to dissatisfaction and will mark it as False in the 'dissatisfied' column. If all factors (that we deem as a sign of dissatisfaction) are NaN, we will treat it as False as well.

(Regarding technicalities of the code I will leave it to the comments in the code to explain too much to type otherwise 😫)

```python
#Creating the update_val function
def update_val(val):
    if pd.isnull(val):
        return np.nan
    elif val == '-':
        return False
    else:
        return True

main()
```
This is the function used applied to every single element in the tafe_survey columns 'Contributing Factors. Dissatisfaction' and 'Contributing Factors. Job Dissatisfaction' using the '.apply()' function in the main code. Creating a self-made function and applying the '.apply()' function makes the code look neater compared to the brute force method (that I commented out in the main code)

There is no need to change the elements for the factors (columns) (that we deem as a sign of dissatisfaction) in the dete_survey dataset as they are already in Boolean.

<br>

_Task 8_
```python
import pandas as pd

dete_survey= pd.read_csv('dete_survey7(resignations).csv')
tafe_survey = pd.read_csv('tafe_survey6(resignations).csv')

#1. Adding a new 'institute' column to both datasets with all its values as 'DETE' and 'TAFE' respectively
dete_survey['institute'] = 'DETE'
tafe_survey['institute'] = 'TAFE'

#To check the columns are added
print(dete_survey.head(5))
print(tafe_survey.head(5))

print(dete_survey.info())
print(tafe_survey.info())
```
For task 8, the task is to create an 'institute' column in both the dete_survey and tafe_survey dataset and filling its values with 'DETE' and 'TAFE' respectively to indicate which respondant is from which organisation after we combined the 2 datasets. Then, remove any excess columns we do not need for this project's data analysis, ensuring the columns are the same for both datasets and also combining these 2 datasets.

Here, we create the new 'institute' column in both datasets as well as filling said columns.

```python
#Removing excess columns that we won't need in our data analysis. 
#From both the dete_survey and tafe_survey datasets we will only keep the columns 'id', 'seperationtype', 'gender', 'age', 
#'institute_service', 'dissatisfied' and 'institute' (from earlier in this code)
dete_survey_updated = dete_survey[['id', 'separationtype', 'gender', 'age', 'institute_service', 'dissatisfied', 'institute']]
tafe_survey_updated = tafe_survey[['id', 'separationtype', 'gender', 'age', 'institute_service', 'dissatisfied', 'institute']]

#To check the excess columns are removed
print(dete_survey_updated.head(5))
print(tafe_survey_updated.head(5))

print(dete_survey_updated.info())
print(tafe_survey_updated.info())
```
Removing excess columns in both datasets we don't need for this project's data analysis and as a good habit, to check to ensure they are removed.

```python
#2. Combining the datasets (top and bottom)
combined_updated = pd.concat([dete_survey_updated, tafe_survey_updated])
print(combined_updated)
print(combined_updated.info())
```
Combining the 2 datasets with the 'pd.concat()' function

```python
#3. Using the 'dropna()' function to drop any rows that has at least 1 NaN value to eliminate any NaN values in our new combined_updated dataset

#The 'inplace=True' parameter is important! By default 'inplace=False' and the 'dropna()' function will return you a
#new modified DataFrame instead of the existing one. In order to modify the existing dataset with 'dropna()'
#you need to make 'inpplace=True'
combined_updated.dropna(axis=0, how='any', inplace=True)
print(combined_updated.info())
```
Now, we try to make the new combined dataset cleaner by removing any rows that contains any NaN values using the '.dropna()' function (take note of the 'inplace=True' parameter!). Data loss is not too bad looking at the '.info()'

<br>

_Task 9_
```python
import pandas as pd

combined_updated = pd.read_csv('combined_updated.csv')

def main():

    #1. To view the types of values present in the 'institute_service' column
    print(combined_updated['institute_service'].value_counts())
    print(combined_updated.info())

    #There are string values 'Less than 1 year' and 'More than 20 years' in the 'institute_service' column that 
    #we need to deal with. I decided to convert the 'Less than 1 year' values to just a value of 1 and 'More than 
    #20 years' value to a value of 20
    combined_updated.loc[combined_updated['institute_service'] == 'Less than 1 year', 'institute_service'] = 1
    combined_updated.loc[combined_updated['institute_service'] == 'More than 20 years', 'institute_service'] = 20

    #Checking the values in the 'institute_service' column again
    print(combined_updated['institute_service'].value_counts())

    #There are string values '1-2', '3-4', '5-6' '7-10' and '11-20' in the 'institute_service' column that we also
    #need to deal with. I decided to use vectorized string method to split them into a list with '-' as the
    #delimiter and taking the first element in those lists as the new value
    combined_updated['institute_service'] = combined_updated['institute_service'].str.split('-').str[0]

    #Checking the values in the 'institute_service' column again
    print(combined_updated['institute_service'].value_counts())
```
For task 9, the task is to create a 'service_cat' column in both the dete_survey and tafe_survey (now combined) datasets indicating how long a respondant has been working in the organisation. In the Dataquest guide the service categories are defined as:

-New: Less than 3 years at a company

-Experienced: 3-6 years at a company

-Established: 7-10 years at a company

-Veteran: 11 or more years at a company

To do so, we take reference from the 'institute_service' columns for both datasets. Checking the 'institute_service' columns for the combined dataset, there is unusual input in the tafe_survey part of the combined dataset while dete_survey dataset's 'institute_service' column have no unusual input (Because in Task 6, we already cleaned as we created the 'institute_service' columns).

There are unusual inputs (strings) such as 'Less than one year', 'More than 20 years', '1-2', and '11-20' that we dealt with seperately in the code above (technicalities explained in comments in code).

```python
    #Using the Series.astype() method to change the type of the 'institute_service' column to 'float'
    combined_updated['institute_service'] = combined_updated['institute_service'].astype(float)
    
    #Checking the values in the 'institute_service' column again as well as its data type
    print(combined_updated['institute_service'].value_counts())
    print(combined_updated.info())
```
Converting the data type of the 'institute_service' column from object to float after dealing with the unusual inputs.

```python
    #Applying the 'career_stage' function to the 'institute_service' column and adding the new labels into a new
    #column 'service_cat'
    combined_updated['service_cat'] = combined_updated['institute_service'].apply(career_stage)
    print(combined_updated['service_cat'].value_counts())
    print(combined_updated.info())
```
Applying the self-made function 'career_stage' to assign each element/respondants career stage according to the definitions provided by Dataquest's guide through the '.apply()' function once again and creating a 'service_cat' column in the combined dataset in the process.

```python
#Creating the career_stage function
def career_stage(val):
    if val < 3:
        return 'New'
    elif val >= 3 and val <= 6:
        return 'Experienced'
    elif val > 6 and val <= 10:
        return 'Established'
    elif val > 10:
        return 'Veteran'


main()
```
This is how the self-made function 'career_stage' look like, quite similar to the self-made function 'update_val' in Task 7.

<br>

<br>

**3. Data Modelling and Analysis**

Up till now, the cleaning and preparing of the data will enable us to do some data analysis via looking at the patterns of the graphs and answer some questions about the Employee Exit surveys. In my code, I will be exploring questions like 'Are employees who only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been there longer?' and 'Are younger employees resigning due to some kind of dissatisfaction? What about older employees?' (Task 10)

For visualisation, I drew a bar graph of percentage of resigned employees due to dissatisfaction (vs other reasons for exit) for each defined career stage. (Task 10)

_Task 10_
```python
import matplotlib.pyplot as plt
import pandas as pd
```
Imported the matplotlib library to draw graphs.

```python
combined_updated = pd.read_csv('combined_updated2.csv')

#1 and 2. As we can see from this code, we only have True or False values in the 'dissatisfied' column as we have already
#   decided to drop all the rows with NaN values in any of the columns. We may have lost some data, but it is not
#   a significant lost during this cleaning process
print(combined_updated['dissatisfied'].value_counts(dropna=False))

#3 and 4. Using the '.pivot_table()' function to create a pivot table. It takes many parameters (see documentation). 
#   -> The first parameter is the name of dataframe
#   -> 'index=' represents the row headers
#   -> 'values=' represents the column headers
#   -> 'aggfunc=' (by default will be mean so technically no need put here but I just did it so its clear), 
#      represents what operator to use (see documentation for list of accepted operators). Since the values are all =
#      Boolean and Python can take Boolean values as int 1 (for True) and 0 (for False), finding mean will give
#      us percentage of respondants that said True and False for dissatisfied, and categorized by their service_cat
#      shown in row header in the pivot table
dissatisfied_pivot_table = pd.pivot_table(combined_updated, index='service_cat', values='dissatisfied', aggfunc='mean')
print(dissatisfied_pivot_table)
```
For Task 10, the task is to create a graph to have a visual aid for us to answer some questions of this guided project's data analysis.

We first printed out '.value_counts()' of the combined dataset to have a idea of what kind of data we are working with, noticing to show NaN values (if any).

We now made use of Panda's '.pivot_table()' function (quite a powerful and new tool) that enabled us to apply different kinds of operators to any dataframe such as 'count', 'mean', 'sum', etc. to reveal interesting statistics of our dataframe. In this case, we wish to see the percentage of people that has True in the 'dissatisfied' column for every career group in the combined dataset. Since Python can take Boolean values True as 1 and False as 0, the mean value (under the 'pivot_table()' function) of the 'dissatisfied' column for each career group will show us the percentage of people that has True in the 'dissatisfied' column for every career group in the combined dataset.

(Again, regarding technicalities of the code I will leave it to the comments in the code to explain😫)

```python
#5. Plotting the results in a bar graph
xaxis = ['Established', 'Experienced', 'New', 'Veteran']
#Using the new 'dissatisfied' column given to us in the pivot table as the y-axis data
yaxis = dissatisfied_pivot_table['dissatisfied']

plt.bar(xaxis, yaxis)

plt.title('Bar Graph of Percentage of Resigned Dissatisfied Employees\n(by Service Category)')
plt.xlabel('Service Category')
plt.ylabel('Percentage of Resigned Dissatisfied Employees\n(vs other reasons for exiting the company)')

plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6])

plt.savefig('bargraph(resigned_dissatisfied_employees_(by_service_category)).png', dpi=100)

plt.show()
```

![My Image](bargraph(resigned_dissatisfied_employees_(by_service_category)).png)

Code for drawing the graph. (matplotlib stuffs)

From the graph, we can see that career groups 'Established' (7-10 years institute service) and 'Veteran' (more than 11 years of institute service) has the highest percentage of resignation due to dissatisfaction, while the career group 'New' (Less than 3 years of institute service) has the lowest percentage of resignation due to dissatisfaction.

<br>

<br>

**4. Analysing Other Aspects of the Dataset**

Task 10 marked the end of the guided part of the data analysis of the Employee Exit survey, and that Dataquest recommends that we try to analyse other aspects and find any interesting results from our analysis such as 'Decide how to handle the rest of the missing values. Then, aggregate the data according to the service_cat column again. How many people in each career stage resigned due to some kind of dissatisfaction?', 'Clean the age column. How many people in each age group resgined due to some kind of dissatisfaction?' and 'Instead of analyzing the survey results together, analyze each survey separately. Did more employees in the DETE survey or TAFE survey end their employment because they were dissatisfied in some way?'

In Task 11, I decided to see 'How many people in each age group resgined due to some kind of dissatisfaction?'

_Task 11_
```python
import pandas as pd
import matplotlib.pyplot as plt

combined_updated = pd.read_csv('combined_updated.csv')

def main():
    #Checking all the different types of values present in the 'age' column. (Noticed there are no NaN values as we
    #cleared them earlier in the project already)
    print(combined_updated['age'].value_counts(dropna=False))

    #I plan to split the age groups into 6 groups:
    #-> <21
    #-> 21 to 30
    #-> 31 to 40 
    #-> 41 to 50 
    #-> 51 to 60 
    #-> >60
```
In task 11, the task is to create a graph to have a visual aid for us to answer the selected question (stated above) of this project's data analysis.

We define the age groups in the commented part of the code after checking the types of values we have in the 'age' column.

```python
    #Cleaning the age column (I plan to split the current values into a list and taking only the first element)
    #First split those values with spaces and taking the first element
    combined_updated['age'] = combined_updated['age'].str.split(' ').str[0]
    print(combined_updated['age'].value_counts(dropna=False))

    combined_updated['age'] = combined_updated['age'].str.split('-').str[0]
    print(combined_updated['age'].value_counts(dropna=False))
```
Similar to a part of the code Task 9, we encountered unusual inputs such as '41  45' and '26-30' that we need to deal with using vectorized string methods to get the desired input (of a single float).

```python
    #Making the data type of the 'age' column into floats
    combined_updated['age'] = combined_updated['age'].astype(float)
```
Converting the data type of the 'age' column from object to float after dealing with the unusual inputs.

```python
    #Creating a function and mapping it to the 'age' column to split the respondants to different age groups and 
    #assigning the age groups to an 'age_group' column
    combined_updated['age_group'] = combined_updated['age'].apply(age_group)
    print(combined_updated['age_group'].value_counts(dropna=False))
    print(combined_updated.head(5))
```
Similar to Task 9 again, creating a self-made function 'age_group' and later applying to the 'age' column using '.apply()' to split each element'respondant to an age group while creating a new 'age_group' column in the combined dataset.

```python
    #Plotting out the results in a bar graph
    #5. Plotting the results in a bar graph
    xaxis = ['21 to 30', '31 to 40', '41 to 50', '51 to 60', '<21', '>60']

    #Creating a pivot table and using the new 'dissatisfied' column given to us in the pivot table as the 
    #y-axis data
    dissatisfied_pivot_table = pd.pivot_table(combined_updated, index='age_group', values='dissatisfied', aggfunc='count')
    print(dissatisfied_pivot_table)
    yaxis = dissatisfied_pivot_table['dissatisfied']
```
Similar to task 10, making use of Panda's '.pivot_table()' function and passing the 'count' operator this time (instead of 'mean' in task 10) to obtain the count of number of resignation due to dissatisfaction per age group.

Then using the count number of resignation due to dissatisfaction per age group obtained from the pivot table as data for the y-axis of the bar graph later.

```python
    plt.bar(xaxis, yaxis)

    plt.title('Bar Graph of Number of Resigned Dissatisfied Employees\n(by Age Group)')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Resigned Dissatisfied Employees')

    plt.yticks([0,20,40,60,80,100,120,140,160,180])

    plt.savefig('bargraph(number_of_dissatisfied_employees_(by_age_group)).png', dpi=100)

    plt.show()
```
![My Image](bargraph(number_of_dissatisfied_employees_(by_age_group)).png)

Code for drawing the graph. (matplotlib stuffs)

From the graph, we can see that age group of '41-50' has the highest number of resignation due to dissatisfaction among all the age groups, with '<21' and '>60', the extreme ends of the age group having the least number of resignation due to dissatisfaction. 

```python
#Creating the age_group function
def age_group(val):
    if val < 21:
        return '<21'
    elif val >= 21 and val <= 30:
        return '21 to 30'
    elif val >= 31 and val <= 40:
        return '31 to 40'
    elif val >= 41 and val <= 50:
        return '41 to 50'
    elif val >= 51 and val <= 60:
        return '51 to 60'
    elif val > 60:
        return '>60'

main()
```
This is how the self-made function 'age_group' look like at the end of the code for earlier, quite similar to the self-made function 'career_group' from Task 9 and 'update_val' in Task 7.

<br>

_Analysis of Task 10 bar graph_

A possible reason I can think of for why a higher percentage of respondants that have had longer institute service resigned due to some sort of dissatisfaction is that it gets boring doing the same job for so many years due to same tasks, people and environment everyday, and disagreements may build up. While those with shorter institute service still have much to learn and that since they worked hard to be able to join the institute, and everything may seem more exciting and new for them to learn that they are more unlikely to leave at an early stage.

<br>

_Analysis of Task 11 bar graph_

I feel there might be many reasons for the trend.

One reason could be poor dataset as there are fewer respondants doing the surveys under the extreme age groups of <21 and >60 hence lower number of people under these age group indicating resignation by dissatisfaction. (haven't really checked the datasets fully, may be proven wrong)

Another reason (provided the dataset is good and spread among the age groups evenly), is that younger people (<21) may find the workplace new and are learning a lot and are obviously won't resign so early immdiately after getting a job. While older people (>60) may have spent many years on the job and the fact that they have spent so many years on that job may show it is very satisfactory for them and are hence also more unlikely to resign from the job due to dissatisfaction.

Meanwhile, higher number resign due to dissatisfaction at the from 30 to 50s due to boredom from working at a job they dislike after a while or maybe they are able to find other jobs suitable for their skillset and can switch jobs more easily hence are less tolerable to dissatisfaction as they have more freedom to choose from the younger age groups.

<br>

<br>

## Thoughts after the project
Urghhhhhhhhhh I almost reached 1000 lines in this readme file... Will probably shorten this next time, wayyyyyyyy too much typing.

I feel that this project definitely expanded my tool box for data analysis through discovering newer and powerful functions such as '.pivot_table()' and '.apply()'.

Through talking with other programmers, I've learnt that at my current stage of coding I would like to keep exploring the different aspects of programming such as using other more complex libraries such as TensorFlow, Scikit-learn and PyTorch for machine learning, neural network, making backend/frontend/full stack websites and not to stick to one for now. 

I believe that I will be moving on to projects of a different nature in the next one, or to more learning journey repositories such as understanding more on different Algorithms and Data Structures.

<br>

To be improved:
* I might stop making this section in the future as there will always be more and more things to be improved the more you look at your code and the list will be endless. One quick one is I haven't tried figure out how to align the x-axis of both graphs in ascending order for the career group and age group. But I believe this can be a quick fix with a quick google search.

<br>

Have a gif:

![Semantic description of image](https://media4.giphy.com/media/GeimqsH0TLDt4tScGw/200w.webp?cid=ecf05e47qay4jqawe7nw3xpt76cn1n2qu1va8rld7g3h5g17&ep=v1_gifs_search&rid=200w.webp&ct=g)
