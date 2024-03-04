# -*- coding: utf-8 -*-


!pip install -q -U google-generativeai
!pip install gTTS

import textwrap
from gtts import gTTS

import google.generativeai as genai
from IPython.display import display, Markdown, Audio

# Start searching with Google Gemini
from google.colab import userdata

GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Start searching with Google Gemini



model = genai.GenerativeModel('gemini-pro')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#step-1
def ask_question(name):
  ques = f"Hey {name}, what do you want? "
  ques=input(ques)
  return ques

def classify_questions(ques):
  goahead_with_web_search = False
  device_lst = ['alarm', 'reminder', 'message', 'call']
  personal_lst = ['who are you?', 'who created you?']

  device = False
  for i in device_lst:
    if i in ques:
      device = True

  if device:
    print("This question is related to Device things, which is not supported in our Google Assistant!")

  personal_question = False
  for i in personal_lst:
    if i in ques.lower():
      personal_question = True

  if personal_question:
    print("Hey, I am a Personal Assistant created by Rohith.")

  if device or personal_question:
    goahead_with_web_search = False
  else:
    goahead_with_web_search = True

  return goahead_with_web_search

def ask_gemini(ques):
  modified_prompt = f"Hey, give me the answer to this question '{ques}' in a maximum of 40 words: "
  response = model.generate_content(modified_prompt)
  display(to_markdown(response.text))
  return response.text

def speak(answer):
  tts = gTTS(answer)
  tts.save('audio.mp3')
  display(Audio('audio.mp3', autoplay=True))

classify_questions("who are you?")

have_any_other_ques = 'y'
name = ''
while have_any_other_ques=='y':
  if name=='':
    name = input("Hey, what is your name? ")
  q = ask_question(name)

  go_ahead = classify_questions(q)

  answer = ''
  if go_ahead:
    answer = ask_gemini(q)
    speak(answer)
    print(answer)

  have_any_other_ques = input("Do you have any other questions? (y/n) ")
