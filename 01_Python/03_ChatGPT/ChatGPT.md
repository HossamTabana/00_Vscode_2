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

