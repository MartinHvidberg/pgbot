#!/usr/bin/env python

""" Playing around with basic pg read access, from Python
    mainly stuff I copied from: http://www.jmapping.com/getting-started-with-scripted-geo-data-processing-postgresql-postgis-python-and-a-little-ogr/
"""

import psycopg2

import users_and_passwords # Hide the names and passwords in a file not shared as open source...
uap = users_and_passwords.UaP()
#print uap.show()

#DB connection properties
conn = psycopg2.connect(dbname = 'pgv', 
                        host = 'localhost', 
                        port = 5432, 
                        user = uap.id(),
                        password = uap.pw())

cur = conn.cursor()  ## open a cursor

# Hard code a table
tbl_name = 'ers_zonekort'
sch_name = 'samp'
tbl_funa = sch_name+'.'+tbl_name

# Simple read 
sqlSimpleSelect = "SELECT * FROM "+tbl_funa+";"
cur.execute(sqlSimpleSelect)
for row in cur:
    print row

# Find the fields in that table
sql_list_fields = "SELECT column_name, data_type FROM information_schema.columns WHERE table_name ='"+tbl_name+"';"
cur.execute(sql_list_fields)
for row in cur:
    print row



# Check domain violation


cur.close()
conn.close()
print "Done..."

