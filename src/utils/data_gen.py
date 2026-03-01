"""
TEKNOFEST 2025 — Elite Command Center
Synthetic Data Generator (Enconding Safe)
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_sample_data(num_records=100):
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    np.random.seed(42)

    data = {
        'user_id': [f"user_{i:03d}" for i in range(num_records)],
        'timestamp': [(datetime.now() - timedelta(days=np.random.randint(0, 30))).strftime("%Y-%m-%d %H:%M:%S") for _ in range(num_records)],
        'phq9_score': np.random.randint(0, 28, num_records),
        'gad7_score': np.random.randint(0, 22, num_records),
        'pss10_score': np.random.randint(0, 41, num_records),
        'cd_risc_score': np.random.randint(30, 101, num_records),
        'sleep_disruption': np.random.choice([0, 1], num_records, p=[0.7, 0.3]),
        'social_withdrawal': np.random.choice([0, 1], num_records, p=[0.8, 0.2]),
        'sentiment_label': np.random.choice(['positive', 'neutral', 'negative'], num_records, p=[0.3, 0.4, 0.3])
    }

    df = pd.DataFrame(data)
    raw_path = "data/raw/synthetic_psych_data_2025.csv"
    df.to_csv(raw_path, index=False)
    # No prints to avoid encoding issues in restricted shells

if __name__ == "__main__":
    generate_sample_data()
