import sqlite3 as sq


class DataBase:
	def __init__(self, path):
		self.path = path

	""" Connect to Data Base """
	def connect(self):
		try:
			self.conn = sq.connect(str(self.path))
			self.cursor = self.conn.cursor()
		except Exception as e:
			print("[ERROR] File DataBase error: " + e)
		
	""" Create in Data Base """
	def create(self):
		self.cursor.execute(
			'''CREATE TABLE status
			(id integer, status text)'''
		)

	""" Add in Data Base """
	def insert(self, nameTable:str, paramArray):
		self.connect()
		request = 'INSERT INTO ' + nameTable + ' VALUES(?, ?)'
		self.cursor.execute(request, paramArray)

		self.conn.commit()
		self.close()

	def insert_status(self, name:str, author:str):
		self.connect()
		self.cursor.execute('''INSERT INTO status(name, author) VALUES(?, ?)''', (name, author))

		self.conn.commit()
		self.close()

	""" Remove in Data Base """
	def delete(self, nameTable:str, func:str):
		self.connect()
		request = '''DELETE FROM {0} {1}'''.format(nameTable, func)
		self.cursor.execute(request)
		self.conn.commit()
		self.close()

	def delete_status(self, id):
		self.connect()
		self.cursor.execute('''DELETE FROM status WHERE id=?''', (id,))
		self.conn.commit()
		self.close()

	""" Select in Data Base """
	def select_order_by(self, nameTable:str, sort:str):
		self.connect()
		request = 'SELECT * FROM {0} ORDER BY {1}'.format(nameTable, sort)
		self.cursor.execute(request)
		data = self.cursor.fetchall()
		return data
		self.close()

	def select_all(self, nameTable:str):
		self.connect()
		request = 'SELECT * FROM {0}'.format(nameTable,)
		self.cursor.execute(request)
		data = self.cursor.fetchall()
		return data
		self.close()

	""" Close """
	def close(self):
		self.cursor.close()
		self.conn.close()
		print("[INFO] Close connect to database, and close cursor")