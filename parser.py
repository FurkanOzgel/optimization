import pandas as pd
from datetime import datetime
import json
import os

def convert_json_to_dataframe(file_path):
    """
    Converts JSON data from a file to a pandas DataFrame with dates as index and close prices.

    Parameters:
    file_path (str): The path to the JSON file from Yahoo Finance API.

    Returns:
    pd.DataFrame: A pandas DataFrame with dates as index and close prices as column.
    """
    # Load JSON data from file
    with open(file_path, 'r') as f:
        json_data = json.load(f)
    
    # Extract data from nested JSON structure
    result = json_data['chart']['result'][0]
    
    # Get symbol name
    symbol = result['meta']['symbol']
    
    # Get timestamps and convert to dates
    timestamps = result['timestamp']
    dates = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d') for ts in timestamps]
    
    # Get close prices (using adjclose if available, otherwise close)
    try:
        close_prices = result['indicators']['adjclose'][0]['adjclose']
    except (KeyError, IndexError):
        close_prices = result['indicators']['quote'][0]['close']
    
    # Create DataFrame
    df = pd.DataFrame({
        symbol: close_prices
    }, index=pd.to_datetime(dates))
    
    df.index.name = 'Date'
    
    return df

def load_multiple_stocks(folder_path):
    """
    Loads multiple Yahoo Finance JSON files and merges them into a single DataFrame.
    """
    dfs = []

    for file in os.listdir(folder_path):
        if file.endswith(".json"):
            df = convert_json_to_dataframe(os.path.join(folder_path, file))
            dfs.append(df)

    prices = pd.concat(dfs, axis=1)
    return prices



if __name__ == "__main__":
    # Test the conversion function
    df = convert_json_to_dataframe('train_data/aapl.json')
    print(df)