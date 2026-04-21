import pandas as pd
import json

# Read your test.csv
df = pd.read_csv('papers.csv')
df = df.fillna("")

# Convert to list of dictionaries
data = df.to_dict(orient='records')

# Save as a JavaScript variable assignment
with open('data.js', 'w') as f:
    f.write("const PAPERS_DATA = ")
    json.dump(data, f, indent=4)
    f.write(";")

print("Generated data.js! Now update your index.html.")