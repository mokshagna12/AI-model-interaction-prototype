# text-to-image/generate_image.py
import openai

openai.api_key = 'your_openai_api_key'

def generate_image(prompt):
    response = openai.Image.create(prompt=prompt, n=1)
    image_url = response['data'][0]['url']
    return image_url

if __name__ == "__main__":
    prompt = "A futuristic cityscape"
    print(generate_image(prompt))
 
