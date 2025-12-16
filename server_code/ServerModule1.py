import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#

uri = "mongodb+srv://t1053600121_db_user:KYPk.4rwQHmU5V9@cluster0.lnquhmr.mongodb.net/?appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
@anvil.server.callable
def conect_mongoDB():
  try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
  except Exception as e:
    print(e)

@anvil.server.callable
def create_user(user_name, user_password):
  app_tables.users.add_row(name = user_name, password=user_password)
  return True