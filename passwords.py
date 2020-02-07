import sqlite3
from interface import run
"""
	TODO: 7. find the way to make installer
		  8. icon   
		  9. android version
		  10. upgrade password generator ???
"""

conn = sqlite3.connect('password.sql')
c = conn.cursor()

sql = """CREATE TABLE passwords(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		service TEXT,
		login TEXT,
		password TEXT);
		"""


def main():
	try:
		c.execute(sql)
		run()
	except:
		run()


if __name__ == "__main__":
	main()
