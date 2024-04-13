# MagykAi-Telegram-Bot

# WittyWeather Telegram Bot Documentation   ![image](https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/55008fb2-a134-4b3a-8eac-6badd10feb7b)


WittyWeather is a Telegram bot designed to provide weather reports with a touch of sarcasm and personality. This documentation will guide you through the functionality of the bot and how to interact with it.

### Personality 
WittyWeather ```@wittyweatherbot``` is more than just a weather bot with personality full of Saracasm and mischef and this is evident from his replies and the way he adds a touch Sarcasm to everything he is asked to convey. WittyWeather not only provides its users with the required weather reporting but it tries to reaches farther adding more and more to the experience of its users which is through its additional features like ```/funfact``` , ```/trivia``` , ```/summary``` , suggesting correction for mistaken or old city names , Asking for ```citytrivia```
Example for fun : ![image](https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/bbca4622-1902-4c40-bcf4-06af6549ab3d)


## Setup and Running Instructions
### 1. Installation of required python packages

To use WittyWeather, you first need to install the required Python packages. You can do this using pip:
```
!pip install -r requirements.txt
```
### 2. Run the python file using 
```
python wittyweather.py
```
### 3. Access the Telegram bot at 
```
@wittyweatherbot
```
Or
```
t.me/wittyweatherbot
```

## ChatGPT Chat URls 
```
https://chat.openai.com/share/ade967f9-f8b5-4165-a028-69b00ef8db1e
```
```
https://chat.openai.com/share/b4fe0226-b30d-45a2-819f-4fa98db6a072
```
## Script Explanation and Added Functionalities to improve interactions and bot personality
### Personality 
WittyWeather ```@wittyweatherbot``` is more than just a weather bot with personality full of Saracasm and mischef and this is evident from his replies and the way he adds a touch Sarcasm to everything he is asked to convey. WittyWeather not only provides its users with the required weather reporting but it tries to reaches farther adding more and more to the experience of its users which is through its additional features like ```/funfact``` , ```/trivia``` , ```/summary``` , suggesting correction for mistaken or old city names , Asking for ```citytrivia``` 
### 1. General Commands
 WittyWeather supports the following general commands:

- ```/start```: Initiates the bot and provides an introduction of WitttyWeather and its personality along with a random funny quote or interesting weather fact.
- ```/help```: Displays a help message with instructions on how to use the bot.
- ```/hello```: Greets the user with his name and with a sarcastic message

### 2. Weather Reporting and Follow Ups
Commands related to weather reporting and follow-ups:

1. ``` /weather <city_name> ```: Fetches the current weather report for the specified city along with a fun fact about the city (Ofcourse with a sarcastic touch)
        - Uses GPT 3.5 API to suggest correct city name in case the user mistakens ![image](https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/e3de4b48-9aac-4ca9-91d2-7b78821aa1e1)

        - Added an additional command ``` /summary ``` to summarize the weather report and include recommendations in WittyWeather's Sarcastic Style
2. ``` /summary ```: Can be used after ```/weather <city_name>```  to summarize the weather report with a sarcastic touch.


### 3. Other Additions
1.  ``` /funfact ``` : Provides a random weather or geographical fun fact with a sarcastic touch (using GPT 3.5 API )
2.  ``` /trivia ``` : Uses GPT 3.5 API and good prompts to generate new trivia question (But in same dictionary format) to provide a mindboggling experience to the users 
