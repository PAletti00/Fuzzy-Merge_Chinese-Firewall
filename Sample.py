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
df_master['author_name'] = df_master['author']
df_master['Source'] = 'Master Dataset'
del df_master['author']

df_new = pd.read_csv(dir2 + file_new)
df_new['coauthor_name'] = df_new['coauthor']
df_new['Source'] = 'New Dataset'
del df_new["coauthor"]

# Merge the two data sets
file_int = 'author_coauthor.csv'
df_merged = df_master.join(df_new['coauthor_name'])
df_merged.to_csv(dir1 + file_int, index=False)


# First remove all duplicates that are identical matches
# df_merged.drop_duplicates(subset='Name', keep="first", inplace=True)
df_merged.reset_index(drop=True, inplace=True)

#Create a subsample of 300 observations of df_merged
df_merged_sample = df_merged.sample(n=300,replace=False)
df_merged_sample.to_csv(dir_output + file_output, index=False)
print(df_merged_sample.head(10))




