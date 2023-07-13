from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
  conn_string = os.environ['CONNECTION_STRING']
  conn = psycopg2.connect(conn_string)
  return conn

@app.route('/')
def index():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('SELECT * FROM movies;')
  movies = cur.fetchall()
  response = ""
  for movie in movies:
    response += "<div>"
    response += "<h3>" + str(movie[0]) + " - " + movie[1] + "</h3>"
    response += "<i><p>(" + str(movie[2])+ ")</p></i>"
    response += "<i><p>Director: " + movie[3] + "</p></i>"
    response += "<p>" + movie[5]+  "</p>"
    response += "<i><p>Rating: " + str(movie[4]) +" / 5</p></i>"
    response += "<i><p>Added" + str(movie[6]) + "</p></i>"
  cur.close()
  conn.close()
  return response

app.run(host='0.0.0.0', port=8080)
