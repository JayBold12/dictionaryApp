import requests

def get_word_definition(term: str):
    dictionary_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    url = dictionary_URL + term
    response = requests.get(url)
    
    if response.status_code == 200:
        word_data = response.json()
        meanings = word_data[0]["meanings"]
        for meaning in meanings:
            part_of_speech = meaning["partOfSpeech"]
            print(part_of_speech)
    else:
        print(f"Problem with this request: ERROR CODE {response.status_code}")
        error_data = response.json()
        title = error_data['title']
        print(title)
        message = error_data['message']
        print(message)
        resolution = error_data['resolution']
        print(resolution)

def generate_a_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    
    if response.status_code == 200:
        word_data = response.json()
        return word_data[0]
    else:
        print(f"Problem with this request: {response.status_code}")


word = generate_a_word()
print(word + "\n")
#word = input("Enter a word you would like to look up: ")
get_word_definition('concealing')