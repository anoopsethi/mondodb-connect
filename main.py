import pymongo
from pymongo import MongoClient
import random
from faker import Faker

# Initialize the Faker library
fake = Faker()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
database = client['mydatabase']
collection = database['mycollection']

# Function to generate random data
def generate_random_data(num_entries):
    data = []
    for _ in range(num_entries):
        entry = {
            'name': fake.name(),
            'address': fake.address(),
            'email': fake.email(),
            'age': random.randint(18, 80),
            'phone_number': fake.phone_number(),
            'occupation': fake.job()
        }
        data.append(entry)
    return data

# Insert random data into the collection
def insert_random_data(num_entries):
    data = generate_random_data(num_entries)
    collection.insert_many(data)
    print(f"Inserted {num_entries} entries into the database.")

if __name__ == "__main__":
    num_entries = 100  # Change this to the number of random entries you want to add
    insert_random_data(num_entries)
