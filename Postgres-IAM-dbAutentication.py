# Python Script to Authenticate a IAM user with RDS AUthenticate Policy attached to an RDS where we already have same user with GRANT access Permission

import boto3
import sys
import psycopg2 
from psycopg2 import sql

ENDPOINTS = "iam-dbauth.cn9rmirzyzex.us-east-1.rds.amazonaws.com"
PORT =      "5432"
USR =       "db_test_user"
REGION =    "us-east-1"
DBNAME =    "test_iam"

session = boto3.Session()
client  = boto3.client('rds')

DB_NAME = "some_new_database"

token = client.generate_db_auth_token(DBHostname=ENDPOINTS,Port=PORT,DBUsername=USR,Region= REGION)

try:

  conn = psycopg2.connect(host=ENDPOINTS, port=PORT, database=DBNAME, user=USR, password=token)
  cur = conn.cursor()
  
  cur.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
  cur.execute("INSERT INTO  customers (name, address) VALUES ('Sagar', 'India')")
  cur.execute("SELECT * FROM customers")
  
  query_results = cur.fetchall()
  print(query_results)

except Exception as e:
   print("Database connection failed due to {}".format(e))     



