def is_palindrome(string):
	result = True
	checks = 0
	for i in range(len(string)//2+1):
		if string[i]==string[-(i+1)]:
			result = True
			checks += 1
		else:
			result = False
			checks += 1
			break
	return result, checks

with open("pi_1million_digits.txt", 'r') as file:
	number = file.readline()
	number = number[:-1]

sizenumber = 28
print(len(number))
finalresult = False
for i in range(len(number)-sizenumber+1):
	subnumber = number[i:i+sizenumber]
	if is_palindrome(subnumber)[0]:
		print(f"{subnumber} is palindrome. It's first digits is in index {i}, its final index is {i+sizenumber-1}")
		finalresult = True
if not finalresult:
	print(f"There was no {sizenumber}-digit palindrome within the first 1.000.000 digits of Pi")