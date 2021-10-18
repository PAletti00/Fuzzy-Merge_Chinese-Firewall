# Imports
import os
from difflib import SequenceMatcher

import pandas as pd
from whoswho import who

# File directories and file names
dir1 = os.path.join('C:',os.sep,'Users', 'pietr', 'Desktop', 'Esther and Pietro', 'Chinese Firewall project', '')
print(dir1)
file_master = 'all_authors_list_top50.csv'

dir2 = os.path.join('C:',os.sep,'Users', 'pietr', 'Desktop', 'Esther and Pietro', 'Chinese Firewall project', 'Output', '')
file_new = 'authorsonly.csv'
print(dir2)
dir_output = os.path.join('C:',os.sep,'Users', 'pietr', 'Desktop', 'Esther and Pietro', 'Chinese Firewall project', 'Output',
                          '')
print(dir_output)
file_output = 'Output.csv'

# Load data sets
df_master = pd.read_csv(dir1 + file_master)
df_master['Name'] = df_master['author']
df_master['Source'] = 'Master Dataset'
del df_master['author']

df_new = pd.read_csv(dir2 + file_new)
df_new['Name'] = df_new['coauthor']
df_new['Source'] = 'New Dataset'
del df_new["coauthor"]

# Merge the two data sets
df_merged = pd.concat([df_master, df_new])

# First remove all duplicates that are identical matches
df_merged.drop_duplicates(subset='Name', keep="first", inplace=True)
df_merged.reset_index(drop=True, inplace=True)
print("Just before Loop")
# Then remove duplicates based on a high similarity ratio (>0.75)
for index1, row1 in df_merged.iterrows():
    name1 = row1['Name']

    for index2, row2 in df_merged.iterrows():
        name2 = row2['Name']

        if index2 > index1:
            similarity_ratio = SequenceMatcher(None, name1, name2).ratio()
            similarity_score = who.ratio(name1, name2)

            if similarity_ratio > 0.75 and similarity_score > 75:
                df_merged.drop(index2, inplace=True)
            else:
                pass

print("Right After Loop")
# Subset only rows that come from new dataset
df_merged_new = df_merged[df_merged['Source'] == 'New Dataset']

# Save output as CSV
df_merged_new.to_csv(dir_output + file_output, index=False)
#Computation Time
time_elapsed_minutes = int((time.time() - start_time)/ 60)
time_elapsed_seconds = round((time.time() - start_time)% 60, 2)
print(f'Time Elapsed: {str(time_elapsed_minutes)} minutes and {str(time_elapsed_seconds)} seconds')