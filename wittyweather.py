



# !pip install requests openai==0.28 telebot pandas

"""## Integrating OpenWeatherMapAPI"""

import requests

key = "f6371c62dd6648c6d3655f12465334f7"

def fetch_response(city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.reason}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None  # Return None to indicate failure

def fetch_weather_report(city_name):
    response = fetch_response(city_name)
    if response:
        return response['main']
    else:
        return None  # Or handle the error in a different way as per your requirement

def to_celcius(temp):
    return round(temp - 273 , 1)

# Function to extract weather details from the API response
def extract_weather_details(city_name):
    response = fetch_response(city_name)
    if response:
        weather = response['weather'][0]
        main = response['main']
        weather_details = {
            'main': weather['main'],
            'description': weather['description'],
            'temp': to_celcius(main['temp']),
            'feels_like': to_celcius(main['feels_like']),
            'temp_min': to_celcius(main['temp_min']),
            'temp_max': to_celcius(main['temp_max'])
        }
        return weather_details
    else:
        return None

fetch_response('Mumbai')
fetch_response('Rome')
extract_weather_details('rome')

"""## Integrating GPT3.5"""

import openai

openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = "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"

def get_gpt_response(message):
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{'role': 'user', 'content': message}],
            max_tokens=4096,
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Sorry, an unexpected error occurred. Please try again later."

def string_data(weather_data):
    weather_string = "## Weather Report:\n"
    for key, value in weather_data.items():
        weather_string += f"{key.capitalize()}: {value}\n"
    return weather_string

message = 'generate a completely new trivia question as a python dict about Mumbai in this format   {"question": "What\'s the term for the type of cloud that looks like a fluffy white pillow and often indicates fair weather? Because, you know, we all need more pillows in the sky.","options": ["Cumulus", "Stratus", "Cirrus", "Nimbostratus"], "answer": "A"} do not forget to add a sarcastic touch'

get_gpt_response(message)

# # Function to get a fun fact, joke, or weather-related pun using GPT-3.5
# def get_fun_fact():
#     prompt = "Generate a fun fact, joke, or weather-related pun."
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=100
#     )
#     return response.choices[0].text.strip()

# List of funny quotes
funny_quotes = [
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "I'm on a whiskey diet. I've lost three days already.",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "I used to play piano by ear, but now I use my hands.",
    "I'm reading a horror book in Braille. Something bad is about to happen, I can feel it!",
    "I'm so good at sleeping, I can do it with my eyes closed.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "I told my computer I needed a break, and now it won't stop sending me vacation ads.",
    "I'm on a seafood diet. I see food and I eat it!"
]

# List of interesting weather facts
weather_facts = [
    "The highest temperature ever recorded on Earth was 134 degrees Fahrenheit (56.7 degrees Celsius) in Death Valley, California, USA.",
    "Lightning bolts can travel at speeds of up to 130,000 miles per hour (210,000 kilometers per hour).",
    "A single cloud can weigh more than 1 million pounds (450,000 kilograms).",
    "The largest hailstone ever recorded weighed 2.25 pounds (1.02 kilograms) and fell in Vivian, South Dakota, USA, on July 23, 2010.",
    "Rainbows are actually full circles, but we only see half of them because the ground blocks the other half.",
    "The coldest temperature ever recorded on Earth was -128.6 degrees Fahrenheit (-89.2 degrees Celsius) at the Soviet Union's Vostok Station in Antarctica on July 21, 1983.",
    "Thunderstorms are more likely to occur in the afternoon because the sun heats the Earth's surface, causing warm air to rise and create unstable atmospheric conditions.",
    "Tornadoes can occur on every continent except Antarctica.",
    "The term 'heat lightning' refers to the faint flashes of lightning on the horizon that are too far away to hear the accompanying thunder.",
    "Meteorologists use a scale called the Beaufort Scale to measure wind speed, ranging from 0 (calm) to 12 (hurricane-force)."
]

# List of sarcastic messages for quiz completion
sarcastic_completion_messages = [
    "Oh joy, you've completed the quiz! Who knew answering questions about weather could be so thrilling?",
    "Well, you made it through the quiz. I hope you enjoyed this riveting experience of weather-related interrogation.",
    "Congratulations, you've reached the end of the quiz! Try not to let the excitement overwhelm you.",
    "Quiz complete! I'll just sit here and wait for the applause to die down. Or not."
]

