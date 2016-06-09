
#import MyDB connection module
import MyDB
db = MyDB.DB()

#query to database to select device
query = "SELECT * FROM mapapp_geodata_table;"

#execute the query
db.execute(query)

# print data
print db.cursor.fetchall()
# commit database
db.commit()
db.close()
