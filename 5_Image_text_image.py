import base64
from openai import OpenAI
import requests
client = OpenAI()

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
image_path = "SourceImage.jpg"

# Getting the Base64 string
base64_image = encode_image(image_path)


response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "user",
            "content": [
                { "type": "input_text", "text": "what's in this image?" },
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
)

#print(response.output_text)
#description =  '"' + response.output_text + '"'
description = (response.output_text)
print (description)

with open("SourcePictureDescription.txt", "w") as f:
  f.write(description)
  
prompt = description  




response = client.images.generate(
    model="dall-e-2",
    prompt=description
)



# Extract the URL of the generated image
image_url = response.data[0].url
image_response = requests.get(image_url)

# Save the image to a file
if image_response.status_code == 200:
    with open('generated_image.png', 'wb') as f:
        f.write(image_response.content)
    print("Image downloaded and saved as 'generated_image.png'")
else:
    print("Failed to download the image")
    
