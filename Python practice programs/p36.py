#Valid keyword or not
import keyword
def isKeyword(word) :
	keyword_list = keyword.kwlist

	if word in keyword_list :
		return "Yes"
	else :
		return "No"

if __name__ == "__main__" :

	print(isKeyword("deep"))
	print(isKeyword("for"))

