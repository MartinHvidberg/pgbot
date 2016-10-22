#!/usr/bin/env python
# -*- coding: utf-8 -*- 

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
# e.g. komnr must be in [100..999]
sql_bot = "select * from "+tbl_funa+" where not komnr BETWEEN 100 AND 999;"
cur.execute(sql_bot)
for row in cur:
    print "Violation mode 1: " + str(row)
# e.g. zone must be in [1..3]
sql_bot = "select * from "+tbl_funa+" where not zone BETWEEN 1 AND 3;"
cur.execute(sql_bot)
for row in cur:
    print "Violation mode 2: " + str(row)
# e.g. zonestaatus must love ["Byzone", "Sommerhusområde", "Landzone"]
sql_bot = "select * from samp.ers_zonekort where not zonestatus IN ('Byzone', 'Sommerhusomr�de', 'Landzone');"
cur.execute(sql_bot)
for row in cur:
    print "Violation mode 3: " + str(row)


cur.close()
conn.close()
print "Done..."

