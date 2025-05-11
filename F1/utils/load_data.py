import pandas as pd
import os

def load_csv(filename, subfolder='raw'):
    """
    Load a CSV file from a subfolder under the main /data directory.

    Args:
        filename (str): e.g., 'SPY_5min_2020_05.csv'
        subfolder (str): 'raw', 'processed', or 'features'

    Returns:
        pd.DataFrame
    """
    base_path = os.path.dirname(os.path.dirname(__file__))  # This gets the SPY_Model folder
    csv_path = os.path.join(base_path, "data", subfolder, filename)
    return pd.read_csv(csv_path)