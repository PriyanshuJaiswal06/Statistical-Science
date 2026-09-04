# import yaml
# import os
# print(os.getcwd())

# with open("./ipl/335982.yaml", 'r') as file:
#     yaml_data = yaml.safe_load(file)
# print(yaml_data)

# import pandas as pd
# df = pd.DataFrame([yaml_data["info"]])
# df.to_excel("players.xlsx", index=False)
 
import yaml
import pandas as pd

# Load YAML file
with open('./ipl/335982.yaml') as file:
    data = yaml.safe_load(file)

# Convert to DataFrame
df = pd.DataFrame(data)

# Export to Excel
df.to_excel('output_file.xlsx', index=False)
