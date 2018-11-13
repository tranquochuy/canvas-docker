import sys
import psycopg2

conn = None
try:
    conn = psycopg2.connect("dbname = 'canvas_development' user = 'canvas' host = 'localhost'")
except psycopg2.DatabaseError as ex:
    print('I am unable to connect the database:', ex)
    sys.exit(1)

curs = conn.cursor()
query = "INSERT INTO access_tokens (created_at, crypted_token, developer_key_id, purpose, token_hint, updated_at, user_id) SELECT now(), '3f719486138dabe7b96f76394032fa7967fbc6ea', dk.id, 'user-token', '', now(), 34 FROM developer_keys dk where dk.email = 'canvas@example.edu';"
curs.execute(query)

conn.commit()

query = "SELECT * FROM access_tokens;"
curs.execute(query)

for row in curs:
    print(row)