# The Latest Login in 2020

# Write your MySQL query statement below

# we want to take both columns with the maximum time from time_stamp for each user
# time_stamp containing a string of 2020
# grouping by user_id prevents uniques
select user_id, max(time_stamp) as last_stamp from Logins where time_stamp like '%2020%' group by user_id