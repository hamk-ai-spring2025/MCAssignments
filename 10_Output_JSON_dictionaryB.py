from openai import OpenAI
#from google import genai
client = OpenAI()

# This code snippet demonstrates how to use the OpenAI API to create a response

#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print('Enter a word for the dictionary:')
word = input()

prompt = """

Generate a dictionary entry for the word '""" + word + """' in JSON format. use this JSON schema:


{
    "$schema": "http://json-schema.org/draft-07/schema#",
    
    "type": "object",
    "properties": {
        "word": {
            "type": "string",
            "description": "The word being defined."
        },
        "definition": {
            "type": "string",
            "description": "The definition of the word."
        },
        "synonyms": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "List of synonyms for the word."
        },
        "antonyms": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "List of antonyms for the word."
        },
        "examples": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Example sentences using the word."
        }
    },
    "required": ["word", "definition", "synonyms", "antonyms", "examples"]
}

"""



response = client.responses.create(
    model="gpt-4.1",
    input=prompt
)
with open("JSONDictionaryEntry.txt", "w") as f:
  f.write("User word: ")
  f.write(word)
  f.write("\n")
  f.write("JSON entry: ")
  f.write("\n")
  f.write(response.output_text)
print(response.output_text)



