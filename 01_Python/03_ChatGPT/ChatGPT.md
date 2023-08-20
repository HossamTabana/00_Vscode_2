# ChatGPT best

## About it
> This is the best search of ChatGPT

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
15. [Reading Large CSV files in Pandas and adjust Data Type](#reading-large-csv-files-in-pandas-and-adjust-data-type)
16. [Pandas > Filter and Convert Datetime](#pandas--filter-and-convert-datetime)
17. [SQL > Explain Locate and Position](#sql--explain-locate-and-position)
18. [AWS > Position Function](#aws--position-function)
19. [AWS > SUBSTR and LENGTH](#aws--substr-and-length)
20. [Convert QVD to Parquet](#convert-qvd-to-parquet)
21. [Benefits of Parquet file](#benefits-of-parquet-file)
22. [Pandas > Read Large Parquet files](#pandas--read-large-parquet-files)
23. [SQL > Grant Access](#sql--grant-access)
    - [View Access](#view-access)
    - [Revoke View Access](#revoke-view-access)
    - [Grant Execute Procedure](#grant-execute-procedure)
    - [Grant Execute Procedure and remove other users](#grant-execute-procedure-and-remove-other-users)
    - [Back The User Admin works again](#back-the-user-admin-works-again)
    - [allow PowerBI_HQ to only execute the job](#allow-powerbi_hq-to-only-execute-the-job)
    - [Restoring t_board_db to its original state](#restoring-t_board_db-to-its-original-state)
24. [YouTube Download 1080](#youtube-download-1080)
    - [YouTube Download 720](#youtube-download-720)
25. [Setup environment variables in VSCode](#setup-environment-variables-in-vscode)
    - [Multiple projects within the same workspace in VSCode](#multiple-projects-within-the-same-workspace-in-vscode)
    - [General .env file that's shared across multiple projects](#general-env-file-thats-shared-across-multiple-projects)


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
### Install JupyterLab
```sh
$ conda install -c conda-forge jupyterlab
```
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
### Benefits of Parquet file:
> Parquet is a file format designed for efficient columnar storage and processing of data. Here are some key points to know about Parquet:

- Parquet stores data in a columnar format, which means that all values of a particular column are stored together, making it easier and faster to read and process specific columns of data.
- Parquet uses compression algorithms to reduce file size, making it easier to transfer and store large amounts of data.
- Parquet is an open-source format that is widely used in big data processing frameworks like Apache Hadoop, Apache Spark, and Apache Arrow.
- Some of the benefits of using Parquet include improved query performance, lower storage costs, and better compatibility with distributed systems.

In general, if you have large amounts of data that you need to store and process efficiently, converting it to the Parquet format can be a good option. The columnar storage and compression features of Parquet make it particularly well-suited for big data applications.
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
### SQL > Grant Access :
> Below will indicate all search of Microsoft SQL Server Access:
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




