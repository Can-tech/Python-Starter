import pandas as pd

# Specify the path to your CSV file
csv_file_path = 'in_class\HE_Hall_Effect\part2data.csv'  # Replace with the actual path to your CSV file

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path, sep='\t')
# print("Column Names:", df.columns)

# Access the columns
flux_density = df['flux_density']
hall_voltage = df['hall_voltage']
sample_voltage = df['sample_voltage']

# # Print the arrays
# print("Flux Density:", flux_density)
# print("Hall Voltage:", hall_voltage)
# print("Sample Voltage:", sample_voltage)
