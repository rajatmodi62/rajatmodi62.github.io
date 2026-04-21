import pandas as pd
import json

# Read your generated CSV
df = pd.read_csv('papers.csv')

# Optional: Add a 'subject' column if you want to test sorting by area
# For now, we'll just ensure the data is clean
df = df.fillna("")

# Convert to list of dictionaries
data = df.to_dict(orient='records')

# Save as JSON for the HTML page
with open('papers.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Converted papers.csv to papers.json. Now open the index.html!")