# A python script that tweets a quote from ChatGPT that will surely go viral

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import api_keys 

openai.api_key = api_keys.openai_key
message_content = "Craft the perfect tweet that will definitely go viral."
user_message = {"role": "assistant", "content": message_content}
message_list = [
    {"role":"system", "content": "You are a trendy young lady who loves to use Twitter."},
    user_message
    ]

bot = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=message_list
)


viral_tweet = bot['choices'][0]['message']['content'].replace('"', '')

#print(viral_tweet)



