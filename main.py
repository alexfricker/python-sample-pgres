import psycopg2

from settings import DB_SETTINGS


def get_pg_connector():
    return psycopg2.connect(
            dbname=DB_SETTINGS["DB_NAME"],
            user=DB_SETTINGS["DB_USER"],
            password=DB_SETTINGS["DB_PASSWORD"],
            host=DB_SETTINGS["DB_HOST"],
            port=DB_SETTINGS["DB_PORT"],
        )


def get_server_version():
    """connect to db and query the current postgres version"""

    pg_con = get_pg_connector()
    cur = pg_con.cursor()
    query = "select version();"

    cur.execute(query)
    single_row_result = cur.fetchone()
    first_column = single_row_result[0]
    print(first_column)

    cur.close()
    pg_con.close()


def create_sample_table():
    """create a table in the database - columns can be dynamically passed in to the query string using variables"""

    pg_con = get_pg_connector()
    cur = pg_con.cursor()
    query = """CREATE TABLE IF NOT EXISTS sample_table (
        id int,
        name VARCHAR(50),
        value VARCHAR(50)
    );"""

    cur.execute(query) #there are no results as this is a DDL operation
    pg_con.commit()

    cur.close()
    pg_con.close()


def create_sample_data():
    """load some sample data into test table"""

    create_sample_table()

    pg_con = get_pg_connector()
    cur = pg_con.cursor()
    query = """INSERT INTO sample_table (id, name, value)
        VALUES (1, 'foo', 'bar')
        ,(2, 'something', 'else')
        ,(3, 'another', 'example')
    """ # see https://www.psycopg.org/docs/usage.html for ways to do this with placeholder variables

    cur.execute(query)
    pg_con.commit()

    cur.close()
    pg_con.close()


def query_sample_data():
    """example query with multiple rows returned"""

    pg_con = get_pg_connector()
    cur = pg_con.cursor()
    query = "SELECT * FROM sample_table;"

    cur.execute(query)
    for row in cur:
        print(row)


def drop_sample_table():
    """clean up sample data"""

    pg_con = get_pg_connector()
    cur = pg_con.cursor()
    query = """DROP TABLE IF EXISTS sample_table;"""

    cur.execute(query)
    pg_con.commit()

    cur.close()
    pg_con.close()


print("\n-----------------------------\nCalling 'get_server_version()':")
get_server_version()

print("\nLoading sample data using 'create_sample_data()'...")
create_sample_data()

print("Querying sample data using 'query_sample_data()'...")
query_sample_data()

print("\nCleaning up...")
drop_sample_table()

print("Done! See main.py for code and links.\n\n")