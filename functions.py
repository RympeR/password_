import sqlite3


conn = sqlite3.connect('password.sql')
c = conn.cursor()

def save_file():
	with conn:
		c.execute("SELECT service, login, password FROM passwords")
	res = "\n".join(set([str(i) for i in c.fetchall()]))
	return res


def insert(service, login, password):
	if (service != ""):
		with conn:
			c.execute("INSERT INTO passwords (service, login, password) VALUES ( :service, :login, :password)",
					  {'service': service, 'login': login, 'password': password})


def get_data_by_service(service):
	if (service != ""):
		c.execute("SELECT service as service, login as login, password as password FROM passwords WHERE service =:service ",
				  {'service': service})
		res = "\n".join(set([str(i) for i in c.fetchall()]))
		return res
	else:
		c.execute("SELECT service from passwords")
		res = "\n".join(set([str(i) for i in c.fetchall()]))
		return res


def update_pass(password, service, login):
	with conn:
		c.execute("""UPDATE passwords SET password = :passw
					WHERE service = :service AND login = :Login""",
				  {'passw': password, 'service': service, 'Login': login})


def remove_pass_by_service(service, login):
	with conn:
		c.execute("DELETE FROM passwords WHERE service = :service AND login = :Login",
				  {'service': service, 'Login': login})
