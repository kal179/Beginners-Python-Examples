print("Hello,")
while True:
	start_or_end = str(input("Start or End : "))
	print(" ")
	if start_or_end.strip() == "Start":
		get_text = str(input("Text to decode : "))
		get_key = int(input("Key : "))

		decoded = []

		for i in get_text:
			decoded_char = chr(ord(i) - get_key)
			decoded.append(decoded_char)

		decoded_text = ""

		for a in decoded:
			decoded_text = decoded_text + str(a)

		print("Decrypted Text : " + decoded_text)
		print(" ")
		continue
	else:
		break
