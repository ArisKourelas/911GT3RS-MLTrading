from src.data.load_data import load_5min_data
from src.features.block1_basics import basic_price_features
from src.models.train_model import train_model
import pandas as pd

def run_pipeline(data_path):
    df = load_5min_data(data_path)
    df = basic_price_features(df)

    df_filtered["date"] = df_filtered["timestamp"].dt.date
    df_filtered["time"] = df_filtered["timestamp"].dt.time

    # Drop duplicates
    df_filtered = df_filtered.drop_duplicates(subset=["date", "time"], keep="first")

    # Filter out any days that don’t have exactly 9:30 AND 9:35
    time_counts = df_filtered.groupby("date")["time"].nunique()
    invalid_dates = time_counts[time_counts != 2].index
    df_filtered = df_filtered[~df_filtered["date"].isin(invalid_dates)]

    # Pivot safely
    df_pivot = df_filtered.pivot(index="date", columns="time", values="close")
    
    # Create target: percent return 9:30 → 9:35
    time_930 = pd.to_datetime("09:30").time()
    time_935 = pd.to_datetime("09:35").time()

    df_pivot["target"] = (df_pivot[time_935] - df_pivot[time_930]) / df_pivot[time_930]
    df_pivot["label"] = (df_pivot["target"] > 0).astype(int)

    # Simple feature: just 9:30 price
    features = df_pivot[[time_930]]
    features.columns = ["open_930"]

    labels = df_pivot["label"]

    train_model(features, labels)