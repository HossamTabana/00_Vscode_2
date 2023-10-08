# %%
# Source code: https://robust-dinosaur-2ef.notion.site/DuckDB-Tutorial-Getting-started-for-beginners-b80bf0de8d6142d6979e78e59ffbbefe
# Material : https://www.kaggle.com/datasets/kushagra1211/usa-sales-product-datasetcleaned#
# Youtube : https://www.youtube.com/watch?v=AjsB6lM2-zw
# %%
import pandas as pd
# %%
import pandas as pd
import glob
import time
import duckdb
# %%
conn = duckdb.connect() # create an in-memory database
# %%
# with pandas
cur_time = time.time()
df = pd.concat([pd.read_csv(f) for f in glob.glob('dataset/*.csv')])
print(f"time: {(time.time() - cur_time)}")
print(df.head(10))
# %%
# with duckdb
cur_time = time.time()
df = conn.execute("""
	SELECT *
	FROM 'dataset/*.csv'
	LIMIT 10
""").df()
print(f"time: {(time.time() - cur_time)}")
print(df)
# %%
df = conn.execute("""
	SELECT *
	FROM 'dataset/*.csv'
""").df()
conn.register("df_view", df)
conn.execute("DESCRIBE df_view").df() # doesn't work if you don't register df as a virtual table
# %%
conn.execute("SELECT COUNT(*) FROM df_view").df()
# %%
df.isnull().sum()
df = df.dropna(how='all')

# Notice we use df and not df_view
# With DuckDB you can run SQL queries on top of Pandas dataframes
conn.execute("SELECT COUNT(*) FROM df").df()
# %%
conn.execute("""SELECT * FROM df WHERE "Order ID"='295665'""").df()
# %%
conn.execute("""
CREATE OR REPLACE TABLE sales AS
	SELECT
		"Order ID"::INTEGER AS order_id,
		Product AS product,
		"Quantity Ordered"::INTEGER AS quantity,
		"Price"::Decimal AS price_each,
		strptime("Order Date", '%Y-%m-%d %H:%M:%S')::DATE as order_date,
		"Purchase Address" AS purchase_address
	FROM df
	WHERE
		TRY_CAST("Order ID" AS INTEGER) NOTNULL
        and TRY_CAST("Price" AS Decimal) NOTNULL
""")
# %%
conn.execute("FROM sales").df()
# %%
conn.execute("""
	SELECT 
		* EXCLUDE (product, order_date, purchase_address)
	FROM sales
	""").df()
# %%
