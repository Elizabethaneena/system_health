import os

def display_avail_RAM():
	memory = os.popen('free -m').read()	 
	print(f'___Available memory___ :\n  {memory}')

def display_load_average():
	commands = os.popen('cat /proc/loadavg').read()
	print(f"\nLoad average : {commands}")
def hostname_details():
	cmd = 'hostnamectl status'
	res = os.popen(cmd).read()
	print('___Host name details___')
	print(res)

def all_process_count():
	cmd = 'ps -a | wc -l'
	res = os.popen(cmd).read()
	print('___All process count___')
	print(res)

def display_uptime():
	cmd = 'uptime'
	res = os.popen(cmd).read()
	print('___Uptime___')
	print(res)

def main_menu():
	print('1.Display Available RAM')
	print('2.Display Load average')
	print('3.Display Hostname details')
	print('4.Display All process count')
	print('5.Display Uptime')
	print('6.Exit')
   
while True:
	main_menu()
	ch = int(input('Enter the choice : '))
	if ch == 1:
		display_avail_RAM()
	elif ch == 2:
		display_load_average()
	elif ch == 3:
		hostname_details()
	elif ch == 4:
		all_process_count()
	elif ch == 5:
		display_uptime()
	elif ch == 6:
		break
	else:
		print('Invalid choice')
