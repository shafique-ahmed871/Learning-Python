def frequency(text) :
	if not text :
		print("Empty text!")
		return []
	import string
	freq = []
	
	clean_text = text.translate(str.maketrans('' , '' , string.punctuation))
	
	words = [word for word in clean_text.lower().split()]
	
	repeat = [0 for x in  range(len(words))]
	for i  in range(len(words)) :
		if repeat[i] != 0 :
			continue
		count = 1
		fr = {}
		for j in range(i + 1 , len(words)) :
			if words[i] == words[j] :
					count += 1
					repeat[j] += 1
		# adding unique word
		fr['word'] = words[i]
		
		# adding frequency of each word
		fr['frequency'] = count

		#adding each unique word along with frequency
		freq.append(fr)
	return freq

def showFrequency(freq) :
	print("--- Word Frequencies ---")
	if not freq :
		print("Empty Text!")
		return 
	for word in freq :
		print(f"{word['word']}{' ' * (8 - len(word['word']))}: {word['frequency']}")

def showTopWords(freq) :
	print("--- Top 5 Words ---")
	if not freq :
		print("Empty text!")
		return 
	sorted_freq = sorted(freq , key = lambda x : x['frequency'] , reverse = True)[:5]	

	for word in sorted_freq :
		count = word['frequency']
		print(f"{word['word']}{' ' * (8 - len(word['word']))}{'█' * count}{count}")
	if len(sorted_freq) < 5: 
		print(f"There are only {len(sorted_freq)} words in text!")
def showCountWords(freq) :
	if not freq :
		print("Empty text!")
		return 
	sum = 0
	for word in freq :
		sum += word['frequency']
	print(f"Total Words	: {sum}")
	print(f"Unique Words	: {len(freq)}")

def searchWordFrequency(freq) :
	search_word = input("Enter word to search: ")
	index = -1
	for word in range(len(freq)) :
		if search_word.lower() == freq[word]['word'] :
			index = word
			break

	if index != -1 :
		print(f'"{search_word}" appears {freq[index]["frequency"]} times')
	else :
		print(f'"{search_word}" does not appear in text!')		
def main() :
	text = ''
	freq = []
	while True :
		
		print("=== Word Frequency Counter ===")
		print("1. Enter Text")
		print("2. Show All Words Frequencies")
		print("3. Show Top 5 Words")
		print("4. Show Total Word Count")
		print("5. Search Word Frequency")
		print("6. Exit")
		
		while True :
			try :
				choose = int(input("Choose: "))
			except ValueError :
				print("Invalid choose, must be number!")
				continue
			if choose < 1 or choose > 6 :
				print("must choose b/w (1-6)!")
				continue
			break
		match choose :
			case 1 :
				text = input("Enter text: ")
				print('\nText saved successfully')
				freq = frequency(text)

			case 2 :
				showFrequency(freq)

			case 3 :
				showTopWords(freq)

			case 4 :
				showCountWords(freq)

			case 5 :
				searchWordFrequency(freq)

			case 6 :
				print("Goodbye!")
				break
		
main()