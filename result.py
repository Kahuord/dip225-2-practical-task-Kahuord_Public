import pandas
get_info=input() #input information from terminal

fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA") # if no pages are specified, then the last one saved is open
info_list = fails.values.tolist()

# Search for region code by name
region_code = None
for row in info_list:
    if row[1] == get_info:
        region_code = row[0]
        break

if region_code is None:
    print(0)
else:
    # Read data from data.csv
    data_csv = pandas.read_csv("data.csv")

    total_geo_count = data_csv[data_csv['Area'] == region_code]['geo_count'].sum()
   
    print(int(total_geo_count))
