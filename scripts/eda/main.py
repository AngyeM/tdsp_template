import psycopg2 as pgsql
import pandas as pd

cnx=pgsql.connect(**dbcnx)
cursor=cnx.cursor()


def get_data():
     query='select * from view_test_supports'
     cursor.execute(query)
     column_names = [column[0] for column in cursor.description]
     cursor_data = cursor.fetchall()
     data_list = [dict(zip(column_names, row)) for row in cursor_data]
     cursor.close()
     df = pd.DataFrame(data_list)
     return df