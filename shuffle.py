import pandas as pd
import numpy as np

# Load the dataset
file_path = 'final_dataset.csv'  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Shuffle the entire dataset while ensuring the sentiments are mixed
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the shuffled dataset to a new CSV file
df_shuffled.to_csv('final_dataset1.csv', index=False)

print("The data has been shuffled and saved to 'shuffled_file.csv'.")
