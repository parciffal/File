from database import DataConnector
id = '123546'
name = 'Ashot'
status = False

db = DataConnector()
if db.id_cheaker(id) == False:
    db.make_userActive(id)