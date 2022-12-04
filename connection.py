from multiprocessing import connection
from ssl import _PasswordType
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='sarita@12345')
print(mydb.connection_id)