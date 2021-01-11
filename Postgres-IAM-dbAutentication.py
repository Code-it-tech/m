# Python Script to Authenticate a IAM user with RDS AUthenticate Policy attached to an RDS where we already have same user with GRANT access Permission

import boto3
import sys
import psycopg2 
from psycopg2 import sql

# USername of Instance : e911DeVadmin
# Password of Instance : NextNav#2020

ENDPOINTS = "e911dev-rds-instance-2.ce7tdtnmakzo.us-east-2.rds.amazonaws.com"
PORT =      "5432"
USR =       "test_iam_dbauth_role"
REGION =    "us-east-2"
DBNAME =    "test_iam"

session = boto3.Session(profile_name='795577991693_AWSAdministratorAccess')
client  = boto3.client('rds')



token = client.generate_db_auth_token(DBHostname=ENDPOINTS,Port=PORT,DBUsername=USR,Region= REGION)
print("Printing Token\n")
print(token)
try:

  conn = psycopg2.connect(host=ENDPOINTS, port=PORT,database=DBNAME, user=USR, password=token)
  cur = conn.cursor()
  
  cur.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
  cur.execute("INSERT INTO  customers (name, address) VALUES ('Sagar', 'India')")
  # cur.execute("""SELECT now()""")
  
  query_results = cur.fetchall()
  print(query_results)

except Exception as e:
   print("Database connection failed due to {}".format(e))     



