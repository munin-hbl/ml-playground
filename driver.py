import pandas as pd
import os
import kagglehub
from kagglehub import KaggleDatasetAdapter

dataset_path = kagglehub.dataset_download("ramakrishnanthiyagu/delivery-truck-trips-data")
print("Dataset downloaded to:", dataset_path)


file_name = "Delivery truck trip data.xlsx"
file_path = os.path.join(dataset_path, file_name)

print("Excel file path:", file_path)

# 3. Læs filen med pandas direkte
df = pd.read_excel(file_path, engine="openpyxl")

df
