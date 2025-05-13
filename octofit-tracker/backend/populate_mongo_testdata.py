import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['octofit_db']

# Users
users = [
    {"email": "john.doe@example.com", "name": "John Doe"},
    {"email": "jane.smith@example.com", "name": "Jane Smith"}
]
try:
    db.users.insert_many(users, ordered=False)
except Exception as e:
    print("Warnung: ", e)

# Teams
teams = [
    {"name": "Team Alpha"},
    {"name": "Team Beta"}
]
try:
    db.teams.insert_many(teams, ordered=False)
except Exception as e:
    print("Warnung: ", e)

# Activities
activities = [
    {"description": "Running 5km"},
    {"description": "Swimming 1km"}
]
try:
    db.activity.insert_many(activities, ordered=False)
except Exception as e:
    print("Warnung: ", e)

# Leaderboard
leaderboard = [
    {"rank": 1},
    {"rank": 2}
]
try:
    db.leaderboard.insert_many(leaderboard, ordered=False)
except Exception as e:
    print("Warnung: ", e)

# Workouts
workouts = [
    {"title": "Morning Yoga"},
    {"title": "Evening Cardio"}
]
try:
    db.workouts.insert_many(workouts, ordered=False)
except Exception as e:
    print("Warnung: ", e)

print('Testdaten (kompatibel mit älterem MongoDB) eingefügt.')
