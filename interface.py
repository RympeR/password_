import tkinter as tk
import tkinter.ttk as ttk
from functions import *
import random
import webbrowser
import os


# window mainloop
def run():
	def f_get_data():
		my_data.delete(0.0, 100.100)
		my_data.insert(1.0, get_data_by_service(text_entry_service.get()))

	def f_help():
		webbrowser.open(os.getcwd() + "/Help.txt")

	def f_about():
		webbrowser.open(os.getcwd() + "/About.txt")

	def f_update():
		update_pass(pass_field.get(), text_entry_service.get(),
					text_entry_login.get())

	def f_save():
		with open("My_passwords.txt", 'w') as f:
			f.write(save_file())

	def f_generate():
		encode_field.delete(0, 40)
		s = random.randint(97, 122)
		res = []
		length = random.randint(8, 20)
		for i in range(length):
			symbol = [random.randint(97, 122), random.randint(48, 57)]
			res.append(chr(symbol[random.randint(0, 1)]))
		if res[0].isalpha():
			res[0].upper()
		else:
			res.extend(chr(s).upper())
		random.shuffle(res)
		result = "".join(res)
		encode_field.insert(0, result)
	
	
	def email_gen():
		print(Email_Check)
		email_entry.delete(0, 40)
		s = random.randint(97, 122)
		res = []
		emails = ['@gmail.com', '@mail.ru', '@ukr.net', '@yahoo.ru']
		length = random.randint(6, 25)
		for i in range(length):
			symbol = random.randint(97, 122)
			res.append(chr(symbol))
		if Email_Check.get() == 0:
			res.extend(emails[Email_Check.get()])
		elif Email_Check.get() == 1:
			res.extend(emails[Email_Check.get()])
		elif Email_Check.get() == 2:
			res.extend(emails[Email_Check.get()])
		elif Email_Check.get() == 3:
			res.extend(emails[Email_Check.get()])
    	
		result = "".join(res)
		email_entry.insert(0, result)


	def f_rem():
		remove_pass_by_service(text_entry_service.get(),
							   text_entry_login.get())

	def f_insert():
		insert(text_entry_service.get(),
			   text_entry_login.get(), pass_field.get())

	app = tk.Tk()

   

	app.title("Password searcher")
	app.resizable(width=False, height=False)
	# init
	mainmenu = tk.Menu(app)
	app.config(menu=mainmenu)

	filemenu = tk.Menu(mainmenu, tearoff=0)
	filemenu.add_command(label='Сохранить', command=f_save)

	helpmenu = tk.Menu(mainmenu, tearoff=0)

	helpmenu.add_command(label="Помощь", command=f_help)
	helpmenu.add_command(label="О программе", command=f_about)

	mainmenu.add_cascade(label="Файл", menu=filemenu)
	mainmenu.add_cascade(label="Справка", menu=helpmenu)

	Email_Check = tk.IntVar()
	Email_Check.set(0)

	Gmail = ttk.Radiobutton(app, text='gmail.com', variable=Email_Check,
								width=20, value=0)						 
	MailRu = ttk.Radiobutton(app, text='mail.ru', variable=Email_Check,
                          		width=20, value=1)
	UkrNet = ttk.Radiobutton(app, text='urk.net', variable=Email_Check,
								width=20, value=2)
	Yahoo = ttk.Radiobutton(app, text='yahoo.ru', variable=Email_Check,
								width=20, value=3)

	email = ttk.Label(app, text='Email')
	email_entry = ttk.Entry(app, width=40)

	my_data = tk.Text(width=30, height=4)
	service_label = ttk.Label(app, text='Service')
	login_label = ttk.Label(app, text='Login')
	output_label = ttk.Label(app, text='Password')
	total_output = ttk.Label(app, text='Full output')
	generate_label = ttk.Label(app, text='Generate')
	pass_field = ttk.Entry(app, width=40)
	text_entry_service = ttk.Entry(app, width=40)
	text_entry_login = ttk.Entry(app, width=40)
	encode_field = ttk.Entry(app, width=40)
	search_btn = ttk.Button(app, text="Search",
							width=10, command=f_get_data)
	update_btn = ttk.Button(app, text='Update Password',
							width=20, command=f_update)
	add_btn = ttk.Button(app, text='Add Password',
						 width=20, command=f_insert)
	rem_btn = ttk.Button(app, text='Remove password',
						 width=20, command=f_rem)
	get_pass = ttk.Button(app, text='Generate',
						  width=10, command=f_generate)
	get_email = ttk.Button(app, text='Get email',
							width=15, command=email_gen)
	# grid
	encode_field.grid(row=4, column=1)
	total_output.grid(row=3, column=0)
	service_label.grid(row=0, column=0)
	generate_label.grid(row=4, column=0)
	text_entry_service.grid(row=0, column=1)
	login_label.grid(row=1, column=0)
	text_entry_login.grid(row=1, column=1)
	output_label.grid(row=2, column=0)
	pass_field.grid(row=2, column=1)
	my_data.grid(row=3, column=1)

	add_btn.grid(row=0, column=2)
	search_btn.grid(row=3, column=2)
	update_btn.grid(row=1, column=2)
	rem_btn.grid(row=2, column=2)
	get_pass.grid(row=4, column=2)
	email.grid(row=5, column=0)
	email_entry.grid(row=5, column=1)
	get_email.grid(row=5, column=2)
	Yahoo.grid(row=3, column=3)
	Gmail.grid(row=4, column=3)
	UkrNet.grid(row=5, column=3)
	MailRu.grid(row=6, column=3)
	
	app.mainloop()
