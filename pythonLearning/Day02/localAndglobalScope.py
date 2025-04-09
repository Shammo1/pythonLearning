# Define balance globally
balance = 100

def func():
	print(balance)  # Accessible

func()
print(balance)  # Accessible

def chk():
	global balance
	balance = balance - 5

chk()
print(balance)  # Updated balance
