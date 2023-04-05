ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

user1_ids = ids['user1']
user2_ids = ids['user2']
user3_ids = ids['user3']

all_user_ids = user1_ids + user2_ids + user3_ids
result = []

for user_ids in all_user_ids:
  if user_ids not in result:
    result.append(user_ids)
    

print(result)