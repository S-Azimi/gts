print("in the name of god")
import pandas as pd

# Load the Excel file
excel_file = 'test_data.xlsx'  # Replace with your Excel file path
data = pd.read_excel(excel_file, sheet_name='Sheet1')  # Adjust sheet name as necessary

# Convert the DataFrame to JSON
json_data = data.to_json(orient='records', lines=True)

# Save the JSON data to a file
with open('output.json', 'w') as json_file:
    json_file.write(json_data)

print("Conversion complete! JSON saved as output.json")