import pandas as pd

def basic_price_features(df):
    df['date'] = df['timestamp'].dt.date
    df['time'] = df['timestamp'].dt.time
    df['is_930'] = df['time'] == pd.to_datetime("09:30").time()
    df['is_935'] = df['time'] == pd.to_datetime("09:35").time()
    return df