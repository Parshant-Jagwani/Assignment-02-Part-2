from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask with PostgreSQL!'

# PostgreSQL configuration
db_params = {
    'dbname': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword',
    'host': 'database',  # This should match the service name defined in docker-compose.yml
    'port': '5432',
}

@app.route('/data')
def data():
    # Fetch data from PostgreSQL
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mytable;")
    data = cursor.fetchall()
    connection.close()

    return f'Hello, Flask with PostgreSQL! Data from PostgreSQL: {data}'

@app.route('/new-feature')
def new_feature():
    # Insert data into PostgreSQL
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mytable (column1, column2) VALUES ('value1', 'value2');")
    connection.commit()
    connection.close()

    return 'This is the new feature! Data posted to PostgreSQL.'

if __name__ == '__main__':
    app.run(debug=True)