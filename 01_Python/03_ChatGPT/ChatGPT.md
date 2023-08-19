# ChatGPT best

## About it
> This is the best search of ChatGPT

## Table of contents

1. [Merge Two DataFrame](#merge-two-dataframe)
2. [Vlookup in Pandas](#vlookup-in-pandas)
3. [Concatenate two columns using pandas](#concatenate-two-columns-using-pandas)
4. [Install JupyterLab](#install-jupyterlab)
5. [Extract SAP using Excel](#extract-sap-transaction-using-excel)
6. [Extract SAP Using Excel Method 2](#extract-sap-transaction-using-excel-method-2)


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

