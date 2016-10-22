#!/usr/bin/env python

""" Playing around with basic pg read access, from Python
    mainly stuff I copied from: http://www.jmapping.com/getting-started-with-scripted-geo-data-processing-postgresql-postgis-python-and-a-little-ogr/
"""

import psycopg2#, urllib, zipfile, os

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

# Simple read 
sqlSimpleSelect = 'SELECT komnr FROM samp.ers_zonekort GROUP BY komnr;'
cur.execute(sqlSimpleSelect)
for row in cur:
    print row

conn.commit() ## commits pending transactions to the db (making them persistent). This is needed for sql that modifies data or creates objects.
cur.close()
conn.close()

print "Done..."

