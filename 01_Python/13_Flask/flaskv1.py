from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Create a simple dataframe
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
})


@app.route('/get_dataframe', methods=['GET'])
def get_dataframe():
    return jsonify(df.to_dict(orient='records'))


if __name__ == "__main__":
    app.run(debug=True)
