import sys

def default():
	print("Hello")

def cat():
	print("meow")

def dog():
	print("Baw")

def main():
	default()


if __name__=="__main__":
	if sys.argv[1] == "dog":
		dog()
	else:
		main()