# List of sarcastic messages for ending the quiz
sarcastic_end_quiz_messages = [
    "Quiz ended. I guess you've had enough of my sarcastic charm for now. Until we meet again!",
    "Oh, is the quiz over already? Don't worry, I'll try not to miss you too much.",
    "And just like that, the quiz comes to an end. It's been real, folks. Or has it?",
    "That's it for the quiz! But don't worry, I'll be back with more opportunities to test your patience soon."
]

# List of sarcastic messages for correct answers
sarcastic_correct_messages = [
    "Congratulations, you managed to get one right! I guess even a broken clock is right twice a day. 🎉",
    "Well done, you actually got one right! Color me impressed. Or not.",
    "Congratulations, you managed to choose the least incorrect option. You must be thrilled.",
    "Hooray, you got it right! The stars have aligned, and you've answered a weather trivia question correctly."
]

# List of sarcastic messages for incorrect answers
sarcastic_incorrect_messages = [
    "Incorrect. 😞 But hey, who needs correct answers when you can have fun, right?",
    "Oops! Looks like someone needs to brush up on their weather knowledge. Or not.",
    "Nice try, but that answer is as incorrect as it gets. Better luck next time. Or not.",
    "Incorrect. But hey, at least you're consistent. Consistently wrong, that is."
]

"""## Importing Libraries"""

import telebot
import random

from telebot import types
from random import shuffle
import json

import pandas as pd



# weather_questions = easy_weather_questions + tough_weather_questions

"""API KEY and BOT Initiation"""

API_KEY = "6768322907:AAE4_IXIOLV76-bIHwCj6sGqvGL5u1i7yLU" #wittyweather
bot = telebot.TeleBot(API_KEY)

"""## Main Codeblock containing the Functions

## 01 Defining General commands [ /start , /help , /hello ]
- Added a Random fact or joke at the end of **/start** response *(Using List)*
- Added Sarcastic messages ( Lost your way ? Need Help ? use **/help** )
- Made **/help** text more sassy
- Added first name and a sarcastic greeting in **/hello** *(Using GPT 3.5 API)*

## 02 Handling Weather Report Response and Follow Ups ( Like City Based Trivia , City Based Fun Facts , Weather Summarization and Travel Recommendation)
Follow Ups
- Like City Based Trivia
- City Based Fun Facts
- Weather Summarization and Travel Recommendation

#### Added Features and Sarcastic Personality of WeatherWhiz in his weather reporting
- Use */weather <city_name>* to get weather report of the city along with a **Fun Fact** about the city
- In case use entered an incorrect city name, the bot would suggest you the correct city name in his sarcastic and humorous style
- After reporting the weather details the bot prompts you for a **Trivia** about the city ( Ofcourse with his **Sarcastic touch** )and choose to play the trivia for as many questions as you want


Technical Error Resolution
- Added Dataframe to handle global variables

## 03 Trivia
- Use /trivia to start the weather trivia
- Answer by typing the correct option ( a , b , c , d)
- The responses would be handled by the response handler and you will get to know whether you are correct or wrong
- You will be asked If you want 1 more trivia question ( Select Yes or No from the virtual buttons ) and it will continue
- use /end_quiz to
"""

#----------------------------------------------------------------------------- 01 : Defining General commands [ /start , /help , /hello ] -------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# Function to present a random funny quote or interesting weather fact with the start message
def present_random_fact_or_quote():
    random_int = random.randint(0,1)
    if(random_int):
      random_message = [str('random fact'),random.choice(weather_facts)]

    else:
      random_message = [str('joke'),random.choice(funny_quotes)]

    return random_message

# Function to handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
    # print(message.from_user.first_name)
    first_name = message.from_user.first_name
    greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
    description = f"{random.choice(greetings)} *{first_name}*, I'm *WittyWeather* 🌤️, your cheerful and quirky weather companion\! " \
                  "I bring a ray of sunshine even on the cloudiest days. \n\n " \
                  "Just type /weather *<city name>* to get the current weather forecast for any city. \n\n" \
                  "You can also say /hello for some fun interactions! ☀️🌈 \n\n"\
                  f"Btw here's a {present_random_fact_or_quote()[0]} to brighten your day: \n\n'{present_random_fact_or_quote()[1]}' \n\n"\
                  "Whenever feeling like a digital tumbleweed .... Just cry for help with '/help' and watch the magic unfold. Easy-peasy!"
    bot.reply_to(message, description , parse_mode="Markdown")



