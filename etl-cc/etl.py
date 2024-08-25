import pandas as pd

def extract(file_path):
    return pd.read_csv(file_path)

def transform(data):
    # Simple transformation: Add a new column 'Processed' with True
    data['Processed'] = True
    return data

def load(data, output_path):
    data.to_csv(output_path, index=False)

if __name__ == '__main__':
    data = extract('input.csv')
    transformed_data = transform(data)
    load(transformed_data, 'output.csv')
