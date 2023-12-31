# Best Practices

<a name="top"></a>

## About it
> This is the best Practices

## Table of contents :

1. [Merge Two DataFrame](#merge-two-dataframe)
2. [Vlookup in Pandas](#vlookup-in-pandas)
3. [Concatenate two columns using pandas](#concatenate-two-columns-using-pandas)
4. [Install JupyterLab](#install-jupyterlab)
5. [Extract SAP using Excel](#extract-sap-transaction-using-excel)
6. [Extract SAP Using Excel Method 2](#extract-sap-transaction-using-excel-method-2)
7. [Connect to AWS using OS](#connect-to-aws-using-os)
8. [Schedule run SQL query - sqlite](#schedule-run-sql-query)
9. [Schedule run SQL query MSSQL](#schedule-run-sql-query-mssql)
10. [Schedule run SQL query MSSQL and copy files](#schedule-run-sql-query-mssql-and-copy-files)
11. [Schedule run SQL query MSSQL and copy One file](#schedule-run-sql-query-mssql-and-copy-one-file)
12. [Copy specific files](#copy-specific-files)
13. [Complete code for creating Chatbot](#complete-code-for-creating-chatbot)
14. [Reading Large CSV files in Pandas](#reading-large-csv-files-in-pandas)
15. [Reading Large CSV files in Pandas and Data Type](#reading-large-csv-files-in-pandas-and-adjust-data-type)
16. [Pandas > Filter and Convert Datetime](#pandas--filter-and-convert-datetime)
17. [SQL > Explain Locate and Position](#sql--explain-locate-and-position)
18. [AWS > Position Function](#aws--position-function)
19. [AWS > SUBSTR and LENGTH](#aws--substr-and-length)
20. [Convert QVD to Parquet](#convert-qvd-to-parquet)
21. [Benefits of Parquet file](#benefits-of-parquet-file)
22. [Pandas > Read Large Parquet files](#pandas--read-large-parquet-files)
23. [SQL > Grant Access](#sql--grant-access)
    1.   [View Access](#view-access)
    2.   [Revoke View Access](#revoke-view-access)
    3.   [Grant Execute Procedure](#grant-execute-procedure)
    4.   [Grant Execute Procedure and remove other users](#grant-execute-procedure-and-remove-other-users)
    5.   [Back The User Admin works again](#back-the-user-admin-works-again)
    6.   [allow PowerBI_HQ to only execute the job](#allow-powerbi_hq-to-only-execute-the-job)
    7.   [Restoring t_board_db to its original state](#restoring-t_board_db-to-its-original-state)
24. [YouTube Download 1080](#youtube-download-1080)
    1.  [YouTube Download 720](#youtube-download-720)
25. [Setup environment variables in VSCode](#setup-environment-variables-in-vscode)
    1.  [Multiple projects same workspace in VSCode](#multiple-projects-within-the-same-workspace-in-vscode)
    2.  [General .env file that's across projects](#general-env-file-thats-shared-across-multiple-projects)
26. [Anaconda Commands](#anaconda-commands)
27. [Read file Names in Directory](#read-file-names-in-directory)
28. [SQL > Delete from Table](#sql--delete-from-table)
29. [Qlikview Scripts](#qlikview-scripts)
    1.  [Loading Max File Name](#loading-max-file-name)
    2.  [Add Load](#add-load)
    3.  [recno()](#recno)
    4.  [Load Excel and Sheet dynamically](#load-excel-and-sheet-dynamically)
30. [Pandas > Outlier](#pandas--outlier)
31. [SQL Scripts](#sql-scripts)
    1.  [Final all views and jobs](#final-all-views-and-jobs)
    2.  [Identify triggers on a table](#identify-triggers-on-a-table)
    3.  [Find which stored procedures are used](#find-which-stored-procedures-are-used)
    4.  [Dynamic return last two months](#dynamic-return-last-two-months)
32. [DataBricks](#databricks)
    1.  [Convert KEY](#convert-the-modified-private-key-back-to-standard-pem-format)
    2.  [Read Parquet files](#read-all-parquet-files-in-dbfs)
    3.  [Read YAML file](#read-yaml-file)
    4.  [Create Incrmental Loading](#create-incrmental-loading)
    5.  [Write csv to S3 Bucket](#write-csv-to-s3-bucket)
    6.  [Write Parquet to S3 Bucket](#write-parquet-to-s3-bucket)
33. [Athena](#athena)
    1.  [SUBSTR and SUBSTRING](#substr-and-substring)
    2.  [Date and Year](#date-and-year)
34. [Python > Copy files](#python--copy-files)
35. [Python > Dynamic Column Rename](#python--dynamic-column-rename)
36. [Python > Rename file with date](#python--rename-file-with-date)
37. [Alteryx > Read Parquet file](#alteryx--read-parquet-file)


### Merge two dataframe:
```py
import pandas as pd

# create two sample DataFrames
df1 = pd.DataFrame({
    "key": [1, 2, 3, 4],
    "A": ["A1", "A2", "A3", "A4"]
})

df2 = pd.DataFrame({
    "key": [3, 4, 5, 6],
    "B": ["B3", "B4", "B5", "B6"]
})

# merge the two DataFrames on the "key" column
merged_df = df1.merge(df2, on="key")
```
[Back to Top](#top)
### Vlookup in Pandas
```py
import pandas as pd

# create a sample "lookup" DataFrame
lookup_df = pd.DataFrame({
    "key": [1, 2, 3, 4],
    "value": ["A", "B", "C", "D"]
})

# create a sample DataFrame to lookup values in
data_df = pd.DataFrame({
    "key": [2, 4, 6, 8],
    "other_columns": ["X", "Y", "Z", "W"]
})

# merge the two DataFrames on the "key" column
merged_df = data_df.merge(lookup_df, on="key", how="left")
```
[Back to Top](#top)
### Concatenate two columns using pandas
```py
import pandas as pd

# create a sample DataFrame
df = pd.DataFrame({
    "column_1": ["A", "B", "C", "D"],
    "column_2": ["1", "2", "3", "4"]
})

# concatenate the values of the two columns
df["concatenated"] = df["column_1"].astype(str) + df["column_2"].astype(str)
```
[Back to Top](#top)
### Install JupyterLab
```sh
$ conda install -c conda-forge jupyterlab
```
[Back to Top](#top)
### Extract SAP Transaction Using Excel:
```vb
Sub ExtractDataFromSAPAndClose()

Dim SAPSession As Object
Dim SAPGuiAuto As Object
Dim Connection As Object
Dim Session As Object
Dim xlApp As Excel.Application
Dim wb As Workbook

Set SAPGuiAuto = GetObject("SAPGUI")
Set SAPSession = SAPGuiAuto.GetScriptingEngine

Set Connection = SAPSession.Children(0)
Set Session = Connection.Children(0)

Session.findById("wnd[0]").maximize

'Enter your SAP transaction code here
Session.findById("wnd[0]/tbar[0]/okcd").Text = "/nse16"
Session.findById("wnd[0]").sendVKey 0

'Enter your SAP data extraction logic here

'Save the file with the specified name
Session.findById("wnd[1]/usr/ctxtDY_FILENAME").Text = "ZFGL0003_CU_" & Format(Now, "yyyymm") & ".xlsx"
Session.findById("wnd[1]/tbar[0]/btn[11]").press

'Close the specified Excel file
Set xlApp = GetObject(, "Excel.Application")
Set wb = xlApp.Workbooks("ZFGL0003_CU_" & Format(Now, "yyyymm") & ".xlsx")
wb.Close SaveChanges:=False

End Sub
```
[Back to Top](#top)
### Extract SAP Transaction Using Excel (Method 2) :
```vb
Sub ExtractDataFromSAPAndClose()

Dim SAPSession As Object
Dim SAPGuiAuto As Object
Dim Connection As Object
Dim Session As Object
Dim FilePath As String

Set SAPGuiAuto = GetObject("SAPGUI")
Set SAPSession = SAPGuiAuto.GetScriptingEngine

Set Connection = SAPSession.Children(0)
Set Session = Connection.Children(0)

Session.findById("wnd[0]").maximize

'Enter your SAP transaction code here
Session.findById("wnd[0]/tbar[0]/okcd").Text = "/nse16"
Session.findById("wnd[0]").sendVKey 0

'Enter your SAP data extraction logic here

'Save the file with the specified name
FilePath = ThisWorkbook.Path & "\ZFGL0003_CU_" & Format(Now, "yyyymm") & ".xlsx"

'Check if the file already exists, and if it does, delete it
If Dir(FilePath) <> "" Then
    Kill FilePath
End If

Session.findById("wnd[1]/usr/ctxtDY_FILENAME").Text = FilePath
Session.findById("wnd[1]/tbar[0]/btn[11]").press

'Close the specified Excel file
Kill FilePath

End Sub
```
[Back to Top](#top)
### Connect to AWS using OS:
```py
import boto3
import pandas as pd
import os

# Set the AWS access key, secret access key, and session token as environment variables
os.environ['AWS_ACCESS_KEY_ID'] = 'your_access_key_id'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'your_secret_access_key'
os.environ['AWS_SESSION_TOKEN'] = 'your_session_token'

# Create an S3 client object using boto3, and specify the region and workgroup if required
session = boto3.Session(region_name='us-west-2', workgroup='your_workgroup')
s3 = session.client('s3')

# Specify the S3 bucket and object key, and download the file to a local directory
bucket_name = 'your_bucket_name'
object_key = 'your_object_key'
file_path = 'local_file_path'
s3.download_file(bucket_name, object_key, file_path)

# Read the downloaded file as a pandas DataFrame
df = pd.read_csv(file_path)

# Output the DataFrame to Alteryx
Output = pd.DataFrame(df)
```
[Back to Top](#top)
### Schedule run SQL query:
```py
import datetime
import time
import pandas as pd
import sqlite3

# Set the path to the database file
db_path = 'path/to/database.db'

# Set the path to the output folder
output_path = 'path/to/output/folder'

# Define the SQL query
query = 'SELECT * FROM table_name'

# Define the filename for the output file
filename = 'output.csv'

# Define the frequency at which to run the query (e.g. every day at 3am)
schedule_time = datetime.time(hour=3, minute=0)

# Run the query at the scheduled time
while True:
    now = datetime.datetime.now().time()
    if now.hour == schedule_time.hour and now.minute == schedule_time.minute:
        # Connect to the database
        conn = sqlite3.connect(db_path)

        # Execute the query and save the results to a DataFrame
        df = pd.read_sql_query(query, conn)

        # Close the database connection
        conn.close()

        # Save the DataFrame to a CSV file
        file_path = f'{output_path}/{filename}'
        df.to_csv(file_path, index=False)

        # Wait until the scheduled time for the next run
        time.sleep(60)  # Wait for 1 minute before checking again
```
[Back to Top](#top)
### Schedule run SQL query MSSQL :
```py
import datetime
import time
import pandas as pd
import pyodbc
# Set the connection details
server = 'my_server_name'
database = 'my_database_name'
trusted_connection = 'yes'
# Set the path to the output folder
output_path = 'path/to/output/folder'
# Define the SQL query
query = 'SELECT * FROM table_name'
# Define the filename for the output file
filename = 'output.csv'
# Define the frequency at which to run the query (e.g. every day at 3am)
schedule_time = datetime.time(hour=3, minute=0)
# Define the connection string
conn_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}"
# Run the query at the scheduled time
while True:
    now = datetime.datetime.now().time()
    if now.hour == schedule_time.hour and now.minute == schedule_time.minute:
        # Connect to the database
        conn = pyodbc.connect(conn_string)
        # Execute the query and save the results to a DataFrame
        df = pd.read_sql_query(query, conn)
        # Close the database connection
        conn.close()
        # Save the DataFrame to a CSV file
        file_path = f'{output_path}/{filename}'
        df.to_csv(file_path, index=False)
        # Wait until the scheduled time for the next run
        time.sleep(60)  # Wait for 1 minute before checking again
```
[Back to Top](#top)
### Schedule run SQL query MSSQL and copy files :
```py
import os
import shutil
import schedule
import time
# Set the path to the source and destination folders
src_folder = 'path/to/source/folder'
dst_folder = 'path/to/destination/folder'
# Define the function to copy the files
def copy_files():
    # Get the list of files in the source folder
    files = os.listdir(src_folder)
    # Loop through each file and copy it to the destination folder
    for file in files:
        src_path = os.path.join(src_folder, file)
        dst_path = os.path.join(dst_folder, file)
        shutil.copy(src_path, dst_path)
    print(f'Copied {len(files)} files from {src_folder} to {dst_folder}')
# Schedule the task to run every day at a specific time
schedule.every().day.at('12:00').do(copy_files)
# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 1 minute before checking again
```
[Back to Top](#top)
### Schedule run SQL query MSSQL and copy One file:
```py
import os
import shutil
import schedule
import time
# Set the path to the source and destination folders
src_folder = 'path/to/source/folder'
dst_folder = 'path/to/destination/folder'
# Set the filename of the file to copy
filename = 'file_to_copy.txt'
# Define the function to copy the file
def copy_file():
    # Check if the file exists in the source folder
    src_path = os.path.join(src_folder, filename)
    if not os.path.isfile(src_path):
        print(f'File {filename} does not exist in {src_folder}')
        return
    # Copy the file to the destination folder
    dst_path = os.path.join(dst_folder, filename)
    shutil.copy(src_path, dst_path)
    print(f'Copied file {filename} from {src_folder} to {dst_folder}')
# Schedule the task to run every day at a specific time
schedule.every().day.at('12:00').do(copy_file)
# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 1 minute before checking again
```
[Back to Top](#top)
### Copy specific files:
```py
import os
import shutil
# Set the path to the source and destination folders
src_folder = 'path/to/source/folder'
dst_folder = 'path/to/destination/folder'
# List of files to copy
files_to_copy = ['file1.txt', 'file2.txt', 'file3.txt']
# Loop through the list of files and copy each one to the destination folder
for file in files_to_copy:
    src_path = os.path.join(src_folder, file)
    dst_path = os.path.join(dst_folder, file)
    # Check if the file exists in the source folder
    if not os.path.isfile(src_path):
        print(f'File {file} does not exist in {src_folder}')
        continue
    # Copy the file to the destination folder
    shutil.copy(src_path, dst_path)
    print(f'Copied file {file} from {src_folder} to {dst_folder}')
```
[Back to Top](#top)
### Complete code for creating Chatbot:
```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey", "What's up"],
      "responses": ["Hello!", "Hi there!", "Greetings!"]
    },
    {
      "tag": "goodbye",
      "patterns": ["Bye", "See you later", "Goodbye"],
      "responses": ["Goodbye!", "See you later!", "Take care!"]
    },
    {
      "tag": "thanks",
      "patterns": ["Thank you", "Thanks", "Appreciate it"],
      "responses": ["You're welcome!", "No problem!", "My pleasure!"]
    },
    {
      "tag": "animal",
      "patterns": ["What does a {animal} eat?", "What is a {animal}?", "Tell me about {animal}"],
      "responses": ["A {animal} eats {diet}.", "A {animal} is a {type} animal.", "Sure! {animal} are {description}"]
    }
  ]
}
```
```py
import random
import json
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
import numpy as np
lemmatizer = WordNetLemmatizer()
intents_file = open('intents.json').read()
intents = json.loads(intents_file)
words = []
classes = []
documents = []
ignore_chars = ['?', '!', '.', ',']
# loop through each sentence in the intents patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        # add the sentence to documents
        documents.append((word_list, intent['tag']))
        # add the intent tag to classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
# lemmatize and lowercase each word and remove duplicates
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_chars]
words = sorted(list(set(words)))
# sort classes
classes = sorted(list(set(classes)))
# create training data
training_data = []
output_empty = [0] * len(classes)
for document in documents:
    bag = []
    word_patterns = document[0]
    # lemmatize and lowercase each word in the sentence
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    # create a bag of words for each sentence
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    # create output
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training_data.append([bag, output_row])
# shuffle the data and convert to numpy array
random.shuffle(training_data)
training_data = np.array(training_data)
# split data into training and testing sets
train_x = list(training_data[:,0])
train_y = list(training_data[:,1])
# define the model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))
# compile the model
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
# train the model
history = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
# save the model
model.save('chatbot_model.h5', history)
print('Chatbot training completed!')
```
> after saving the model, please provide me the rest of the code to test the model
```py
import random
import json
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
lemmatizer = WordNetLemmatizer()
intents_file = open('intents.json').read()
intents = json.loads(intents_file)
words = []
classes = []
documents = []
ignore_chars = ['?', '!', '.', ',']
# loop through each sentence in the intents patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        # add the sentence to documents
        documents.append((word_list, intent['tag']))
        # add the intent tag to classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
# lemmatize and lowercase each word and remove duplicates
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_chars]
words = sorted(list(set(words)))
# sort classes
classes = sorted(list(set(classes)))
# load the model
model = load_model('chatbot_model.h5')
# create a function to process user input
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words if word not in ignore_chars]
    return sentence_words
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)
# create a function to predict the intent of a user's message
def predict_intent(message):
    # generate probabilities from the model
    probabilities = model.predict(np.array([bag_of_words(message)]))[0]
    # get the index of the highest probability
    index = np.argmax(probabilities)
    # return the corresponding tag
    return classes[index]
# create a function to get a response from the chatbot
def get_response(intents_list, intent):
    for i in intents_list['intents']:
        if i['tag'] == intent:
            result = random.choice(i['responses'])
            break
    return result
# create a chatbot
while True:
    message = input("You: ")
    intent = predict_intent(message)
    response = get_response(intents, intent)
    print("Chatbot:", response)
```
```markdown
In this code, we first load the trained model from the saved file. Then we define two functions to process the user's input and predict the intent of the message using the loaded model. Finally, we define a function to generate a response based on the predicted intent, and we use these functions to create a simple chatbot that can communicate with the user.

You can run this code to test your chatbot and see how well it performs.
```
[Back to Top](#top)
### Reading Large CSV files in Pandas:
```py
import pandas as pd
# Set the chunksize parameter to control the size of each chunk
chunksize = 10**6
# Create an empty DataFrame to append each chunk to
df = pd.DataFrame()
# Iterate over each chunk of the CSV file and append it to the DataFrame
for chunk in pd.read_csv('large_file.csv', low_memory=False, nrows=1000000, chunksize=chunksize):
    # Remove any unnecessary columns or rows here
    df = pd.concat([df, chunk])
# Do further processing on the DataFrame as needed
```
[Back to Top](#top)
### Reading Large CSV files in Pandas and adjust Data Type:
```py
import pandas as pd
# Define the data types for each column
dtypes = {
    'column_name_1': 'int32',
    'column_name_2': 'float64',
    'column_name_3': 'category',
    # ...
}
# Specify the columns to read from the CSV file
columns_to_read = ['column_name_1', 'column_name_2', 'column_name_3']
# Set the chunksize parameter to control the size of each chunk
chunksize = 10**6
# Create an empty DataFrame to append each chunk to
df = pd.DataFrame()
# Iterate over each chunk of the CSV file and append it to the DataFrame
for chunk in pd.read_csv('large_file.csv', dtype=dtypes, usecols=columns_to_read, chunksize=chunksize):
    df = pd.concat([df, chunk])
# Do further processing on the DataFrame as needed
```
[Back to Top](#top)
### Pandas > Filter and Convert Datetime:
> In this example, we first filter out the rows where the SCR_EOV_ID column is equal to -1 using the .loc method and extract the values using .values. Then we convert the filtered values to datetime format using pd.to_datetime(). Finally, we replace the original SCR_EOV_ID column with the filtered and converted values using .loc
```py
import pandas as pd
# create a sample dataframe with a column of string dates
df = pd.DataFrame({'SCR_EOV_ID': ['20230201', '-1', '20230203', '-1']})
# filter out rows with '-1' in the SCR_EOV_ID column and extract the values
scr_eov_id = df.loc[df['SCR_EOV_ID'] != '-1', 'SCR_EOV_ID'].values
# convert the filtered values to datetime format
scr_eov_id = pd.to_datetime(scr_eov_id, format='%Y%m%d')
# replace the original column with the filtered and converted values
df.loc[df['SCR_EOV_ID'] != '-1', 'SCR_EOV_ID'] = scr_eov_id
# display the resulting dataframe
print(df)
```
[Back to Top](#top)
### SQL > Explain Locate and Position:
**SQL:**
> In SQL (Structured Query Language), the LOCATE() function is used to search for a substring within a string and returns the position of the first occurrence of the substring within the string.
The syntax of the LOCATE() function is as follows:
```sql
LOCATE(substring, string, start_position)
```
> Here, substring is the substring that you want to search for, string is the string that you want to search within, and start_position is an optional argument that specifies the position within the string where the search should start. If start_position is not provided, the search will start from the beginning of the string.
The function returns an integer value that represents the position of the first occurrence of the substring within the string. If the substring is not found within the string, the function returns 0.
For example, consider the following SQL query:
```sql
SELECT LOCATE('world', 'Hello world')
```
> The result of this query would be 7, because the substring "world" appears at position 7 within the string "Hello world".
You can also use the LOCATE() function in conjunction with other SQL functions, such as SUBSTRING(), to extract parts of a string based on the position of a substring.
---
**AWS:**
> In AWS Athena, the equivalent function to the LOCATE() function in SQL is the POSITION() function. The syntax of the POSITION() function is similar to that of LOCATE(), but with some differences.
The syntax of the POSITION() function in Athena is:
```sql
POSITION(substring IN string)
```
> Here, substring is the substring that you want to search for, and string is the string that you want to search within.
The function returns an integer value that represents the position of the first occurrence of the substring within the string. If the substring is not found within the string, the function returns 0.
For example, consider the following query:
```sql
SELECT POSITION('world' IN 'Hello world')
```
> The result of this query would be 7, because the substring "world" appears at position 7 within the string "Hello world".
Note that unlike the LOCATE() function in SQL, the POSITION() function in Athena does not support an optional third argument to specify the starting position of the search. If you need to start the search at a specific position, you can use the SUBSTR() function to extract a substring of the original string starting at the desired position, and then apply the POSITION() function to the extracted substring.
[Back to Top](#top)
### AWS > Position Function:
```sql
SELECT
  CASE 
    WHEN POSITION(UPPER(TRIM(gf.GEO_HIER_STRING)) IN UPPER(TRIM(g.GEO_HIER_STRING))) = 1 
    THEN 1 
    ELSE 0 
  END AS "TEU Confirmed Total"
FROM
  table_name gf
  INNER JOIN table_name g ON gf.column_name = g.column_name
```
### AWS > SUBSTR and LENGTH :
```sql
SELECT 
  geo_string, 
  teu_allocation,
  CASE 
    WHEN LENGTH(geo_string) = 1 THEN 
      SUM(CASE WHEN LENGTH(geo_string) = 3 THEN teu_allocation ELSE 0 END) OVER (PARTITION BY SUBSTR(geo_string, 1, 1), dpvoyage, allocation_scope, relation)
    ELSE 
      NULL 
  END AS sum_teu_allocation
FROM my_table;
```
[Back to Top](#top)
### Convert QVD to Parquet:
```bash
pip install qreader pyarrow
```
> This code will first read the QVD file into a DataFrame using the qreader package, then write the DataFrame to a CSV file. After that, it reads the CSV file into a DataFrame and writes the DataFrame to a Parquet file using the pyarrow engine.
Please note that this approach requires enough memory to read the entire QVD file into a DataFrame. If memory is a concern, you may need to split the QVD file into smaller parts using QlikView or Qlik Sense, then convert each part to a CSV file and subsequently to a Parquet file. Once you have the data in Parquet format, you can read it in chunks using Pandas, as shown in my previous response.
```py
import pandas as pd
import qreader
# Set your input file path, output CSV file path, and output Parquet file path
input_qvd_file = r"\\fs-bi-user\FS_User\Shared_Files_User\BA\Shipment\fact_ms_shp_cargo_revenue_combined.qvd"
output_csv_file = r"\\fs-bi-user\FS_User\Shared_Files_User\BA\Shipment\fact_ms_shp_cargo_revenue_combined.csv"
output_parquet_file = r"\\fs-bi-user\FS_User\Shared_Files_User\BA\Shipment\fact_ms_shp_cargo_revenue_combined.parquet"
# Read the QVD file into a DataFrame
df = qreader.read(input_qvd_file)
# Write the DataFrame to a CSV file
df.to_csv(output_csv_file, index=False)
# Read the CSV file into a DataFrame
df_csv = pd.read_csv(output_csv_file)
# Write the DataFrame to a Parquet file
df_csv.to_parquet(output_parquet_file, index=False, engine='pyarrow')
```
[Back to Top](#top)
**Below is another one using Chuck:**
```py
import pandas as pd
# Set your file path and chunk size
file_path = r"\\fs-bi-user\FS_User\Shared_Files_User\BA\Shipment\fact_ms_shp_cargo_revenue_combined.parquet"
chunksize = 1000  # Choose an appropriate chunk size
# Initialize an empty DataFrame to store the combined data
combined_df = pd.DataFrame()
# Read the Parquet file in chunks and concatenate them into the combined_df DataFrame
for chunk in pd.read_parquet(file_path, engine="pyarrow", chunksize=chunksize):
    combined_df = pd.concat([combined_df, chunk])
```
[Back to Top](#top)
### Benefits of Parquet file:
> Parquet is a file format designed for efficient columnar storage and processing of data. Here are some key points to know about Parquet:

- Parquet stores data in a columnar format, which means that all values of a particular column are stored together, making it easier and faster to read and process specific columns of data.
- Parquet uses compression algorithms to reduce file size, making it easier to transfer and store large amounts of data.
- Parquet is an open-source format that is widely used in big data processing frameworks like Apache Hadoop, Apache Spark, and Apache Arrow.
- Some of the benefits of using Parquet include improved query performance, lower storage costs, and better compatibility with distributed systems.

In general, if you have large amounts of data that you need to store and process efficiently, converting it to the Parquet format can be a good option. The columnar storage and compression features of Parquet make it particularly well-suited for big data applications.
[Back to Top](#top)
### Pandas > Read Large Parquet files:
```py
import pandas as pd
import pyarrow.parquet as pq
file_path = 'your_large_parquet_file.parquet'
# Get the number of row groups in the Parquet file
parquet_file = pq.ParquetFile(file_path)
n_row_groups = parquet_file.num_row_groups
# Read and process the Parquet file one row group at a time
for row_group_idx in range(n_row_groups):
    # Read a single row group
    table = parquet_file.read_row_group(row_group_idx)
    
    # Convert the Arrow Table to a Pandas DataFrame
    df_chunk = table.to_pandas()
    # Perform your operations on the chunk, e.g., filtering, aggregation, etc.
    print(df_chunk.head())
```
> Given that you have multiple large Parquet files, you can use the glob library to find all the matching file names and then read them one by one using the pyarrow.parquet library, as shown in the previous example. To optimize memory usage, you can perform your processing operations on each file individually and then concatenate the results.
Here's the code to read and process multiple large Parquet files:
```py
import glob
import pandas as pd
import pyarrow.parquet as pq
# Find all the matching Parquet files
file_pattern = 'sales_chun*.parquet'
file_list = glob.glob(file_pattern)
# Initialize an empty list to store the results
results = []
# Read and process each Parquet file
for file_path in file_list:
    # Get the number of row groups in the Parquet file
    parquet_file = pq.ParquetFile(file_path)
    n_row_groups = parquet_file.num_row_groups
    
    # Read and process the Parquet file one row group at a time
    for row_group_idx in range(n_row_groups):
        # Read a single row group
        table = parquet_file.read_row_group(row_group_idx)
        
        # Convert the Arrow Table to a Pandas DataFrame
        df_chunk = table.to_pandas()
        # Perform your operations on the chunk, e.g., filtering, aggregation, etc.
        # For example, let's filter the data based on a condition
        filtered_chunk = df_chunk[df_chunk['column_name'] > some_value]
        # Append the filtered_chunk to the results list
        results.append(filtered_chunk)

# Concatenate the results into a single Pandas DataFrame
result_df = pd.concat(results, ignore_index=True)
```
> Replace 'column_name' with the appropriate column name and some_value with the desired value for your filtering condition. You can also replace the filtering operation with other operations such as aggregation or transformation.
Keep in mind that this approach reads and processes each row group individually, which can help with memory management. However, the final DataFrame, result_df, will still hold the concatenated results in memory. If the result is too large to fit in memory, you may need to perform your operations in a more incremental manner or use out-of-core processing techniques such as Dask.
---
> If you want to process large Parquet files in a more incremental manner or use out-of-core processing techniques, Dask is a great option. Dask is a parallel computing library that integrates well with Pandas and can handle large datasets that don't fit in memory.
Here's how you can read and process multiple large Parquet files using Dask:
```sh
pip install dask[delayed] dask[dataframe] dask-ml
```
```py
import dask.dataframe as dd
import glob
# Find all the matching Parquet files
file_pattern = 'sales_chun*.parquet'
file_list = glob.glob(file_pattern)
# Read the Parquet files using Dask
ddf = dd.read_parquet(file_list, engine='auto')
# Perform operations on the Dask DataFrame (similar to Pandas DataFrame)
# For example, let's filter the data based on a condition
filtered_ddf = ddf[ddf['column_name'] > some_value]
# Alternatively, you can perform other operations such as aggregation
# result = ddf.groupby('column_name').mean()
# Compute the result and convert it to a Pandas DataFrame
result_pd = filtered_ddf.compute()
print(result_pd.head())
```
> Replace 'column_name' with the appropriate column name and some_value with the desired value for your filtering condition. You can also replace the filtering operation with other operations such as aggregation or transformation.
Dask will read and process the data in parallel, which can be more efficient than processing the data in chunks with Pandas. Moreover, Dask can handle larger-than-memory datasets, allowing you to work with the data without running out of memory.
Keep in mind that the final result, result_pd, will still hold the computed data in memory as a Pandas DataFrame. If the result is too large to fit in memory, you can perform incremental writes to disk, use Dask's out-of-core capabilities, or scale your Dask processing to a cluster.
---
> If you need to read the entire content of multiple large Parquet files and concatenate them into a single Dask DataFrame, you can follow these steps:
```sh
$pip install dask[delayed] dask[dataframe] dask-ml
```
```py
import dask.dataframe as dd
import glob
# Find all the matching Parquet files
file_pattern = 'sales_chun*.parquet'
file_list = glob.glob(file_pattern)
# Read the Parquet files using Dask
ddf = dd.read_parquet(file_list, engine='auto')
# Perform any operations you need on the Dask DataFrame, if required
# For example: result_ddf = ddf.groupby('column_name').mean()
# If you don't need to perform any operations, you can skip the above step
result_ddf = ddf
# Compute the result and convert it to a Pandas DataFrame (if it fits in memory)
result_pd = result_ddf.compute()
print(result_pd.head())
```
> Keep in mind that the final result, result_pd, will still hold the computed data in memory as a Pandas DataFrame. If the result is too large to fit in memory, consider performing incremental writes to disk, using Dask's out-of-core capabilities, or scaling your Dask processing to a cluster.
---
> If you need to write the final DataFrame to disk, you can use Dask's to_parquet function:
```py
# Save the Dask DataFrame to a Parquet file (or multiple files, if the dataset is partitioned)
result_ddf.to_parquet('output_parquet_file.parquet', engine='auto')
```
> If you want to read multiple large Parquet files one by one and then combine them into a single Pandas DataFrame (assuming the combined data fits in memory), you can do the following:
```py
import pandas as pd
import glob
# Find all the matching Parquet files
file_pattern = 'sales_chun*.parquet'
file_list = glob.glob(file_pattern)
# Initialize an empty list to store DataFrames
dataframes = []
# Read and process each Parquet file
for file_path in file_list:
    # Read a single Parquet file
    df = pd.read_parquet(file_path, engine='auto')
    
    # Perform any operations on the DataFrame, if needed (e.g., filtering, aggregation)
    
    # Append the DataFrame to the list
    dataframes.append(df)
# Concatenate all the DataFrames into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)
```
> This code reads each Parquet file one by one and appends the resulting DataFrame to a list. Once all files are read, it concatenates them into a single Pandas DataFrame.
Keep in mind that this approach loads the entire combined data into memory as a single Pandas DataFrame. If the combined data is too large to fit in memory, you should consider using Dask for out-of-core processing or perform incremental writes to disk.
---
> Here's an example of how to read multiple large Parquet files one by one, store them in separate DataFrames (df1, df2, ...), and finally combine them into a single DataFrame:
```py
import pandas as pd
import glob
# Find all the matching Parquet files
file_pattern = 'sales_chun*.parquet'
file_list = glob.glob(file_pattern)
# Initialize a dictionary to store DataFrames
dataframes = {}
# Read and process each Parquet file
for i, file_path in enumerate(file_list):
    # Read a single Parquet file
    dataframes[f'df{i+1}'] = pd.read_parquet(file_path, engine='auto')
    # Perform any operations on the DataFrame, if needed (e.g., filtering, aggregation)
# Combine all DataFrames into a single DataFrame
combined_df = pd.concat(dataframes.values(), ignore_index=True)
```
> This code reads each Parquet file one by one and stores the resulting DataFrame in a dictionary with keys like df1, df2, etc. Once all files are read, it concatenates the DataFrames in the dictionary into a single Pandas DataFrame.
Keep in mind that this approach loads the entire combined data into memory as a single Pandas DataFrame. If the combined data is too large to fit in memory, you should consider using Dask for out-of-core processing or perform incremental writes to disk.
---
> To read each file into separate DataFrames (df1, df2, etc.), you can use the following code:
```py
import pandas as pd
import glob
# Find all the matching Parquet files
file_pattern = 'sales_chun*.parquet'
file_list = glob.glob(file_pattern)
# Initialize a dictionary to store DataFrames
dataframes = {}
# Read and process each Parquet file
for i, file_path in enumerate(file_list):
    # Read a single Parquet file
    dataframes[f'df{i+1}'] = pd.read_parquet(file_path, engine='auto')
    # Print column names
    print(f"Column names for {file_path}: {list(dataframes[f'df{i+1}'].columns)}")
# Combine all DataFrames into a single DataFrame
combined_df = pd.concat(dataframes.values(), ignore_index=True)
```
> This code reads each Parquet file one by one, stores the resulting DataFrame in a dictionary with keys like df1, df2, etc., and prints the column names for each file. Once all files are read, it concatenates the DataFrames in the dictionary into a single Pandas DataFrame.
Keep in mind that this approach loads the entire combined data into memory as a single Pandas DataFrame. If the combined data is too large to fit in memory, you should consider using Dask for out-of-core processing or perform incremental writes to disk.
---
[Back to Top](#top)
### SQL > Grant Access :
> Below will indicate all search of Microsoft SQL Server Access:
[Back to Top](#top)
### View Access :
> In Microsoft SQL Server, if you want a user to view the definition of a view but not modify it, you should grant them the VIEW DEFINITION permission on that specific view. This permission will allow the user to see the T-SQL code behind the view without being able to modify it.
Here's how you can grant this permission:
```sql
USE [YourDatabaseName];
GO
GRANT VIEW DEFINITION ON [dbo].[YourViewName] TO [UserName];
GO
```
> Replace [YourDatabaseName], [dbo].[YourViewName], and [UserName] with the appropriate names for your setup.
After running this, the user will be able to see the view definition using tools like SQL Server Management Studio but won't be able to modify the view.
---
> If you want to grant the VIEW DEFINITION permission to a user for all views in a database, you can do so by granting the permission on the entire database. However, note that this will also allow the user to see the definition of other objects like stored procedures, functions, etc.
Here's how you can grant VIEW DEFINITION for all objects in the database:
```sql
USE [YourDatabaseName];
GO
GRANT VIEW DEFINITION ON DATABASE::[YourDatabaseName] TO [UserName];
GO
```
> Replace [YourDatabaseName] and [UserName] with the appropriate names for your setup.

If you only want to grant permission for all views and not other objects, you'll need to script this out using a loop or cursor for each view in the database. Here's a basic example using a cursor:
```sql
USE [YourDatabaseName];
GO
DECLARE @ViewName NVARCHAR(500)
DECLARE view_cursor CURSOR FOR 
SELECT '[' + TABLE_SCHEMA + '].[' + TABLE_NAME + ']' 
FROM INFORMATION_SCHEMA.VIEWS
OPEN view_cursor
FETCH NEXT FROM view_cursor INTO @ViewName
WHILE @@FETCH_STATUS = 0
BEGIN
    EXEC('GRANT VIEW DEFINITION ON ' + @ViewName + ' TO [UserName]')
    FETCH NEXT FROM view_cursor INTO @ViewName
END
CLOSE view_cursor
DEALLOCATE view_cursor
GO
```
> Replace [YourDatabaseName] and [UserName] with the appropriate values for your setup. This script will grant VIEW DEFINITION permission for each view in the database to the specified user.
### Revoke View Access:
> If you mistakenly granted VIEW DEFINITION on the entire database and wish to revoke it, you can use the REVOKE statement.
Here's how you can revoke the VIEW DEFINITION permission for the entire database:
```sql
USE [YourDatabaseName];
GO
REVOKE VIEW DEFINITION ON DATABASE::[YourDatabaseName] FROM [UserName];
GO
```
> Replace [YourDatabaseName] and [UserName] with the appropriate names for your setup.
This will remove the VIEW DEFINITION permission for the user on all objects in the database. If there were any specific objects (like certain views or tables) where the user had VIEW DEFINITION permission granted individually, those permissions would remain. If you want to ensure the user doesn't have VIEW DEFINITION on any object in the database, you'd have to revoke it for each object separately.
[Back to Top](#top)
### Grant Execute Procedure:
> To allow a user to execute the stored procedure without giving them broader access, you'll want to grant them explicit EXECUTE permissions on the procedure. This way, the user can run the procedure and it will execute with the permissions of the procedure's owner (in this case, presumably t_board_db or whichever user created the procedure). This concept is called "ownership chaining".
Here's how you can do this:

1. Create the User:
First, if you haven't created the new user yet, create the user in the database.
```sql
CREATE USER [UserName] WITHOUT LOGIN;
```
2. Grant Execute Permission:
Grant this new user permission to execute the stored procedure.
```sql
GRANT EXECUTE ON [dbo].[PowerBI_CL_Daily] TO [UserName];
```
3. Ensure SQL Server Agent Permissions:
Your procedure calls a job using msdb.dbo.sp_start_job. The user will need permission to execute this. 
Generally, the SQL Server Agent roles can be used.
```sql
USE [msdb];
EXEC sp_addrolemember N'SQLAgentUserRole', N'UserName'; 
```
> The SQLAgentUserRole is the least privileged of the SQL Server Agent fixed database roles. It allows members to execute and view their own jobs. If you have other security requirements, you might need to adjust the role membership or set up specific permissions.
NOTE: When creating roles and users, always check your current setup and permissions, to ensure there's no unintended access or security lapses.
---
> Explained Above access :
granting permissions to a new user won't impact the rights or permissions of the t_board_db admin user or any other users. The t_board_db user, if it's an admin or has a high privilege level, will retain all its permissions and capabilities.
In the steps I provided:
1. Creating a new user - This action only adds a user; it doesn't modify or impact existing users.
2. Granting Execute Permission - This only gives the new user the ability to execute the specific stored procedure [dbo].[PowerBI_CL_Daily]. It doesn't change anything for other users or for the t_board_db user.
3. SQL Server Agent Permissions - By giving the new user the SQLAgentUserRole role in the msdb database, you're just enabling them to start SQL Agent jobs that they own. This won't change the rights or permissions of the t_board_db user or any other existing users.

> The key principle in SQL Server security (and in most database platforms) is that granting permissions to one user doesn't reduce or change the permissions of another user. Each user's permissions are managed independently.
However, always be cautious and test any changes in a development or staging environment before applying them to production, just to ensure there are no unexpected behaviors or issues.
---
> If the job behind the stored procedure executes a CMD command (i.e., it's a CmdExec job step type in SQL Server Agent), there are a few additional considerations:
1. Proxy Account: CmdExec job steps run under the context of the SQL Server Agent Service Account, unless a proxy account has been defined. A proxy account allows SQL Server Agent to execute the job step under a different Windows account.
If you want to keep using the Service Account for this, ensure the SQL Server Agent service account has the necessary permissions to execute the CMD command.
If you need a different security context, you'll need to create a proxy account. You'll then assign the necessary permissions to this proxy and ensure the CmdExec job step uses this proxy.
2. Grant Permission to use Proxy (if used): If you are using a proxy account for the CmdExec step, ensure that your new user has permissions to use that proxy.
```sql
USE msdb;
EXEC sp_grant_proxy_to_subsystem @proxy_name=N'YourProxyName', @subsystem_id=3; -- 3 is for CmdExec
EXEC sp_grant_login_to_proxy @proxy_name=N'YourProxyName', @login_name=N'UserName';
```
3. Security Risks: Running CMD commands through SQL Server Agent introduces security risks, as it can expose the system to potential vulnerabilities. Ensure that the commands being run are safe, sanitized, and cannot be tampered with. Avoid constructing CMD commands using string concatenation from untrusted sources.
4. Permissions: The account (either the SQL Server Agent Service Account or the proxy account) needs to have permissions on the OS level to execute the desired CMD commands. You might need to work with your system administrator to ensure these permissions are correctly set.

> In conclusion, if your job is executing a CMD command, it's crucial to understand and validate the security context under which it's running and ensure that only trusted, authenticated users can initiate such jobs. It's also essential to audit and limit what the CMD command can do to prevent potential security risks.
---
[Back to Top](#top)
### Grant Execute Procedure and remove other users:
> To ensure that a new SQL Server user has access to run only the procedure [dbo].[PowerBI_CL_Daily] and nothing else, you'll need to do the following steps:
1. Create a new login for the user.
2. Create a new user based on the login.
3. Grant execute permissions on the procedure to the user.
> Here's how you can do it:
1. Create a new login:
```sql
USE [master]
GO
CREATE LOGIN [YourNewLoginName] WITH PASSWORD = 'YourStrongPasswordHere';
GO
```
2. Create a new user for your database:
```sql
USE [YourDatabaseName]
GO
CREATE USER [YourNewUserName] FOR LOGIN [YourNewLoginName];
GO
```
3. Grant execute permissions on the procedure to the new user:
```sql
USE [YourDatabaseName]
GO
GRANT EXECUTE ON [dbo].[PowerBI_CL_Daily] TO [YourNewUserName];
GO
```
> This will ensure that the new user can only execute the procedure and nothing else. But keep in mind:
The procedure itself accesses the msdb database and the job SP_PowerBI_Daily_Board. So, the user needs the required permissions to start that job. If you want to limit the user's permissions further, you may need to grant the user role membership in SQLAgentUserRole in the msdb database which allows starting jobs owned by that user. But this has other implications so be careful.
The procedure also reads from [sta].[T_FACT_CL_Daily_TXT], so the user will need at least SELECT permission on that table.
You can handle the above by either granting the permissions directly or by encapsulating all required operations in the stored procedure and making sure the stored procedure runs with elevated permissions using WITH EXECUTE AS clause.
Be careful while granting permissions, especially on system databases like msdb. Ensure you fully understand the implications of each permission you grant.
---
> If you want to ensure the user has the necessary permissions to execute the job and also read from the specified table, but nothing more, you'll need to handle the permissions at various levels.
1. Give user role membership in SQLAgentUserRole in the msdb database:
This role will allow your user to start jobs that they own.
```sql
USE [msdb]
GO
EXEC sp_addrolemember N'SQLAgentUserRole', N'YourNewUserName';
GO
```
> To be able to execute the job, the job SP_PowerBI_Daily_Board should be owned by YourNewUserName or a way to execute as a different user should be established.
2. Grant SELECT permission on the required table:
```sql
USE [YourDatabaseName]
GO
GRANT SELECT ON [sta].[T_FACT_CL_Daily_TXT] TO [YourNewUserName];
GO
```
3. Ensure the Job Ownership:
If you want this user to have the ability to run the job, you might want to ensure the job SP_PowerBI_Daily_Board is owned by the YourNewUserName. You can do this via the SQL Server Agent Jobs settings in SQL Server Management Studio or use T-SQL to change the owner.
Note: Changing the owner of the job might have other implications depending on how the job is currently configured and used. Ensure you understand those implications before making changes.
4. Additional Restrictions:
You might want to ensure this user cannot create new jobs, schedules, etc. within the SQL Agent. The SQLAgentUserRole role is limited, but you should validate that the user can only do what's intended. Test thoroughly by logging in as the user and attempting various operations.
> With these permissions in place, your new user should be able to execute the procedure, which in turn will start the job and query the table, but won't be able to do much else.
> Always be careful when assigning permissions, and ensure you've restricted access adequately to meet security requirements.
---
> The @database_user_name parameter is not for sp_add_jobserver, but rather for sp_add_jobstep.
> 
> To give permissions to the specific user for running a SQL Agent Job, you can follow these steps:
1. Ensure the user is a member of the SQLAgentUserRole in the msdb database:
This allows the user to start and stop jobs they own.
```sql
USE [msdb]
GO
EXEC sp_addrolemember N'SQLAgentUserRole', N'YourNewUserName';
GO
```
2. Change the ownership of the job:
Make sure that SP_PowerBI_Daily_Board is owned by YourNewUserName.
```sql
USE [msdb]
GO
EXEC sp_update_job
@job_name = N'SP_PowerBI_Daily_Board',
@owner_login_name = N'YourNewLoginName';
GO
```
> This should give your new user the permission to run the SP_PowerBI_Daily_Board job.
Additionally, make sure you've already provided the necessary permissions as mentioned in the previous steps (execute permission on the stored procedure and select permission on the table).
---
> To run a SQL Agent Job step that uses the CmdExec job step type. For security reasons, SQL Server doesn't allow non-SysAdmins to run CmdExec steps directly, as these can execute arbitrary operating system commands.
To address this, you can set up a proxy account and associate it with a credential that has the necessary permissions. Here are the steps:
1. Create a Credential:
A credential consists of the Windows username and password which will be used to run the CmdExec job steps.
```sql
USE [master]
GO
CREATE CREDENTIAL [YourCredentialName] 
WITH IDENTITY = 'Domain\WindowsUsername', 
SECRET = 'WindowsPassword';
GO
```
> Replace 'Domain\WindowsUsername' with the Windows account you want to use and 'WindowsPassword' with the password for that account. This Windows account should have the necessary permissions to execute whatever the CmdExec step is trying to do.
2. Create a Proxy:
Once you've created a credential, you can then create a proxy that uses this credential.
```sql
USE [msdb]
GO
EXEC sp_add_proxy 
@proxy_name = N'YourProxyName', 
@credential_name = N'YourCredentialName', 
@enabled = 1;
GO
```
3. Associate the Proxy with CmdExec:
After creating the proxy, you need to associate it with the subsystem (CmdExec in this case).
```sql
USE [msdb]
GO
EXEC sp_grant_proxy_to_subsystem 
@proxy_name = N'YourProxyName', 
@subsystem_id = 3;  -- 3 is for CmdExec
GO
```
4. Grant the necessary SQL Server user the ability to use the proxy:
```sql
USE [msdb]
GO
EXEC sp_grant_login_to_proxy 
@login_name = N'YourNewLoginName', 
@proxy_name = N'YourProxyName';
GO
```
5. Modify the SQL Agent Job step:
Finally, modify the job step to use the proxy. You can do this via SQL Server Management Studio:
    - Navigate to the SQL Server Agent -> Jobs -> Your Job -> Steps.
    - Edit the step that's failing.
    - In the "Run as" drop-down, select your proxy.
    - Save changes.
> You should now be able to run the job step as a non-SysAdmin user. Always ensure you are following security best practices when setting up credentials and proxies.
> [Back to Top](#top)
### Back The User Admin works again:
> Given the specific error message you received about the CmdExec step, and the changes you made, I'd suggest the following steps to correct the issue:
1. Revert Job Owner to Original:
If you know the original owner of the SP_PowerBI_Daily_Board job, revert back to that owner.
```sql
USE [msdb]
GO
EXEC sp_update_job
@job_name = N'SP_PowerBI_Daily_Board',
@owner_login_name = N'OriginalOwnerLoginName';
GO
```
> Replace OriginalOwnerLoginName with the login name of the original owner.
2. Remove from SQLAgentUserRole:
Given that you added PowerBI_HQ to the SQLAgentUserRole, but the job now no longer belongs to them, remove the user from this role to ensure there's no unintended elevation of permissions:
```sql
USE [msdb]
GO
EXEC sp_droprolemember N'SQLAgentUserRole', N'PowerBI_HQ';
GO
```
3. Revoke unnecessary permissions:
Revoke any excessive permissions you might have granted:
```sql
USE msdb;
REVOKE EXECUTE ON OBJECT::dbo.sp_start_job FROM PowerBI_HQ;
REVOKE SELECT ON OBJECT::dbo.sysjobs FROM PowerBI_HQ;
REVOKE SELECT ON OBJECT::dbo.sysjobactivity FROM PowerBI_HQ;
```
4. Drop the unnecessary role:
```sql
USE msdb;
GO
DROP ROLE db_jobexecutor;
GO
```
5. Reconfigure Proxy:
If the job still fails because it requires CmdExec steps to be run, and the original owner isn't a SysAdmin, you'll need to set up a proxy as described in the previous steps.
6. Validate other Permissions:
Ensure that the user PowerBI_HQ still has the necessary permissions to execute the stored procedure and query the desired tables.
> Remember, permissions in SQL Server can be a bit intricate, especially when involving SQL Server Agent jobs. It's crucial to periodically review and understand the exact permissions required for specific tasks to avoid potential security vulnerabilities. Always test in a development environment before applying to production.
[Back to Top](#top)
### allow PowerBI_HQ to only execute the job:
> You want to retain all permissions for t_board_db and only give PowerBI_HQ the permission to execute that specific job.
>
> If you want to allow PowerBI_HQ to only execute the job without the ability to perform other tasks, the best approach is using a combination of database roles and proxies.
> Follow these steps:
1. Ensure PowerBI_HQ has the necessary role in msdb:
The SQLAgentUserRole in the msdb database will give the user permission to run jobs they own, but we can't change the job ownership here. We'll handle execution differently.
```sql
USE [msdb]
GO
EXEC sp_addrolemember N'SQLAgentUserRole', N'PowerBI_HQ';
GO
```
2. Set Up a Credential and Proxy for Job Execution:
If the job step requires elevated permissions or is of the type CmdExec, non-SysAdmin users won't be able to execute it directly. We'll create a credential and proxy to bypass this.
1. Create a Credential:
```sql
USE [master]
GO
CREATE CREDENTIAL JobExecCredential 
WITH IDENTITY = 'Domain\WindowsUsername', -- Windows account
SECRET = 'WindowsPassword';
GO
```
2. Create a Proxy Using the Credential:
```sql
USE [msdb]
GO

EXEC sp_add_proxy 
@proxy_name = N'JobExecProxy', 
@credential_name = N'JobExecCredential', 
@enabled = 1;
GO

EXEC sp_grant_proxy_to_subsystem 
@proxy_name = N'JobExecProxy', 
@subsystem_id = 3;  -- 3 is for CmdExec
GO

EXEC sp_grant_login_to_proxy 
@login_name = N'PowerBI_HQ', 
@proxy_name = N'JobExecProxy';
GO
```
3. Update the SQL Agent Job to Use the Proxy:
In SQL Server Management Studio:
    - Navigate to SQL Server Agent > Jobs > Your Job > Steps.
    - Edit the step(s) that require elevated permissions.
    - In the "Run as" drop-down, select JobExecProxy.
    - Save changes.
4. Grant PowerBI_HQ Execute on the Job:
The safest way to grant PowerBI_HQ execute permission on a specific job without changing its ownership is through a stored procedure that encapsulates the sp_start_job command. This way, you can avoid potential unwanted permissions that might come from directly granting rights to start jobs.
```sql
USE [msdb]
GO

CREATE PROCEDURE Start_SpecificJob_For_PowerBI_HQ
AS
BEGIN
    EXEC dbo.sp_start_job N'SP_PowerBI_Daily_Board';
END;
GO

GRANT EXECUTE ON Start_SpecificJob_For_PowerBI_HQ TO PowerBI_HQ;
GO
```
> Now, PowerBI_HQ can execute this stored procedure to start the job.
Remember to replace 'Domain\WindowsUsername' and 'WindowsPassword' with the correct Windows account details that have necessary permissions to run the job's steps.
This way, the user PowerBI_HQ will only be able to start the specific job and won't have other elevated permissions.
---
> The steps I provided are designed to add permissions for PowerBI_HQ without affecting the existing permissions or functionality of the t_board_db user or other aspects of your system.
> To clarify:
1. SQLAgentUserRole for PowerBI_HQ: This action only grants PowerBI_HQ certain permissions related to SQL Agent jobs. It doesn't impact any other users or their permissions.
2. Credential and Proxy Creation: This action just establishes a way for non-SysAdmin users (like PowerBI_HQ) to run specific job types that would normally require elevated permissions. Creating these doesn't change or override the way jobs are currently run by t_board_db or any other users.
3. Updating the SQL Agent Job to Use Proxy: This is necessary only if the job has steps that a non-SysAdmin user can't normally run (like CmdExec steps). If t_board_db is an admin user, it will still be able to run the job without any issues even with this change. The proxy just provides an avenue for users like PowerBI_HQ to run it.
4. Stored Procedure for PowerBI_HQ: The specific stored procedure is just a wrapper around the sp_start_job system procedure. It doesn't change how the job is run, just how it's initiated. t_board_db can still run jobs directly or through any other existing mechanisms.
> That said, it's always a good practice to:
>
> Backup: Before making any changes, especially related to permissions or configurations, ensure you have recent backups of your SQL Server system and databases.
Test: If possible, test these changes in a development or staging environment before applying them to your production system.
Monitor: After applying changes, monitor the system to ensure that everything is functioning as expected and there are no unexpected side effects.
Always take care with permissions and configurations in SQL Server to ensure system security and integrity.
[Back to Top](#top)
### Restoring t_board_db to its original state:
> If t_board_db is not visible under the users of msdb anymore, it's possible it was inadvertently dropped or its permissions were altered. Let's work on restoring t_board_db to its original state and ensuring that it remains an admin for that SQL Server.
1. First, verify if t_board_db still exists as a login:
```sql
USE [master]
GO
SELECT * FROM sys.server_principals WHERE name = 't_board_db';
```
> If this returns a result, then the login still exists, and we just need to map it to msdb and other necessary databases. If it doesn't return a result, we need to recreate the login.
2. If you need to recreate the t_board_db login (only do this if the above query did not return any results):
```sql
USE [master]
GO
CREATE LOGIN [t_board_db] WITH PASSWORD=N'YourPasswordHere', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF;
GO
```
> Replace 'YourPasswordHere' with the appropriate password.
3. Map the t_board_db login to the msdb database:
```sql
USE [msdb]
GO
CREATE USER [t_board_db] FOR LOGIN [t_board_db];
```
4. If t_board_db should have admin rights on the SQL Server instance, you should add it to the sysadmin server role:
```sql
USE [master]
GO
EXEC sp_addsrvrolemember 't_board_db', 'sysadmin';
```
5. Clean up PowerBI_HQ:
If you want to undo the changes made to PowerBI_HQ, you can revoke the permissions and remove it from the roles:
```sql
USE [msdb]
GO
REVOKE EXECUTE ON OBJECT::dbo.sp_start_job FROM PowerBI_HQ;
EXEC sp_droprolemember N'SQLAgentUserRole', N'PowerBI_HQ';
DROP USER PowerBI_HQ;
```
6. Finally, always ensure that after making changes to permissions, you:
    - Check application connectivity and functionality to ensure nothing is disrupted.
    - Review SQL Server logs for any errors or warnings related to permissions or login issues.
    - Regularly backup SQL Server logins and permissions as a part of your disaster recovery plan.
> By following these steps, you should be able to restore t_board_db to its administrative status and clean up the changes made to PowerBI_HQ.
---
> The sysadmin role is not a database role; it's a server-level role. Therefore, you won't see it under the "Database Roles" for any specific database, including msdb. Instead, you'll find it under "Server Roles" in the SQL Server Management Studio (SSMS) Object Explorer at the instance level.
The sp_addsrvrolemember stored procedure is used to add a login to a server-level role. The sysadmin role grants the highest level of privileges on the SQL Server instance, effectively giving administrative rights to the login on that SQL Server instance.
If t_board_db was previously an administrator of the SQL Server instance, and you want to restore that status, then you should run the command.
However, if you're not sure about the previous permissions for t_board_db, here's what you can do:
1. Check Existing Server Roles for t_board_db:
Before adding t_board_db to sysadmin, you can check which server roles it currently belongs to:
```sql
USE [master]
GO
EXEC sp_helpsrvrolemember @rolename = 'sysadmin';
```
> This will list all the members of the sysadmin role. If t_board_db is listed in the result, then it already has sysadmin rights. If it's not listed, and you're sure it needs to be an admin, then you can safely add it.
2. Add to sysadmin Role:
If you've determined that t_board_db should be in the sysadmin role, then you can proceed with the command:
```sql
USE [master]
GO
EXEC sp_addsrvrolemember 't_board_db', 'sysadmin';
```
> However, if you're uncertain or unsure, it's always a good practice to:
Consult: Speak with any other DBAs or admins or check documentation to confirm the intended permissions for t_board_db.
Backup: Ensure you have backups of your SQL Server and its configurations.
Caution: If you're ever in doubt about executing a command, especially one that can grant elevated permissions, it's better to hold off and seek clarity.
Always prioritize the security and integrity of your SQL Server environment.
[Back to Top](#top)
### YouTube Download 1080:
> When you want to download 1080p (or higher) videos using pytube, you need to understand that such resolutions often come in adaptive streams — where video and audio are separate.
To achieve this, you would need to:
1. Download the highest resolution video-only stream.
2. Download the highest quality audio stream.
3. Merge the two streams together.
> Here's how you can do that:
```py
import os
from pytube import YouTube
from pytube.cli import on_progress
from moviepy.editor import *
def download_highest_quality(youtube_url, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    yt = YouTube(youtube_url, on_progress_callback=on_progress)
    print("Fetching video details...")
    
    # Fetch the video-only and audio-only streams.
    video_stream = yt.streams.filter(only_video=True, file_extension='mp4').order_by("resolution").desc().first()
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    print(f"Downloading video stream: {video_stream.resolution}")
    video_filename = video_stream.download(output_path=destination_folder, filename="video_temp")
    audio_filename = audio_stream.download(output_path=destination_folder, filename="audio_temp")
    
    # Combining video and audio using moviepy
    video_clip = VideoFileClip(video_filename)
    audio_clip = AudioFileClip(audio_filename)
    final_clip = video_clip.set_audio(audio_clip)
    
    final_filename = os.path.join(destination_folder, yt.title.replace("/", "-") + ".mp4")
    final_clip.write_videofile(final_filename)
    
    # Remove temporary files
    os.remove(video_filename)
    os.remove(audio_filename)

    return f"Download Complete | Saved at {final_filename}"

if __name__ == "__main__":
    url = "https://youtu.be/At5alroIsic"
    dest = "./00_downloaded"
    result = download_highest_quality(url, dest)
    print(result)
```
> This should download the video in 1080p (or the highest available resolution) and merge it with the best available audio stream.
A few considerations:
Ensure you have ffmpeg installed on your machine, as moviepy relies on it for video processing tasks.
Always make sure you have the right to download and use the content from YouTube. Downloading videos can breach YouTube's terms of service.
---
> adjusted code that allows downloading multiple videos by looping through a list of URLs:
```py
import os
from pytube import YouTube
from pytube.cli import on_progress
from moviepy.editor import *

def download_highest_quality(youtube_url, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    yt = YouTube(youtube_url, on_progress_callback=on_progress)
    print(f"Fetching details for {yt.title}...")
    
    # Fetch the video-only and audio-only streams.
    video_stream = yt.streams.filter(only_video=True, file_extension='mp4').order_by("resolution").desc().first()
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    print(f"Downloading video stream: {video_stream.resolution}")
    video_filename = video_stream.download(output_path=destination_folder, filename="video_temp")
    audio_filename = audio_stream.download(output_path=destination_folder, filename="audio_temp")
    
    # Combining video and audio using moviepy
    video_clip = VideoFileClip(video_filename)
    audio_clip = AudioFileClip(audio_filename)
    final_clip = video_clip.set_audio(audio_clip)
    
    final_filename = os.path.join(destination_folder, yt.title.replace("/", "-") + ".mp4")
    final_clip.write_videofile(final_filename)
    
    # Remove temporary files
    os.remove(video_filename)
    os.remove(audio_filename)

    return f"Download Complete | Saved at {final_filename}"

if __name__ == "__main__":
    urls = [
        "https://youtu.be/GHtX0QXfi6g",
        "https://youtu.be/At5alroIsic",  # Add more URLs as needed
    ]
    dest = "./00_downloaded"

    for url in urls:
        result = download_highest_quality(url, dest)
        print(result)
```
> I've converted the url variable into a list called urls which contains all the video links you want to download. The program will loop through each URL and download the videos sequentially.
Just keep adding the YouTube URLs you want to download to the urls list, and the script will handle the rest!
[Back to Top](#top)
### YouTube Download 720:
```py
import os
import ssl
from pytube import YouTube
from pytube.cli import on_progress

def download_highest_quality(youtube_url, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    yt = YouTube(youtube_url, on_progress_callback=on_progress)

    try:
        print("Fetching video details...")
        video_stream = sorted(yt.streams.filter(progressive=True, file_extension='mp4'), key=lambda s: s.resolution, reverse=True)[0]
        print(f"Downloading video: {yt.title} | Resolution: {video_stream.resolution}")
        video_stream.download(output_path=destination_folder)
    except Exception as e:
        return f"ERROR | {e}"

    return f"Download Complete | Saved at {destination_folder}"

if __name__ == "__main__":
    url = "https://youtu.be/At5alroIsic"
    dest = "./00_downloaded"
    result = download_highest_quality(url, dest)
    print(result)
```
[Back to Top](#top)
### Setup environment variables in VSCode:
> 1. set up environment variables in VSCode and then retrieve those variables in your Python code.
>
> Set Up Environment Variables in VSCode:
1. Install the Python Extension in VSCode: If you haven't already, install the Python extension from the VSCode marketplace.
2. Create an .env File: In the root of your project directory, create a file named .env. This is where you'll store your environment variables.
For instance:
```Makefile
DB_USER=myUsername
DB_PASS=myPassword
```
3. Update settings.json: Ensure that the Python extension in VSCode knows to use the .env file. Click on the gear icon (⚙️) in the lower left-hand corner > Settings or simply press Ctrl + ,. In the top-right corner of the settings tab, click on the {} icon to open the settings.json file. Add or update the following lines:
```json
"python.envFile": "${workspaceFolder}/.env",
```
> 2. Retrieve the Credentials in Your Python Code:
1. Install the python-dotenv Library: Use pip to install the python-dotenv library which allows you to easily load environment variables from an .env file:
```bash
pip install python-dotenv
```
2. Use the Credentials in Python:
```py
import os
from dotenv import load_dotenv

load_dotenv()  # This will load environment variables from .env file
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
# Now you can use DB_USER and DB_PASS in your SQL connection code
```
> Important Notes:
1. Keep your .env file secure: Do not commit the .env file to your version control system (like Git). Instead, add .env to your .gitignore file to ensure it doesn't get accidentally committed.
2. Environment variables are generally in ALL CAPS: This is a convention to make them easily distinguishable from regular variables.
3. Setting Environment Variables Directly: The above method is specific to VSCode's development environment. In a production setting, you'd usually set environment variables directly on your server or hosting platform.
> Now, your Python script can access the database credentials without them being hardcoded, making your code more secure and modular!
[Back to Top](#top)
### Multiple projects within the same workspace in VSCode :
> multiple projects within the same workspace in VSCode and each project has its own set of credentials, you can handle them by creating separate .env files for each project. Here's how to set it up:
1. Organize Your Workspace:
Ensure each project is in a separate folder within the workspace. Your workspace directory structure might look something like this:
```lua
/workspace
|-- /project1
|   |-- .env
|   |-- main.py
|
|-- /project2
|   |-- .env
|   |-- main.py
|
| ... and so on
```
2. Create .env files:
Within each project folder, create a .env file containing the credentials specific to that project:
For /project1/.env:
```Makefile
DB_USER=user1
DB_PASS=pass1
```
For /project2/.env:
```makefile
DB_USER=user2
DB_PASS=pass2
```
3. Load Credentials in Python Scripts:
Within each Python script, use the same method to load the environment variables:
```py
import os
from dotenv import load_dotenv

load_dotenv()  # This will automatically load the .env file in the current directory

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
```
> When you run main.py within project1, it will use project1's .env file. Similarly, for project2, it'll use its respective .env.
4. Working with VSCode:
The Python extension for VSCode automatically detects the .env file in the directory of the currently opened file (i.e., if you open a file in project1, it uses the .env from project1). Ensure the setting "python.envFile": "${workspaceFolder}/.env" is set, as mentioned earlier. This allows for relative .env paths.
5. Remember .gitignore:
If you're using a version control system like Git, remember to add each .env file to the .gitignore to prevent accidentally sharing your credentials:
```bash
/project1/.env
/project2/.env
```
> Summary: With this setup, each project within your workspace will have its own set of credentials stored in a separate .env file. When you run or debug a project, it will automatically use the correct credentials for that specific project.
---
> The setting "python.envFile": "${workspaceFolder}/.env" in the settings.json file is a general setting for VSCode's Python extension, and it works with the current directory of the active Python file.
Here's what happens:
1. The placeholder ${workspaceFolder} refers to the root of the currently opened folder in VSCode.
2. When you open a Python file from a particular project (e.g., from project1), the context switches to that folder.
3. Therefore, ${workspaceFolder} dynamically adjusts based on the currently active Python file's location.
4. The Python extension then looks for an .env file in that location and loads it.
So, if you have multiple projects in the same workspace, each with its own .env file, VSCode will automatically load the appropriate .env file when you're working on a file from that project.
> You don't need to make any additional changes in the settings.json file for each individual project; the dynamic context-switching will handle it for you. Just make sure that each project has its own .env file with the necessary credentials.
[Back to Top](#top)
### General .env file that's shared across multiple projects:
> If you want a general .env file that's shared across multiple projects within the same workspace, you can certainly do that. This can be useful if there are some common configurations or settings that many of your projects use.
Here's how you can set it up:
1. Create a General .env File:
Place the general .env file at the root level of your workspace:
```lua
/workspace
|-- general.env
|-- /project1
|   |-- main.py
|
|-- /project2
|   |-- main.py
|
| ... and so on
```
2. Update the settings.json in VSCode:
Modify the settings.json to point to the general.env file:
```json
"python.envFile": "${workspaceFolder}/general.env",
```
3. Loading Variables in Python:
For projects that need the general environment variables, load them as you would normally:
```py
import os
from dotenv import load_dotenv

load_dotenv()  # This will automatically load the general.env file

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
```
> Important Considerations:
1. Overriding Values: If you also have project-specific .env files, and they contain variables with the same name as in the general .env file, you'll need to handle potential overriding of values. You could either load both .env files and ensure the correct order of loading, or avoid having overlapping variable names.
2. Organization: Using a general .env file is useful for shared configurations, but it's important to remember which projects depend on it. Ensure proper documentation so that future maintenance is straightforward.
3. Security: As always, don't commit sensitive information like database credentials. If your general.env contains such data, add it to .gitignore.
> By using a general .env file, you can centralize configurations that are shared across projects, making it easier to manage and update them as needed.
---
> If you have some projects that share common credentials (via a general .env file) and other projects that have their own specific credentials, you'll want to set it up in such a way that VSCode and your Python scripts know when to use the general .env and when to use the project-specific .env.
> Step-by-step Guide:
1. Setting Up .env Files:
a. Create a general.env at the root of your workspace for common credentials:
```bash
/workspace
|-- general.env     # Contains shared credentials
|-- /project1
|   |-- .env        # Contains specific credentials for project1 (if any)
|   |-- main.py
|
|-- /project2       # This project might use the shared credentials
|   |-- main.py
|
| ... and so on
```
> In general.env:
```makefile
DB_USER=sharedUser
DB_PASS=sharedPass
```
> In project1/.env (just an example if project1 has unique credentials):
```makefile
DB_USER=uniqueUser1
DB_PASS=uniquePass1
```
2. Modify settings.json in VSCode:
a. By default, make VSCode point to the general.env file:
```json
"python.envFile": "${workspaceFolder}/general.env",
```
> This means, whenever you run a Python file in VSCode and it doesn't find a project-specific .env, it will use the general.env.
b. For projects with their own specific credentials, you can override the default setting at a folder level. In VSCode, there's a concept of workspace settings where you can specify settings for individual folders within a workspace.
Here's how:
Open your workspace settings in VSCode.
In the settings editor, there's a section titled "Folder Settings" where you can select each folder and specify settings just for that folder.
For project1, you'd add:
```json
"python.envFile": "${workspaceFolder}/project1/.env",
```
> This tells VSCode to use the .env file specific to project1 when working on files within that project.
3. Loading Credentials in Python:
The method to load credentials in your Python scripts remains the same:
```py
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
```
> When you run the script:
If the script is in a project with its own .env, it will load that.
If the script is in a project without a specific .env, it will default to the general.env.
>
> Notes:
1. Ensure the .env files are correctly located in the project directories and the general.env at the workspace root.
2. As always, add .env and general.env to .gitignore to prevent committing sensitive information.
3. This method allows flexibility for future projects. If a new project uses shared credentials, it will automatically use general.env. If it needs unique credentials, just add a new .env within its folder.
By following this setup, you can maintain shared credentials in a central location while also accommodating projects with unique credential needs.
>
> You can add the "python.envFile": "${workspaceFolder}/.env", setting within the settings block in your workspace configuration. Here's how it would look with your provided configuration:
```json
{
	"folders": [
		{
			"path": "."
		}
	],
	"settings": {
		"terminal.integrated.profiles.linux": {

			"bash": {
				"path": "bash",
				"icon": "terminal-bash"
			},
			"zsh": {
				"path": "zsh"
			},
			"fish": {
				"path": "fish"
			},
			"tmux": {
				"path": "tmux",
				"icon": "terminal-tmux"
			},
			"pwsh": {
				"path": "pwsh",
				"icon": "terminal-powershell"
			}
		},
		"python.envFile": "${workspaceFolder}/general.env"
	}
}
```
> Here, I've added the "python.envFile": "${workspaceFolder}/general.env" setting within the settings block. It will specify that, by default, the Python extension should look for a general.env file at the root of your workspace to load environment variables.
[Back to Top](#top)
### Anaconda Commands:
1. List All Environments:
First, confirm that you indeed have environments with duplicate names.
Open the Anaconda prompt or terminal and run:
```bash
conda info --envs
```
2. Rename the Environments:
To avoid confusion, it's a good idea to rename these environments so each has a unique name.
Use the following command to rename an environment:
```bash
conda create --name new_name --clone old_name
```
3. remove the old environment with the duplicate name:
```bash
conda remove --name old_name --all
```
4. create clones with different names like:
```bash
conda create --name myenv1 --clone myenv
conda create --name myenv2 --clone myenv
```
5. remove the original:
```bash
conda remove --name myenv --all
```
6. delete a conda environment, you can use the following command:
```bash
conda env remove --name env_name
```
> Replace env_name with the name of the environment you want to delete. After running the command, the specified environment will be removed. Make sure you're not currently activated into the environment you're trying to delete. If you are, deactivate it first using:
```bash
conda deactivate
```
7. Creating a conda environment from a .yml file is a common practice to ensure reproducibility across different systems. Below are the steps and best practices for creating, structuring, and using a .yml file for a conda environment:

1. Create the .yml file: The file might be named environment.yml. Here's a basic structure:
```yaml
name: my_env_name
channels:
  - defaults
  - conda-forge
dependencies:
  - numpy=1.18.*
  - pandas=1.1.*
  - matplotlib>=3.3,<3.4
  - pip
  - pip:
    - some-pip-package==0.1.*
    - another-pip-package>=0.2,<0.3
```
2. Best Practices for Structuring .yml:
Name: Clearly name the environment. This is useful if you're sharing the environment with others.
Channels: Order channels from most specific at the top to least specific at the bottom. Often, conda-forge is a preferred channel due to its extensive package availability.
Dependencies:
Specify versions to ensure reproducibility. Use the * wildcard for patch versions.
Separate conda and pip dependencies. Include pip itself as a conda dependency.
For pip dependencies, use the pip: sub-list.
3. Create the Environment from the .yml file:
```bash
conda env create -f environment.yml
```
4. Ensuring Smooth Environment Creation:
Test Regularly: If you're making changes to the .yml file, test it frequently to ensure it still works.
Version Pinning: By specifying versions for each package, you help ensure that future changes or updates to packages won't break the environment setup. This aids in reproducibility.
Maintain Dependencies: Over time, some packages may become deprecated or may conflict with newer versions of other packages. Periodically check and update the .yml file as needed.
Activate the Environment: After creation, you can activate the environment using:
```bash
conda activate my_env_name
```
> Sharing: If you're sharing your .yml, ensure that any local paths or private channels are removed or documented so others can adjust as necessary.
> Lastly, remember that while these practices can reduce the likelihood of issues, the world of software has many moving parts. It's always possible for new conflicts to arise. Periodically reviewing and updating your .yml file can help mitigate potential problems.
[Back to Top](#top)
### Read file Names in Directory:
```py
import os

path = r'U:\RHH0T430 - REGION REPORTING\Review'
for filename in os.listdir(path):
    print(filename)
```
[Back to Top](#top)
### SQL > Delete from Table :
```sql
DELETE FROM [PlanX].[sta].[T_FACT_SAP_DailyFX_CSV]
WHERE RIGHT([DateFX], 8) = 'Mar-2023';
```
[Back to Top](#top)
### Qlikview Scripts:
> Below will indicate best practices of Qlikview scripts:
[Back to Top](#top)
### Loading Max File Name:
```csharp
// Create a temporary table to list all the filenames
TempFileList:
LOAD
    FileBaseName() as FileName
FROM
[00_Dataset_*.csv]
(txt, codepage is 28591, no labels, delimiter is ',', msq)
WHERE RecNo() = 1; // just load the first row of each file to speed up the process

// Determine the file with the maximum name
MaxFile:
LOAD
    MaxString(FileName) as MaxFileName
RESIDENT TempFileList;

// Store the maximum filename in a variable
LET vMaxFileName = Peek('MaxFileName', 0, 'MaxFile');

// Drop the temporary tables
DROP TABLE TempFileList;
DROP TABLE MaxFile;

// Now, load data only from the file with the maximum filename
Scheme_Table:
LOAD table_catalog, 
     table_schema, 
     table_name, 
     column_name, 
     ordinal_position, 
     column_default, 
     is_nullable, 
     data_type, 
     comment, 
     extra_info
FROM
[00_Dataset_$(vMaxFileName).csv]
(txt, codepage is 28591, embedded labels, delimiter is ',', msq);
```
[Back to Top](#top)
### Add Load:
> In QlikView script, the add load statement is used to load data from one or more data sources and add it to the existing data model. It allows you to append data to a table or create a new table in the QlikView data model.
Here is an example of how add load can be used in a QlikView script:
```csharp
// Load data from an Excel file and add it to the existing data model
add load *
from [C:\Data\sales.xlsx]
(ooxml, embedded labels, table is Sheet1);

// Load data from a SQL database and add it to the existing data model
add load *
from SalesData
where Year >= 2020;
```
> In the first example, the add load statement loads data from an Excel file located at C:\Data\sales.xlsx and appends it to the existing data model. The data is loaded from the Sheet1 tab of the Excel file, and the ooxml and embedded labels keywords are used to specify the file format and header row, respectively. The * wildcard character is used to load all columns from the Excel file.
In the second example, the add load statement loads data from a SQL database table called SalesData and appends it to the existing data model. The where clause is used to filter the data so that only records where the Year field is greater than or equal to 2020 are loaded.
Overall, add load is a useful statement in QlikView script for adding new data to an existing data model or appending data to an existing table.
 here's a more detailed example of how add load works in QlikView script:

Let's say you have a QlikView document with a table called SalesData that contains information about sales transactions, such as date, product, quantity, and price. The table looks like this:
|Date | Product | Quantity | Price|
|----|--------|--------|--------|
|01/01/2022 | Apples | 10 | 1.50|
|01/02/2022 | Oranges | 5 | 2.00|
|01/03/2022 | Apples | 20 | 1.50|
|01/04/2022 | Bananas | 15 | 0.75|
Now, let's say you have a new file called NewSalesData.csv that contains additional sales data that you want to add to the existing SalesData table. The file looks like this:
|Date | Product | Quantity | Price|
|----|--------|--------|--------|
|01/05/2022 | Apples | 5 | 1.50|
|01/06/2022 | Grapes | 8 | 3.00|
|01/07/2022 | Oranges | 10 | 2.00|
> To add this data to the SalesData table, you can use the add load statement in QlikView script:
```csharp
// Load the new sales data from the CSV file
NewSalesData:
LOAD *
FROM NewSalesData.csv
(txt, codepage is 1252, embedded labels, delimiter is ',', msq);

// Append the new sales data to the existing SalesData table
SalesData:
add load *
resident NewSalesData;

// Drop the temporary NewSalesData table
drop table NewSalesData;
```
In the first line of the script, we use the LOAD statement to load the data from the NewSalesData.csv file into a new table called NewSalesData.
Next, we use the add load statement to append the data from the NewSalesData table to the existing SalesData table. The resident keyword is used to specify that we want to append the data from the NewSalesData table to the SalesData table. The * wildcard character is used to select all columns from the NewSalesData table.
Finally, we use the drop table statement to remove the temporary NewSalesData table from the QlikView document.
After running this script, the SalesData table will be updated with the new sales data from the NewSalesData.csv file:
|Date | Product | Quantity | Price|
|----|--------|--------|--------|
|01/01/2022 | Apples | 10 | 1.50|
|01/02/2022 | Oranges | 5 | 2.00|
|01/03/2022 | Apples | 20 | 1.50|
|01/04/2022	| Bananas | 15 | 0.75|
|01/05/2022 | Apples | 5 | 1.50|
|01/06/2022 | Grapes | 8 | 3.00|
|01/07/2022 | Oranges | 10 | 2.00|

[Back to Top](#top)
### recno():
> the recno() function is used to return the number of the current record being loaded from a data source. It is a built-in function that can be used in load statements to create a field that contains the record number for each row of data.
Here's an example of how recno() can be used in a QlikView script:
```csharp
// Load data from a CSV file and add a record number field
MyData:
LOAD recno() as RecordNumber,
     *
FROM MyData.csv
(txt, codepage is 1252, embedded labels, delimiter is ',', msq);
```
In this example, we're loading data from a CSV file called MyData.csv and creating a field called RecordNumber using the recno() function. The LOAD statement specifies that we want to load all columns from the CSV file using the * wildcard character. The txt, codepage is 1252, embedded labels, delimiter is ',', and msq keywords are used to specify the format of the CSV file.
After running this script, the MyData table will contain a new field called RecordNumber that contains the record number for each row of data:
| RecordNumber | Field1  | Field2  | Field3  |
| :----------- | :------ | :------ | :------ |
| 1            | Value1  | Value2  | Value3  |
| 2            | Value4  | Value5  | Value6  |
| 3            | Value7  | Value8  | Value9  |
| 4            | Value10 | Value11 | Value12 |
> As you can see, the RecordNumber field contains the record number for each row of data, starting at 1 and incrementing by 1 for each row.
recno() can be useful in cases where you need to assign a unique identifier to each row of data in your QlikView data model, such as when you're merging multiple tables together or when you're performing calculations that require a unique row identifier.

[Back to Top](#top)
### Load Excel and Sheet dynamically:
> the code to skip files that do not contain a sheet with a matching name, you can add a check after defining the sheet name based on the file name. Here's the updated code:
```csharp
LET vFolderPath = '\\ww.hl.lan\hh1\Groups\RHH0T019\8220 LSC\Projects\2023\PFP\';
LET vFileExtension = '.xlsx';

// Load each file in the folder
FOR Each vFileName in FileList(vFolderPath & '*' & vFileExtension)
    // Extract the file name without the extension
    LET vBaseFileName = SubField('$(vFileName)', '\', -1);
    LET vBaseFileName = Left(vBaseFileName, Len(vBaseFileName) - Len(vFileExtension));
    
    // Define the sheet name based on the file name
    LET vSheetName = '';
    IF WildMatch('$(vBaseFileName)', '*RAS*') THEN
        LET vSheetName = 'RAS';
    ELSEIF WildMatch('$(vBaseFileName)', '*RLA*') THEN
        LET vSheetName = 'RLA';
    ELSEIF WildMatch('$(vBaseFileName)', '*RME*') THEN
        LET vSheetName = 'RME';
    ELSEIF WildMatch('$(vBaseFileName)', '*RNA*') THEN
        LET vSheetName = 'RNA';
    ELSEIF WildMatch('$(vBaseFileName)', '*RNE*') THEN
        LET vSheetName = 'RNE';
    ELSEIF WildMatch('$(vBaseFileName)', '*Tracking_Equipment*') THEN
        LET vSheetName = 'Equipment';
    ELSEIF WildMatch('$(vBaseFileName)', '*Tracking_Fleet*') THEN
        LET vSheetName = 'Fleet';
    ELSEIF WildMatch('$(vBaseFileName)', '*Tracking_Network*') THEN
        LET vSheetName = 'Network';
    ELSEIF WildMatch('$(vBaseFileName)', '*OvH*') THEN
        LET vSheetName = 'Overhead';
    ELSEIF WildMatch('$(vBaseFileName)', '*RSE*') THEN
        LET vSheetName = 'RSE';
    ELSEIF WildMatch('$(vBaseFileName)', '*Tracking_T&T*') THEN
        LET vSheetName = 'Terminal & Transport';
    ELSEIF WildMatch('$(vBaseFileName)', '*Tracking_TopLine*') THEN
        LET vSheetName = 'Top Line';
    ENDIF
    
    // Load the data from the sheet if the sheet name is not empty
    IF Len(vSheetName) > 0 THEN
        [$(vBaseFileName)]:
        LOAD *
        FROM [$(vFileName)]
        (ooxml, embedded labels, table is [$(vSheetName)]);

        // Add the file and sheet names as fields
        CONCATENATE (Data)
        LOAD '$(vBaseFileName)' AS FileName,
             '$(vSheetName)' AS SheetName,
             *
        RESIDENT [$(vBaseFileName)];
        
        // Drop the table created in the loop
        DROP TABLE [$(vBaseFileName)];
    ENDIF
NEXT

// Drop the Data table if it is empty
IF NoOfRows('Data') = 0 THEN
    DROP TABLE Data;
ENDIF
```
> In this updated code, we add an IF statement after defining the sheet name based on the file name. We only load the data from the sheet and concatenate it with the "Data" table if the sheet name is not empty. If the sheet name is empty, we skip the file and move on to the next file.

[Back to Top](#top)
### Pandas > Outlier:
> To see the outliers in a pandas dataframe, you can use a combination of descriptive statistics and visualizations. Here are some steps you can follow:
1. Use the describe() function to get a summary of the numerical columns in the dataframe. This will give you an idea of the range, mean, median, and standard deviation of the data.
2. Create box plots or histograms for the numerical columns to visualize the distribution of the data. This can help you identify potential outliers.
3. Use the quantile() function to calculate the 25th and 75th percentiles of the data. This can help you determine the interquartile range (IQR).
4. Calculate the lower and upper bounds for outliers using the IQR method. Any data point outside of these bounds can be considered an outlier.
5. Use boolean indexing to filter the dataframe for the outliers.
> Here's an example code snippet:
```py
import pandas as pd
import seaborn as sns
# load data into a pandas dataframe
df = pd.read_csv('data.csv')
# get summary statistics
print(df.describe())
# create box plot for a numerical column
sns.boxplot(x=df['column_name'])
# calculate IQR and bounds for outliers
q1 = df['column_name'].quantile(0.25)
q3 = df['column_name'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
# filter dataframe for outliers
outliers = df[(df['column_name'] < lower_bound) | (df['column_name'] > upper_bound)]
print(outliers)
```
> To see the outliers in a specific column of a pandas dataframe, you can follow the steps below:
1. Select the specific column you want to analyze by using its column name as a key to the dataframe. For example, if the column name is "col_name", you can use df['col_name'] to select it.
2. Use the describe() function on the selected column to get its summary statistics.
3. Create a box plot or a histogram for the selected column to visualize its distribution.
4. Calculate the lower and upper bounds for outliers using the IQR method. Any data point outside of these bounds can be considered an outlier.
5. Use boolean indexing to filter the selected column for outliers.
> Here's an example code snippet:
```py
import pandas as pd
import seaborn as sns
# load data into a pandas dataframe
df = pd.read_csv('data.csv')
# select the column you want to analyze
col_name = 'column_name'
col_data = df[col_name]
# get summary statistics
print(col_data.describe())
# create box plot for the column
sns.boxplot(x=col_data)
# calculate IQR and bounds for outliers
q1 = col_data.quantile(0.25)
q3 = col_data.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
# filter column for outliers
outliers = col_data[(col_data < lower_bound) | (col_data > upper_bound)]
print(outliers)
```
> The Interquartile Range (IQR) is a measure of statistical dispersion that is calculated as the difference between the 75th percentile (Q3) and the 25th percentile (Q1) of a dataset. The IQR represents the spread of the middle 50% of the data, which can be used to identify potential outliers.
The reason for choosing the 1.5 multiplier to calculate the bounds for outliers is a common rule of thumb in statistics. The lower bound is calculated as Q1 - (1.5 * IQR), and the upper bound is calculated as Q3 + (1.5 * IQR). Any data point outside of these bounds can be considered an outlier.
The 1.5 multiplier is based on the assumption that the distribution of the data is approximately normal, and that outliers are rare events that occur outside of three standard deviations from the mean. However, this assumption may not hold true for all datasets. In some cases, you may need to adjust the multiplier or use a different method to detect outliers based on the characteristics of the data.
In general, the choice of the percentage for the IQR method depends on the specific dataset and the desired level of sensitivity to outliers. Using a smaller multiplier, such as 1.0 or 1.3, will result in more stringent criteria for identifying outliers, while using a larger multiplier, such as 2.0 or 3.0, will result in a more lenient approach. It is important to choose an appropriate method based on the context and goals of the analysis.

[Back to Top](#top)
### SQL Scripts:
> Below will indicate best practices of SQL scripts:
[Back to Top](#top)
### Final all views and jobs:
> To find all views and jobs that are using the same table in addition to the stored procedures, you can use the following query:
```sql
SELECT DISTINCT
    OBJECT_NAME(o.object_id) AS 'Object Name',
    CASE o.type
        WHEN 'P' THEN 'Stored Procedure'
        WHEN 'V' THEN 'View'
        WHEN 'J' THEN 'SQL Server Agent Job'
    END AS 'Object Type'
FROM sys.sql_modules m
INNER JOIN sys.objects o ON m.object_id = o.object_id
WHERE m.definition LIKE '%table_name%'
UNION
SELECT DISTINCT 
    OBJECT_NAME(v.object_id) AS 'Object Name',
    'View' AS 'Object Type'
FROM sys.sql_modules m
INNER JOIN sys.views v ON m.object_id = v.object_id
WHERE m.definition LIKE '%table_name%'
UNION
SELECT DISTINCT 
    j.name AS 'Object Name',
    'SQL Server Agent Job' AS 'Object Type'
FROM msdb.dbo.sysjobs j
INNER JOIN msdb.dbo.sysjobsteps js ON j.job_id = js.job_id
WHERE js.command LIKE '%table_name%'
```
> Replace "table_name" with the name of the table you are interested in. This query will return a list of stored procedures, views, and SQL Server Agent jobs that reference the specified table.
Note that this query searches for the table name in the object's definition text for stored procedures and views, and in the job step's command text for SQL Server Agent jobs, so it may not find all references to the table. In particular, it will not find dynamic SQL references.

[Back to Top](#top)
### Identify triggers on a table:
> To identify triggers on a table in SQL Server, you can use the following query:
```sql
SELECT name
FROM sys.triggers
WHERE parent_class_desc = 'OBJECT_OR_COLUMN' 
    AND parent_id = OBJECT_ID('your_table_name');
```
> Replace "your_table_name" with the name of the table you are interested in. This query will return a list of trigger names that are associated with the specified table.
Once you have identified the trigger(s), you can review their code by right-clicking on the trigger name in SQL Server Management Studio and selecting "Modify". Alternatively, you can use the sp_helptext stored procedure to view the trigger code:
```sql
EXEC sp_helptext 'your_trigger_name';
```
> Replace "your_trigger_name" with the name of the trigger you want to view. This will display the trigger code in the query results window.
Note that triggers can be disabled or modified, so it is possible that the trigger code has been changed since it was originally created. It is important to review the trigger code to determine if it is responsible for the data loss issue. If you are unsure, you may want to seek assistance from your database administrator or support team.

[Back to Top](#top)
### Find which stored procedures are used:
> find out which stored procedures are using a specific table in SQL Server, you can use the following query :
```sql
SELECT DISTINCT OBJECT_NAME(OBJECT_ID) AS 'Stored Procedure Name'
FROM sys.sql_modules
WHERE definition LIKE '%table_name%'
```
> Replace "table_name" with the name of the table you are interested in. This query will return a list of stored procedures that reference the specified table.
Note that this query searches for the table name in the stored procedure definition text, so it may not find all references to the table. In particular, it will not find stored procedures that use dynamic SQL to reference the table.

[Back to Top](#top)
### Dynamic return last two months
```sql
DECLARE @CurrentMonth DATE = GETDATE()

SELECT FORMAT(@CurrentMonth, 'yyyyMM') AS MonthInFormat
UNION ALL
SELECT FORMAT(DATEADD(MONTH, -1, @CurrentMonth), 'yyyyMM')
UNION ALL
SELECT FORMAT(DATEADD(MONTH, -2, @CurrentMonth), 'yyyyMM')
ORDER BY MonthInFormat DESC
```
>
```markdown
MonthInFormat
-------------
202308
202307
202306
```
> This script produces the current month and the two previous months in descending order in a single column.

[Back to Top](#top)
### DataBricks:
> Below will indicate best practices of DataBricks scripts:

[Back to Top](#top)
### Convert the modified private key back to standard PEM format :
```py
private_key_pem = "-----BEGIN PRIVATE KEY-----\n" + \
                  "\n".join([pkb[i:i+64] for i in range(0, len(pkb), 64)]) + \
                  "\n-----END PRIVATE KEY-----"

# Convert the PEM string to a private key object
private_key_obj = serialization.load_pem_private_key(
    private_key_pem.encode(),
    password=None,
    backend=default_backend()
)

# Serialize the private key object back to PEM format
pem_private_key_corrected = private_key_obj.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
).decode()

# Update the options dictionary
options["pem_private_key"] = pem_private_key_corrected

# Your DataFrame write operation remains the same
Join_tt1320_tt1190_tt1210.write \
    .format("net.snowflake.spark.snowflake")\
    .options(**options)\
    .option("dbtable", "TREX_01")\
    .mode("overwrite")\
    .save()
```
[Back to Top](#top)
### Read all Parquet files in dbfs:
> To read multiple Parquet files stored in a distributed file system (like HDFS, S3, DBFS, etc.) in Databricks as one DataFrame, you can specify the path to the directory containing those files. If the files are named sequentially as you mentioned (e.g., Pa0001, Pa0002, ...), and they all reside in the same directory, you can specify the directory path itself.
Here's an example of how you can do this:
```py
# Path to the directory containing the Parquet files
path = "dbfs:/path/to/your/directory/"

# Read all Parquet files in the specified directory as one DataFrame
df = spark.read.parquet(path)

# Show the DataFrame
df.show()
```
> Databricks uses Apache Spark under the hood, so when you specify the directory path to the read.parquet method, Spark will read all the Parquet files in that directory and combine them into a single DataFrame.
Ensure you replace "dbfs:/path/to/your/directory/" with the actual path to your directory in the DBFS (Databricks File System) or whichever distributed file system you're using.

[Back to Top](#top)
### Read YAML file
> The correct method for installing a Python library in Databricks is to use the Databricks Libraries UI or to use an initialization script to install the library when the cluster starts. Unfortunately, you can't install libraries directly from a Databricks notebook using dbutils as I suggested in the previous response.
Here is how you can do it using the Libraries UI:
1. In the sidebar, click the cluster name.
2. Click the Libraries tab in the sidebar.
3. Click Install New.
4. Choose PyPI.
5. Type pyyaml in the Package text box.
6. Click Install.
Once you've done this, you should be able to import the yaml module in your notebook:
```py
import yaml
```
> Here's the corrected way to read the content of the file:
```py
import yaml

# Get file content as string
file_content = dbutils.fs.head('dbfs:/FileStore/bia/allocator/archiv/__h.yaml')

# Parse the YAML content to Python object
data = yaml.safe_load(file_content)

# Print the content
print(data)
```
> dbutils.fs.head() will return the first 65,536 bytes (or 64 KiB) of the file as a string. If your YAML file is larger than this, you may need to read the file as a binary object using dbutils.fs.open() and read the content with python built-in file handling methods.
> 
> If you need to read a larger file, here's a sample way to do this:
```py
import yaml

with dbutils.fs.open('dbfs:/FileStore/bia/allocator/archiv/__h.yaml') as f:
  file_content = f.read()

data = yaml.safe_load(file_content)
print(data)
```
> This will read the entire file regardless of its size. Again, I apologize for the confusion earlier, and I hope this helps!

[Back to Top](#top)
### Create Incrmental Loading:
> First we need to load the original table then saved as delta:
```py
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
# Load source data
df = spark.sql("SELECT * FROM `sfa_dl_bronze_prod`.`fis2`.`db2prod_tt1850`")
# Define the Delta table path
delta_path = "dbfs:/FileStore/IBRAHHO/db2prod_tt1850_delta_final"
# Write DataFrame to Delta format and save it
df.write.format("delta").mode("overwrite").save(delta_path)
```
> Then now will do the incrmental and schedule the notebook:
```py
from pyspark.sql import SparkSession
from pyspark.sql.functions import max, col
spark = SparkSession.builder.getOrCreate()
# Load the original source data
original_df = spark.sql("SELECT * FROM `sfa_dl_bronze_prod`.`fis2`.`db2prod_tt1850`")
# Define the source Delta table path
source_delta_path = "dbfs:/FileStore/IBRAHHO/db2prod_tt1850_delta_final"
# Try to load the source Delta table, if not exists then initialize it
try:
    delta_df = spark.read.format("delta").load(source_delta_path)
    # Get the latest timestamp in source Delta table
    last_update_time = delta_df.agg(max("header__event_timestamp")).collect()[0][0]
except:
    # If it's the first time and the table doesn't exist, we initialize it with an old timestamp
    last_update_time = "1970-01-01 00:00:00"
# Filter original source data to get only new data
new_data = original_df.filter(col("header__event_timestamp") > last_update_time)
# If there's new data, append it to the source Delta table
if new_data.count() > 0:
    new_data.write.format("delta").mode("append").save(source_delta_path)
# Load the updated source Delta data
df = spark.read.format("delta").load(source_delta_path)
# Define your target Delta table path
target_delta_path = "dbfs:/FileStore/IBRAHHO/tt1850_Test_Incrmental_final"
# Try to load the target delta table, if not exists then initialize it
try:
    latest_df2 = spark.read.format("delta").load(target_delta_path)
    # Get the latest timestamp in target delta table
    last_update_time_target = latest_df2.agg(max("header__event_timestamp")).collect()[0][0]
except:
    # If it's the first time and the table doesn't exist, we initialize it with an old timestamp
    last_update_time_target = "1970-01-01 00:00:00"
# Filter source data to get only new data 
new_data_target = df.filter(col("header__event_timestamp") > last_update_time_target)
# If there's new data, process it and append it to the delta table
if new_data_target.count() > 0:
    # Filter the latest time stamp
    max_timestamp_df = new_data_target.groupBy("FK_TT1820CLIENT", "FK_TT1820ID_NUMBER", "FK_TT1830REL_NUMBE", "REL_NUMBER").agg(max("header__event_timestamp").alias("latest_timestamp"))
    latest_new_data = new_data_target.join(max_timestamp_df, on=["FK_TT1820CLIENT", "FK_TT1820ID_NUMBER", "FK_TT1830REL_NUMBE", "REL_NUMBER"], how='inner').filter(new_data_target["header__event_timestamp"] == max_timestamp_df["latest_timestamp"])
    
    # Append new data to the delta table
    latest_new_data.write.format("delta").mode("append").save(target_delta_path)
# S3 Path
S3_Path = "s3://052968007531-bia-analytics-zone-s3-eu-central-1/users/IBRAHHO/queries/tt1850_Incrmental_Logic/Parquet"
S3_Path_csv = "s3://052968007531-bia-analytics-zone-s3-eu-central-1/users/IBRAHHO/queries/tt1850_Incrmental_Logic"
# Write to S3 as parquet
latest_new_data.write.format("parquet").mode("overwrite").save(S3_Path)
# Write to S3 as csv
latest_new_data.write.format("csv").mode("overwrite").option("header", "true").save(S3_Path_csv)
```
[Back to Top](#top)
### Write csv to S3 Bucket
```py
def write_data_to_s3(table, bucket, filename):
    """
    Writes dataframe as single csv to defined S3 bucket.
    """
    
    table.coalesce(1).write.format("com.databricks.spark.csv").mode("overwrite").option("header", "true").save(f"{bucket}{filename}")
    data_location = bucket + filename
    files = dbutils.fs.ls(data_location)
    csv_file = [x.path for x in files if x.path.endswith(".csv")][0]
    dbutils.fs.mv(csv_file, data_location.rstrip('/') + ".csv")
    dbutils.fs.rm(data_location, recurse = True)
```
[Back to Top](#top)
### Write Parquet to S3 Bucket
> the function to write to parquet by changing the data format from CSV to Parquet. You also have to adjust the file extension at the end. Here is the updated code:
```py
def write_data_to_s3(table, bucket, filename):
    """
    Writes dataframe as single parquet to defined S3 bucket.
    """
    
    table.coalesce(1).write.format("parquet").mode("overwrite").option("header", "true").save(f"{bucket}{filename}")
    data_location = bucket + filename
    files = dbutils.fs.ls(data_location)
    parquet_file = [x.path for x in files if x.path.endswith(".parquet")][0]
    dbutils.fs.mv(parquet_file, data_location.rstrip('/') + ".parquet")
    dbutils.fs.rm(data_location, recurse = True)
```
> Please note that the option "header" is generally not applicable in parquet format because parquet is a columnar format which always contains schema or header information.
Also, bear in mind that writing to parquet format may not behave exactly as CSV format. For instance, when you use coalesce(1), it may not always create a single parquet file due to the nature of how the parquet format works. If you absolutely need a single file, consider writing the dataframe to a single file in a temporary location and then moving the file to the final location.

[Back to Top](#top)
### Athena:
> Below will indicate best practices of Athena scripts:

[Back to Top](#top)
### SUBSTR and SUBSTRING :
> Athena does not natively support the LEFT() function as it uses Presto SQL. Instead, you can use the SUBSTR() or SUBSTRING() function to achieve the same result. Here's how you can do it:
> 
> Using SUBSTR():
```sql
SELECT SUBSTR(column_name, 1, 4) AS result
FROM your_table_name;
```
> Using SUBSTRING():
```sql
SELECT SUBSTRING(column_name, 1, 4) AS result
FROM your_table_name;
```
> Replace column_name with the name of the column containing the string you want to extract characters from, and your_table_name with the name of the table in your AWS Glue Data Catalog.
> For example, if you have a table named orders with a column named product_code:
> 
> Using SUBSTR():
```sql
SELECT SUBSTR(product_code, 1, 4) AS product_prefix
FROM orders;
```
> Using SUBSTRING():
```sql
SELECT SUBSTRING(product_code, 1, 4) AS product_prefix
FROM orders;
```
> These queries will extract the first 4 characters from the left of the product_code column and return the result in a new column named product_prefix.
> 
> In AWS Athena, to extract characters from the right side of a string, you can use a combination of the LENGTH() and SUBSTR() or SUBSTRING() functions. Here's how you can do it:
> 
> Using SUBSTR():
```sql
SELECT SUBSTR(column_name, LENGTH(column_name) - 3) AS result
FROM your_table_name;
```
> Using SUBSTRING():
```sql
SELECT SUBSTRING(column_name, LENGTH(column_name) - 3) AS result
FROM your_table_name;
```
> Replace column_name with the name of the column containing the string you want to extract characters from, and your_table_name with the name of the table in your AWS Glue Data Catalog.
> 
> For example, if you have a table named orders with a column named product_code and you want to extract the last 4 characters:
> 
> Using SUBSTR():
```sql
SELECT SUBSTR(product_code, LENGTH(product_code) - 3) AS product_suffix
FROM orders;
```
> Using SUBSTRING():
```sql
SELECT SUBSTRING(product_code, LENGTH(product_code) - 3) AS product_suffix
FROM orders;
```
> These queries will extract the last 4 characters from the right of the product_code column and return the result in a new column named product_suffix. Note that the number 3 in the LENGTH function is used because we want to extract the last 4 characters (4 - 1 = 3).

[Back to Top](#top)
### Date and Year:
> This Athena query extracts the first 10 characters from the rft_date column, which likely represents a date in the format 'YYYY-MM-DD', and then parses it using the date_parse function to obtain the date value. To extract the year from this date value, you can use the year function.
> 
> Here's the updated query with the year function:
```sql
year(date_parse(SUBSTRING(rft_date, 1, 10),'%Y-%m-%d'))
```
> In Athena, you can use the date_parse function to convert a VARCHAR date string to a date. Since your date string is in the format 'YY-MM-DD', you can parse it using the following query:
```sql
date_parse('13-03-23', '%y-%m-%d')
```
> This query will convert the VARCHAR '13-03-23' to a date value. The format specifier '%y-%m-%d' is used to match the given date string format.

[Back to Top](#top)
### Python > Copy files
> To copy all the QVD files from the src_folder to the dst_folder, you can modify the script as follows:
```py
import os
import shutil

src_folder = r'\\qs-fs-project-dev.aws-euc1.hlag.com\share\Business Administration\1_QVD_Extract\LSC_Allocation'
dst_folder = r'\\ww.hl.lan\HH1\Groups\RHH0T430 - REGION REPORTING\QV Server\4.BA Controlling\1.Operational Cost Reporting\2.QVD\AM_Allocation'

def copy_files(src_folder, dst_folder, file_extension):
    # Iterate through the files in the source folder
    for filename in os.listdir(src_folder):
        # Check if the file has the desired extension
        if filename.endswith(file_extension):
            src_path = os.path.join(src_folder, filename)
            dst_path = os.path.join(dst_folder, filename)

            # Copy the file to the destination folder
            shutil.copy(src_path, dst_path)
            print(f'Copied file {filename} from {src_folder} to {dst_folder}')

# Call the function to copy all QVD files from src_folder to dst_folder
copy_files(src_folder, dst_folder, '.qvd')
```
> This script defines a copy_files function that takes the source folder, destination folder, and the desired file extension as its arguments. It iterates through the files in the source folder, checks if the file has the desired extension (in this case, .qvd), and copies the file to the destination folder. The function is then called with the appropriate arguments to copy all QVD files from src_folder to dst_folder.

[Back to Top](#top)
### Python > Dynamic Column Rename
> rename the columns based on their position, you can modify the script as follows:
```py
import pandas as pd
import os

# Step 1: Read the original Excel file
input_file = 'your_input_file.xlsx'
df = pd.read_excel(input_file)

# Step 2: Rename the columns based on their position
cols = list(df.columns)
cols[0] = 'HH1'
cols[1] = 'HH2'

df.columns = cols

# Step 3: Convert the DataFrame to CSV and save in the destination folder
output_folder = 'C:\\HO'
output_file = os.path.join(output_folder, 'output_file.csv')
df.to_csv(output_file, index=False)
```
[Back to Top](#top)
### Python > Rename file with date
> You can rename a file in Python using the os module's rename() function. You can create today's date string using the datetime module. Here's how you can do it:
```py
import os
from datetime import datetime

# Current date as string in 'YYYYMMDD' format
today_date = datetime.now().strftime('%Y%m%d')

# Assuming your filename is 'oldfile.txt'
old_file_name = 'oldfile.txt'

# Extract the extension from the old filename
file_extension = os.path.splitext(old_file_name)[1]

# New filename will be 'file_YYYYMMDD.extension'
new_file_name = 'file_' + today_date + file_extension

# Rename the file
os.rename(old_file_name, new_file_name)
```
> This code will rename 'oldfile.txt' to 'file_YYYYMMDD.txt', where 'YYYYMMDD' is today's date.
Please make sure to replace 'oldfile.txt' with your actual file name and ensure that your Python script has the necessary permissions to rename the file.
Also, ensure the file you want to rename and the Python script are in the same directory, otherwise you will need to specify the full path for the file.

[Back to Top](#top)
### Alteryx > Read Parquet file
> Use Python or R within Alteryx: Alteryx supports running Python and R scripts using the Python Tool or R Tool. You could use a similar script to the ones above within Alteryx to read in the parquet file and output a data frame.
> 
> Here's an example using the Python Tool:
```py
import pandas as pd
import pyarrow.parquet as pq

# Read the parquet file
df = pd.read_parquet('yourfile.parquet')

# Output data
Alteryx.write(df, 1)
```
> Note: These methods may not work if you're dealing with very large parquet files, due to memory constraints. For very large datasets, you may need to use a big data processing tool such as Apache Spark to first convert your parquet file into a manageable size or format.
> 
> Finally, Alteryx may have added support for reading parquet files directly after my last update, so you might want to check the latest Alteryx documentation or contact Alteryx support for the most current information.

[Back to Top](#top)