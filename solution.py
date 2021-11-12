"""
Developed by Mohanad Abu-Nayla, Nov-2021.
This work comes without any warranty of any type, use it at your own risk.
If you find any thing useful, please send me a message/credit me, but you are not required to do so.
"""



from helpers import DateUtil
import seed
import pandas as pd
from tabulate import tabulate

# 1- Clean up the list of dates , and remove alpha characters.
raw_dirty_list = seed.res
util = DateUtil()
clean_list = []

# Step 1
print("Step1: remove alphabet characters from time stamps ")
clean_list = util.clean_list_from_alphabet(raw_dirty_list)

# Step 2
print("Step2: sort the list of dates in descending order")
sorted_list = util.sort_list_descending(clean_list)

# Step 3
print("Step3: parse the list of dates into a list of datetime objects")
list_of_dates = util.parse_list_of_dates(sorted_list)

# Step 4
days_list = util.drop_hours_minutes_seconds_microseconds(list_of_dates)

# Step 5
# print("Step 5: Find the longest period of consecutive logins occurred")
test_dict = util.count_logins(days_list)

# Step 6 print the data in a table form with descending order.
df = pd.DataFrame.from_dict(test_dict).sort_values(by=['LENGTHS'], ascending=False)
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
