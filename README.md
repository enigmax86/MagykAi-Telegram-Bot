# MagykAi-Telegram-Bot

# WittyWeather Telegram Bot Documentation   ![image](https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/55008fb2-a134-4b3a-8eac-6badd10feb7b)


WittyWeather is a Telegram bot designed to provide weather reports with a touch of sarcasm and personality. This documentation will guide you through the functionality of the bot and how to interact with it.

### Personality 
WittyWeather ```@wittyweatherbot``` is more than just a weather bot with personality full of Saracasm and mischef and this is evident from his replies and the way he adds a touch Sarcasm to everything he is asked to convey. WittyWeather not only provides its users with the required weather reporting but it tries to reaches farther adding more and more to the experience of its users which is through its additional features like ```/funfact``` , ```/trivia``` , ```/summary``` , suggesting correction for mistaken or old city names , Asking for ```citytrivia``` 

Example for fun : <img src="https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/bbca4622-1902-4c40-bcf4-06af6549ab3d" alt="Image Description" width="400" >


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

---
---
### 1. General Commands
 WittyWeather supports the following general commands:

- ```/start```: Initiates the bot and provides an introduction of WitttyWeather and its personality along with a random funny quote or interesting weather fact.
<img src="https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/2d9ec69c-7773-4974-8148-3ed812d80d88" alt="start command" width="400">

---

- ```/help```: Displays a help message with instructions on how to use the bot.
 <img src="https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/b80202a2-006f-48b3-b255-d60290da059f" alt="help command" width="400">

---

- ```/hello```: Greets the user with his name and with a sarcastic message
 <img src="https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/ba6ea3a7-72a4-4c1e-b1bc-f36058f10dfc" alt="hello command" width="400">

---
---

### 2. Weather Reporting and Follow Ups
Commands related to weather reporting and follow-ups:

1. ``` /weather <city_name> ```: Fetches the current weather report for the specified city along with a fun fact about the city (Ofcourse with a sarcastic touch) 
<img src= "https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/3b0db50a-27a6-4435-8d87-7bde6e3ba6c9" width="300">

---
   - ``` /weather <city_name> ``` Uses GPT 3.5 API to suggest correct city name in case the user mistakens <img src= "https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/e3de4b48-9aac-4ca9-91d2-7b78821aa1e1" width="400">
   - Added an additional command ``` /summary ``` to summarize the weather report and include recommendations in WittyWeather's Sarcastic Style

---

2. ``` /summary ```: Can be used after ```/weather <city_name>```  to summarize the weather report with a sarcastic touch.
     <img src="https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/d983968f-a463-44c9-8640-049c1f3c8135" width="300">

---
---

### 3. Other Additions
1.  ``` /funfact ``` : Provides a random weather or geographical fun fact with a sarcastic touch (using GPT 3.5 API )
   <img src="https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/a6e9c523-5df7-4e1f-aafd-695a0c01832f" width="300">
   
---

2.  ``` /trivia ``` : Uses GPT 3.5 API and good prompts to generate new trivia question (But in same dictionary format) to provide a mindboggling experience to the users . Use ```/trivia``` to get the question and type the correct option 
     <img src="https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/10124983-9e55-459e-adc6-d523de2e34f7" width = "400">
     
---

3. ``` city trivia ``` : After you ask for weather report of a city wittyweather asks you if you want a trivia about that city .... Interesting right ?
     <img src = "https://github.com/skillingshark/MagykAi-Telegram-Bot/assets/117962699/400ff27d-5936-4942-820c-05362c4ad8d6" width="300">

---
---
 
