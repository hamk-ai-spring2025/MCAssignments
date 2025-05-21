
from openai import OpenAI
client = OpenAI()

print('Enter prompt for creative writing:')
userprompt = input()

f = open("CreativeWriterSystemPrompt.txt")
systemprompt = (f.read())


response = client.responses.create(
    model="gpt-4.1",
    instructions=systemprompt,
    input=userprompt
)


with open("CreativeWriterAnswers.txt", "w") as f:
  f.write("User Prompt: ")
  f.write(userprompt)
  f.write("\n")
  f.write("Response: ")
  f.write(response.output_text)
  
print(response.output_text)