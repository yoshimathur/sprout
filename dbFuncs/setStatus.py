import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore

# db setup
cred = credentials.Certificate("/Users/yashmathur/Downloads/sprout-akcyl333-firebase-adminsdk-4bq7t-5594ca04c8.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# getting previously viewed posts
viewed = {}
counter = 0
docs = db.collection("insta").stream()
for doc in docs: 
    counter = counter + 1
    dict = doc.to_dict()
    name = str(dict["user"])

    if name in viewed: 
        viewed[name].add(doc.id)
    else: 
        viewed[name] = set([doc.id])

for key in viewed: 
    viewed[key] = list(viewed[key])

db.collection("insta").document("status").update(viewed)
print(counter)
