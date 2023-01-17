import firebase_admin
import os

from firebase_admin import credentials
from firebase_admin import firestore

# db setup
cred = credentials.Certificate("/Users/yashmathur/Downloads/sprout-akcyl333-firebase-adminsdk-4bq7t-5594ca04c8.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

docs = db.collection("insta").stream()
analytics = {}

for doc in docs: 
    dict = doc.to_dict()
    user = dict["user"]

    if user in analytics: 
        analytics[user] = analytics[user] + 1
    else: 
        analytics[user] = 1

print(analytics)

# Mon Jan 16 4:23 pm
# {
#     'arianagrande': 4979, 
#     'khloekardashian': 4187, 
#     'kyliejenner': 7033, 
#     'zendaya': 1497, 
#     'haileybieber': 2031, 
#     'gigihadid': 3295, 
#     'devonleecarlson': 2485, 
#     'badgalriri': 4862, 
#     'bellahadid': 3308, 
#     'kendalljenner': 644, 
#     'selenagomez': 1860, 
#     'emrata': 1219, 
#     'iamcardib': 1646, 
#     'emmachamberlain': 539, 
#     'kimkardashian': 825, 
#     'matildadjerf': 1644, 
#     'dualipa': 1401, 
#     'staskaranikolaou': 746, 
#     'billieeilish': 672, 
#     'oliviarodrigo': 201, 
#     'kourtneykardash': 516
# }