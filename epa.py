import requests
import pandas as pd
import io
import json
import csv
import os

# Set the API endpoint and your email and password
endpoint = "https://aqs.epa.gov/data/api/sampleData/byCounty"
email = "afakun@u.rochester.edu"
password = "silverram14"

# Set the date range for the data
start_date = "20210101"
end_date = "20210228"

# Set the pollutant codes and column names for the data
pollutant_codes = ["44201", "81102", "85129", "88101"]
column_names = ["date", "Ozone", "PM10 Total 0-10µm STP", "Lead PM10 LC FRM/FEM", "PM2.5 - Local Conditions"]

# Set the county and state codes for the data
# county_codes = ['031']
# state_codes = ["17"]

county_codes = ['017', '055', '086', '027', '029', '031']
state_codes = ["25", "36", "12", "06" , "30", "17"]

# Loop through the counties and download the air quality data
for county, state in zip(county_codes, state_codes):
    # Construct the API request URL
    url = f"{endpoint}?email={email}&key={password}&param={','.join(pollutant_codes)}&bdate={start_date}&edate={end_date}&state={state}&county={county}"
    
    # Send the API request
    response = requests.get(url)
    json_data = response.json()
    
    with open('response.json', 'w') as f:
        json.dump(json_data, f) 
        
    with open('response.json') as json_file:
        data = json.load(json_file)
    
    pollutant_data = data['Data']
    csv_file = open('data_file.csv', 'w')
    
    # create the csv writer object
    csv_writer = csv.writer(csv_file)
    
    count = 0
    
    for var in pollutant_data:
        if count == 0:
            header = var.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(var.values())
    csv_file.close()
            


        
        

    
    
    
  
    
    
    
    
    
    # # Extract the relevant fields for the pollutant of interest
    # rows = []
    # for d in data['Data']:
    #     row = [
    #         d['date_local'],
    #         d['sample_measurement'],
    #         d['state'],
    #         d['county'],
    #         d['parameter_code'],  # Add column for parameter code
    #         d['units_of_measure'],  # Add column for units of measure
    #     ]
    #     rows.append(row)
    
    # # Save the data as a CSV file
    # for column_name in column_names[1:]:
    #     with open(f"{county}_{column_name}.csv", 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(['date', column_name])
            
    #         # Create a new DataFrame from the rows
    #         df = pd.DataFrame(rows, columns=['date_local', 'sample_measurement', 'state', 'county', 'parameter_code', 'units_of_measure'])
    #         df = df[df['state'] == state]  # filter by state
    #         df = df[df['county'] == county]  # filter by county
    #         df = df[df['parameter_code'] == column_name.split()[0]]  # filter by pollutant code
    #         df = df.rename(columns={'sample_measurement': column_name})
    #         df = df[['date_local', column_name]]

    #         # Add missing dates to the DataFrame
    #         date_range = pd.date_range(start_date, end_date)
    #         missing_dates = date_range.difference(pd.to_datetime(df['date_local']))
    #         missing_data = pd.DataFrame({'date_local': missing_dates, column_name: 'none'})
    #         df = pd.concat([df, missing_data])
            
    #         # Write the DataFrame to the file
    #         df.to_csv(file, index=False)