@bot.message_handler(commands=['help'])
def help(message):
    help_text = "Need a hand navigating WittyWeather's unpredictable forecasts? Here's your cheat sheet:\n\n" \
            "To summon the current weather for a place, just type:\n" \
            "/weather <city_name> 🏙️\n\n" \
            "For example, if you're dying to know Mumbai's latest weather tantrum, type: /weather London\n\n" \
            "/funfact : Use /funfact for a random weather funfact 🎉\n\n"\
            "/trivia: Feeling brave? Test your weather and geography IQ with our riveting trivia questions! Just type /trivia and start guessing (or Googling, we won't judge) 🤔\n\n" \
            "/end_quiz: Ready to bail out from the trivia? Simply type /end_quiz. 🚪\n\n" \
            "Let's sprinkle some fake sunshine on your day with our so-called 'delightful' weather updates and 'charming' banter! ☀️🌈"
    bot.reply_to(message, help_text )


# Command to say hello
@bot.message_handler(commands=['hello'])
def hello(message):
  first_name = message.from_user.first_name
  prompt = f"Greet *{first_name}* breifly as a Sarcastic weather bot named *WittyWeather* (Don't forget to add your Sarcastic touch) (Use text formatting (Bold , italics ) and emojis according to MarkdownV1)"
  gpt_response = get_gpt_response(prompt)
#   print(gpt_response)
  reply = f'{gpt_response}  \n\n Wanna try a random weather funfact ? Use /funfact  \n\n Lost your way need some help ? Use /help'
#   print(reply)
  bot.send_message(message.chat.id, reply , parse_mode='Markdown')


@bot.message_handler(commands=['funfact'])
def give_funfact(message):
    seed = random.randint(1,1000)
    prompt = f"Tell me the {seed}th weather funfact. (Don't forget to add a sarcastic touch)"
    gpt_response = get_gpt_response(prompt)
    reply = f'{gpt_response} \n\n Use /funfact to another one 🫠.... Or \n Use /trivia for some braintoasting 🤯 trivia questions (Ofcourse in my sassy style 💁)'
    bot.send_message(message.chat.id , reply)




#----------------------------------------------------------------------------------- 02 : Handling Weather Report Response and Follow Ups (City Trivia)-----------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#





# Function to determine if a message is a city weather request
# Format /weather <city_name>
def weather_request(message):
  request = message.text.split()
  if len(request) < 2 :
    return False
  else:
    return True

def extract_city_name(message):
    # Split the message into words
    print(message.text)
    words = message.text.split()
    # The city name starts after the command (usually the first word)
    # Join all words after the command to form the city name
    city_name = ' '.join(words[1:])
    return city_name

city_list = ['city']
ques_data_list = ['empty']
round_list = [0]
weather_data = ['empty']
weather_ques_data = ['empty']
weather_df = pd.DataFrame({'city_name' : city_list , 'question_data': ques_data_list , 'round' : round_list , 'weather_data' : weather_data , 'weather_question_data' : weather_ques_data})

