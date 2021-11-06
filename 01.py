
# Initializes User Data and friendships
users = [
    { "id": 0, "name": "Hero"},
    { "id": 1, "name": "Dunn"},
    { "id": 2, "name": "Sue"},
    { "id": 3, "name": "Chi"},
    { "id": 4, "name": "Thor"},
    { "id": 5, "name": "Clive"},
    { "id": 6, "name": "Hicks"},
    { "id": 7, "name": "Devin"},
    { "id": 8, "name": "Kate"},
    { "id": 9, "name": "Klien"},
]
friendship = [ (0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
               (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

# Creates connections
for user in users:
    user["friends"] = [] # Creates empty arrays to hold values
for i, j in friendship:
    users[i]["friends"].append(users[j]) # User i is friends with j
    users[j]["friends"].append(users[i]) # User j is friends with i

def number_of_friends(user):
    return(len(user["friends"]))

# calculates the average number of connections on the network
total_connection = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connection // num_users
print(f"The total connections: {total_connection}.\n Number of users: {num_users}.\n  Average Connections: {avg_connections}  " )


num_friends_by_id = [ (user["id"], number_of_friends(user)) for user in users] 
# ??????????????????????????????
sorted(number_of_friends, key=lambda user_id, number_of_fiends: number_of_friends, reverse=True) # what is wrong with this line??
# ??????????????????????????????