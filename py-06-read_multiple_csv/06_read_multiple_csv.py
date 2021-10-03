# YouTube Link: https://www.youtube.com/watch?v=TN_Cvyq_rxE
# Blog Link: https://www.business-science.io/python/2021/09/21/python-read-csv.html?utm_content=buffer874be&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer

# Libraries ----
import pandas as pd
import glob

# File Path ----
path = "car_data/"
all_files = glob.glob(path + "*.csv")

all_files

# Method 01: For-Loop ----
li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

li

df = pd.concat(li, axis=0, ignore_index=True)
df

# Method 02: Map ----
# Benefits: Don't need to make for-loop / More concise/ Slightly faster / no list construction
li_mapper = map(lambda filename: pd.read_csv(filename, index_col=None, header=0), all_files)

li_2 = list(li_mapper)

df = pd.concat(li_2, axis=0, ignore_index=True)
df

# Method 3: List Comprehension ----
# Benefits: Similar to method 2, but slightly more concise

li_3 = [pd.read_csv(filename, index_col=None, header=0) for filename in all_files]

df = pd.concat(li_3, axis=0, ignore_index=True)
df