# @bot.message_handler(func=weather_request)
@bot.message_handler(commands=['weather'])
def send_weather_report(message):
    global messagechatid
    messagechatid = message.chat.id
    if weather_request(message):
        print("hello")
        weather_df['city_name'][0] = extract_city_name(message)
        city_name = weather_df['city_name'][0]
        print(city_name)
        weather = extract_weather_details(city_name)
        # weather_df['weather_data'][0] = string_data(weather)
        if weather:
            print(weather)
            weather_string = string_data(weather)
            weather_df['weather_data'][0] = weather_string
            prompt = f'{weather_string} Present this weather data above in bulletin form with a sarcastic fun fact about the city {city_name} (Adjust formatting and emojis accordingly)'
            #   print(mssg)
            #   print(type(mssg))
            weather_mssg = get_gpt_response(prompt)
            #   print(weather_mssg , type(weather_mssg))
            description = weather_mssg + '\n Too lazy to read ? Get it summarized in my style /summary'
            bot.send_message(message.chat.id, description)
            weather_df['round'][0] = 0
            ask_for_question_about_city(message.chat.id)

        else:

            # prompt = f'Generate the response for an incomplete command : {message.text} , Reply in very short line like this " Did you mean ....*/weather <correct_cityname>*" ( ## Do not forget to add a sarcastic touch to the reply based on the incomplete or the complete command *very important*) (make sure you suggest the latest city name which closely connects to the incorrect command) (Use character formatting and emojis accordingly)'
            # reply = get_gpt_response(prompt)
            # # bot.send_message(message.chat.id,"Looks like you've stumbled upon a city straight out of fairy tales! Sorry, my weather magic only works for real places. But hey, who needs real when you've got imagination? 🌟🔮")
            # bot.send_message(message.chat.id,reply , parse_mode='Markdown')
            suggest_city_correction(message.text)
    else:
            bot.send_message(message.chat.id,random.choice(missing_city_replies) , parse_mode="Markdown")

def gen_weather_report(cityname):
    weather = extract_weather_details(cityname)
        # weather_df['weather_data'][0] = string_data(weather)
    # global messagechatid
    if weather:
        print(weather)
        weather_string = string_data(weather)
        weather_df['weather_data'][0] = weather_string
        prompt = f'{weather_string} Present this weather data above in bulletin form with a sarcastic fun fact about the city {cityname} (Adjust formatting for markdownV1 and emojis accordingly)'
        #   print(mssg)
        #   print(type(mssg))
        weather_mssg = get_gpt_response(prompt)
        #   print(weather_mssg , type(weather_mssg))
        description = weather_mssg + '\n Too lazy to read ? Get it summarized in my style /summary'
        bot.send_message(messagechatid, description , parse_mode = "Markdown")
        weather_df['round'][0] = 0
        ask_for_question_about_city(message.chat.id)

    else:
        suggest_city_correction(f'.weather {cityname}')



def suggest_city_correction(messagetext):
    global messagetextcopy

    prompt = f'Generate the response for an incomplete command : {messagetext} , Reply in very short line like this " Did you mean ....*/weather <correct_cityname>*" ( ## Do not forget to add a sarcastic touch to the reply based on the incomplete or the complete command *very important*) (make sure you suggest the latest city name which closely connects to the incorrect command) (Use character formatting and emojis accordingly)'
    reply = get_gpt_response(prompt)
    prompt2 = f'give me the city name from this text {reply} '
    cityname_reply = get_gpt_response(prompt2)
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text=f"/weather {cityname_reply}"))
    keyboard.add(types.KeyboardButton(text="Noo"))
    messagetextcopy = f"/weather {cityname_reply}"
    bot.send_message(messagechatid, reply , reply_markup=keyboard)

# Function to handle user response to whether they want to answer one more trivia question
@bot.message_handler(func=lambda message: message.text.lower() in ['noo'])
def city_correction(message ):
    # global city_name
    # if message.text.lower() == 'yes':
    #     send_question_about_city(message.chat.id)
    if message.text.lower() == 'noo':
      suggest_city_correction(messagetextcopy)



missing_city_replies = [
    "Looks like we're playing hide and seek with the city name. Ready or not, here I don't find you! 🕵️‍♂️",
    "Did you accidentally swallow the city name? Don't worry, I'll wait for it to come back up. 🤔",
    "No city name, huh? Don't worry, I'll just predict the weather based on your current location: *Cloudy with a chance of forgetfulness.* 🌥️🧠",
]

def ask_for_question_about_city(chat_id ):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Yes plzz"))
    keyboard.add(types.KeyboardButton(text="No I'm full"))
    # handle_more_question_response(message , city_name)
    if weather_df['round'][0] == 0:
      bot.send_message(chat_id, f"Do you want to answer a trivia question about {weather_df['city_name'][0]} ?", reply_markup=keyboard)
    else:
      bot.send_message(chat_id, f"Do you want to answer another trivia question about {weather_df['city_name'][0]} ?", reply_markup=keyboard)

# print(message.text)

