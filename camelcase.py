def camelcase(sentence):
	""" Convert sentence to camelCase, for example, "Display all books" 
	is converted to "displayAllBooks" """

	title_case = sentence.title() # Uppercase first letter of each word
	upper_camel_cased = title_case.replace(' ', '') # remove spaces 
	# Lowercase first letter, join with rest of string 
	# Slices don't produce index out of bounds errors. 
	# So this still works on empty strings, strings of length 1

	return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def banner():
	""" Display program name in banner """
	msg = 'AWSOME camelCaseGenerator PROGRAM'
	stars = '*' * len(msg)
	print(f'\n {stars} \n {msg} \n {stars}\n') 

def instructions():
	inst = "Enter a sentence into the console and it will be trasnformed into a camelcase style variable name!"
	print(inst)

def main():
	banner()
	instructions()
	sentence = input('Enter your sentence: ')
	output = camelcase(sentence)
	print(output)
if __name__ == '__main__':
	main()
