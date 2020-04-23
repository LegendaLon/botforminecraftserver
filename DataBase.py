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

	""" Close """
	def close(self):
		self.cursor.close()
		self.conn.close()
		print("[INFO] Close connect to database, and close cursor")
		
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

	def insert_users(self, funcType:int, user:str, money:int=None, vip:int=None):
		self.connect()

		if funcType == 1:
			try:
				self.cursor.execute('''INSERT INTO users(user) VALUES(?) ''', (str(user),))
			except sqlite3.IntegrityError as e:
				print('[ERROR] sqlite3 ' + e)

		elif funcType == 2:
			self.cursor.execute()

		self.conn.commit()
		self.close()

	def insert_guild(self, funcType:int, guild_id, guild_name=None, channel=None):
		self.connect()

		if funcType == 1 and channel == None:
			try:
				self.cursor.execute('''INSERT INTO guild(guild_id, guild_name) VALUES(?, ?)''', (guild_id, guild_name))
			except Exception as e:
				print('[ERROR] sqlite3 ' + e)

		else:
			print("[ERROR] sqlite3: No func")

		self.conn.commit()
		self.close()

	""" Update in Data Base """
	def update_guild(self, funcType:int, guild_id, channel_join=None):
		self.connect()

		if funcType == 1 and channel_join != None  :
			self.cursor.execute("""UPDATE guild SET channel_join=? WHERE guild_id=? """, (channel_join, guild_id))
		else:
			pass

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
		
		try:
			self.cursor.execute('''DELETE FROM status WHERE id=?''', (id,))

		except Exception as e:
			raise e

		self.conn.commit()
		self.close()

	def delete_guild(self, id):
		self.connect()
		
		try:
			self.cursor.execute('''DELETE FROM guild WHERE guild_id=?''', (int(id),))

		except Exception as e:
			print("[ERROR] sqlite3 " + e)

		self.conn.commit()
		self.close()

	""" Select in Data Base """
	def _select_order_by(self, nameTable:str, sort:str):
		self.connect()
		try:
			request = 'SELECT * FROM {0} ORDER BY {1}'.format(nameTable, sort)
			self.cursor.execute(request)
			data = self.cursor.fetchall()
			return data
		except Exception as e:
			print("[ERROR] sqlite3 " + e)
		self.close()

	def _select_where(self, nameTable:str, elements:str, lines:str):
		self.connect()
		try:
			request = "SELECT * FROM {0} WHERE {1}=?".format(nameTable, elements)
			self.cursor.execute(request, (lines,))
			data = self.cursor.fetchall()
			return data
		except Exception as e:
			print("[ERROR] sqlite3 " + e)
		self.close()

	def _select_all(self, nameTable:str):
		self.connect()
		try:
			request = 'SELECT * FROM {0}'.format(nameTable,)
			self.cursor.execute(request)
			data = self.cursor.fetchall()
			return data
		except Exception as e:
			print("[ERROR] sqlite3 " + e)
		self.close()