# Function to handle user response to whether they want to answer one more trivia question
@bot.message_handler(func=lambda message: message.text.lower() in ['yes plzz', "no i'm full"])
def handle_more_question_response(message):
    # global city_name
    print(hello)
    print(message.text)
    if message.text.lower() == 'yes plzz':
        send_question_about_city(message.chat.id)
    elif message.text.lower() == "no i'm full":
        global flag_city_question
        flag_city_question = False
        bot.send_message(message.chat.id, "Alright, no more questions for you. \n\n Need any other help ? Use /help")

global flag_city_question
flag_city_question = False

def send_question_about_city(chat_id):
    global flag_city_question
    flag_city_question = True
    ques_format = "{\"question\": \"What's the term for the type of cloud that looks like a fluffy white pillow and often indicates fair weather? Because, you know, we all need more pillows in the sky.\", \"options\": [\"Cumulus\", \"Stratus\", \"Cirrus\", \"Nimbostratus\"],\"answer\": \"A\"}"
    prompt = f"generate a completely new trivia question as text about the city  {weather_df['city_name'][0]} in this format {ques_format} \n do not forget to add a sarcastic touch "
    gpt_response =  get_gpt_response(prompt)
    # print(gpt_response)
    weather_df['question_data'][0] = gpt_response
    # print(weather_df['question_data'][0])
    # print(type(weather_df['question_data'][0]))
    question_data = json.loads( weather_df['question_data'][0] )
    print(question_data)
    question_text = f"Question : {question_data['question']}\n\n"
    options_text = "\n".join([f"{chr(65 + i)}. {option}" for i, option in enumerate(question_data['options'])])
    bot.send_message(chat_id, question_text + options_text)



@bot.message_handler(commands=['summary'])
def send_weather_summary(message):
    try:
        print("hello")
        print(weather_df)
        weather_string = weather_df['weather_data'][0]
        print(weather_string)
        prompt = f'You are an expert in weather reporting and you have your own way of summarizing the weather with a Sarcastic touch. Summarize the weather data given below with your Sarcastic touch \n weather_data : {weather_string}'
        prompt2 = "Don't use any entities which can't parsed through telegram api"
        gpt_response = get_gpt_response(prompt)
        print(gpt_response)
        description = f'{gpt_response} \n\n Wanna try a random weather funfact ? Use /funfact .... Or \n Use /trivia for a braintoasting 🤯 trivia (Ofcourse in my sassy style 💁  '
        bot.send_message(message.chat.id, description )

    except Exception as e:
        description = f"An error occurred: {e}"
        # bot.reply_to(message, description , parse_mode="Markdown")
        print(f"An error occurred: {e}")

def check_city_flag():
  return flag_city_question

# Function to handle user responses to quiz questions
@bot.message_handler(func=lambda message: check_city_flag() and message.text.upper() in ['A ', 'B', 'C', 'D'])
def handle_quiz_response(message):
    print(flag_city_question)
    # Check if the message is a response to a quiz question
    if message.text.upper() in ['A', 'B', 'C', 'D']:
        # Get the question number from the message text
        # question_number = int(message.text) - 1
        # Check if the answer is correct
        try:
            if message.text.upper() == json.loads(weather_df['question_data'][0])['answer']:
                bot.reply_to(message, random.choice(sarcastic_correct_messages))
                result = 1
                ask_for_more_question(message.chat.id , result)
            else:
                bot.reply_to(message, random.choice(sarcastic_incorrect_messages) + + f"\n\n Btw the correct answer is {json.loads(weather_df['weather_question_data'][0])['answer']} 🤫")
                result = 0
                ask_for_more_question(message.chat.id , result)
          # Send the next question or end the quiz
      # Check if the message is a command to end the quiz
        except:
            if message.text.upper() == json.loads(weather_df['weather_question_data'][0])['answer']:
                bot.reply_to(message, random.choice(sarcastic_correct_messages))
                result = 1
                ask_for_more_question(message.chat.id , result)
            else:
                bot.reply_to(message, random.choice(sarcastic_incorrect_messages) + + f"\n\n Btw the correct answer is {json.loads(weather_df['weather_question_data'][0])['answer']} 🤫")
                result = 0
                ask_for_more_question(message.chat.id , result)
    # Check if the message is a command to end the quiz
    elif message.text.lower() == '/end_quiz':
        bot.send_message(message.chat.id, random.choice(sarcastic_end_quiz_messages))




#--------------------------------------------------------------------------------------- 03 : WEATHER TRIVIA -----------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# def gen_qno():
#     return random.randint(0,len(weather_questions)-1)


# Function to start the weather quiz
global_qno = -1
@bot.message_handler(commands=['trivia'])
def start_quiz(message):
    # Send the welcome message and first question
    bot.reply_to(message, "Oh great, another trivia quiz! Prepare yourself for some weather-related intellectual gymnastics. Let's get started, shall we?")
    send_question(message.chat.id)

# Function to send a question to the user
def send_question(chat_id):
    ques_format = "{\"question\": \"What's the term for the type of cloud that looks like a fluffy white pillow and often indicates fair weather? Because, you know, we all need more pillows in the sky.\", \"options\": [\"Cumulus\", \"Stratus\", \"Cirrus\", \"Nimbostratus\"],\"answer\": \"A\"}"
    prompt = f"generate a  new and different trivia question based on maybe geography , maybe weather, maybe science and in this format {ques_format} \n do not forget to add a sarcastic touch "
    gpt_response =  get_gpt_response(prompt)
    weather_df['weather_question_data'][0] = gpt_response
    question_data = json.loads( weather_df['weather_question_data'][0] )
    print(question_data)
    question_text = f"Question : {question_data['question']}\n\n"
    options_text = "\n".join([f"{chr(65 + i)}. {option}" for i, option in enumerate(question_data['options'])])
    bot.send_message(chat_id, question_text + options_text)



# Function to ask the user if they want to answer one more trivia question
def ask_for_more_question(chat_id , result):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Yes"))
    keyboard.add(types.KeyboardButton(text="Not for now"))
    bot.send_message(chat_id, "Do you want to answer one more trivia question?", reply_markup=keyboard)

# Function to handle user response to whether they want to answer one more trivia question
@bot.message_handler(func=lambda message: message.text.lower() in ['yes', 'not for now'])
def handle_more_question_response(message):
    if message.text.lower() == 'yes':
        send_question(message.chat.id)
    elif message.text.lower() == 'not for now':
        bot.send_message(message.chat.id, "Alright, no more questions for you. Until next time!")


# Function to handle user responses to quiz questions
@bot.message_handler(func=lambda message: message.text.upper() in ['A', 'B', 'C', 'D'])
def handle_quiz_response(message):
    # Check if the message is a response to a quiz question
    if message.text.upper() in ['A', 'B', 'C', 'D']:
        # Get the question number from the message text
        # question_number = global_qno
        # Check if the answer is correct
        # if message.text.upper() == weather_questions[question_number]['answer']:
        try:
            if message.text.upper() == json.loads(weather_df['weather_question_data'][0])['answer']:
                bot.reply_to(message, random.choice(sarcastic_correct_messages))
                result = 1
                ask_for_more_question(message.chat.id , result)
            else:
                bot.reply_to(message, random.choice(sarcastic_incorrect_messages) + f"\n\n Btw the correct answer is {json.loads(weather_df['weather_question_data'][0])['answer']} 🤫")
                result = 0
                ask_for_more_question(message.chat.id , result)
          # Send the next question or end the quiz
      # Check if the message is a command to end the quiz
        except:
            print(weather_df.head())
            if message.text.upper() == json.loads(weather_df['question_data'][0])['answer']:
                bot.reply_to(message, random.choice(sarcastic_correct_messages))
                result = 1
                ask_for_more_question(message.chat.id , result)
            else:
                bot.reply_to(message, random.choice(sarcastic_incorrect_messages) + f"\n\n Btw the correct answer is {json.loads(weather_df['weather_question_data'][0])['answer']} 🤫")
                result = 0
                ask_for_more_question(message.chat.id , result)

    elif message.text.lower() == '/end_quiz':
        bot.send_message(message.chat.id, random.choice(sarcastic_end_quiz_messages))

#--------------------------------------------------------------------------------------------------------------------------#

@bot.message_handler(func=lambda message: True)
def handle_error(message):
    reply  = f"I didn't understand that \n Maybe you need some help .... /help"
    bot.reply_to(message , reply)




print("-----------------------------------------------Loading @wittyweatherbot---------------------------------------------------------------")
print("-----------------------------------------------Loading @wittyweatherbot 2222222222222222222222222222222222222222222222222---------------------------------------------------------------")

bot.polling()
