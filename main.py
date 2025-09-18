from openai import OpenAI
import time
import sys
import pygame
import datetime
# from important import voice

BLUE = "\033[94m"
RESET = "\033[0m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

pygame.mixer.init()
intro=pygame.mixer.Sound("Futuristic HUD_UI Visuals Sound Design.wav")
mid=pygame.mixer.Sound("Artificial intelligence Intro Template.wav")


def typing(text,delay):
    for i in text:
        time.sleep(delay)
        sys.stdout.write(i)
        sys.stdout.flush()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        typing(MAGENTA+f"\n☀️ Good Morning boss! Utho utho... chai bhi ready hai aur Rokz bhi — it's\n"+RESET,0.01)
    elif hour>=12 and hour<18:
        typing(MAGENTA+f"\n🌞 Good Afternoon Sir! Rokz taiyaar hai full energy ke saath — it's\n"+RESET,0.01)
    else:
        typing(MAGENTA+f"\n🌙 Good Evening boss! Yeh hai aapka AI dost Rokz\n"+RESET,0.01)


def ai():
    try:
        intro.play()
        typing(YELLOW+"\n➤  🤖 Rokz: 🎙️ Namaste doston! Main hoon Rokz — aapka AI dost, assistant! 😎💬\n"+RESET,0.02)
        wish()
        time.sleep(3)
        intro.stop()

        while True:
            vm=input(CYAN+"\n‣ 😎 User: "+RESET).lower().strip()

            mid.play()

            if any(word in vm for word in ["exit", "stop", "quit", "cancel","bye"]):
                mid.stop()
                intro.play()
                typing(BLUE + "\n➤  🤖 Rokz: Rokz signing off... but yaad rakhna, main yahin hoon — standby pe! 🚀📴\n" + RESET, 0.02)
                time.sleep(2)
                intro.stop()
                break

            else:
                a4f_api_key = "Enter-Your-API-Key"
                a4f_base_url = "https://api.a4f.co/v1"

                client = OpenAI(
                api_key=a4f_api_key,
                base_url=a4f_base_url,
                )

                completion = client.chat.completions.create(
                model="provider-3/gemini-2.0-flash",
                messages=[
                    {
                        "role": "user",
                        "content": f"{vm}\n\nPlease keep the response short even mid length will also work depend upon the situation or question, and the response should be in hinglish(hindi+english) and better if it would reply like a friend  along with emoji. and in proper format or structure and make it short please."
                    }
                ]
            )
 
                mid.stop()

                intro.play()
                typing(GREEN+f"\n➤  🤖 Rokz: {completion.choices[0].message.content}\n"+RESET,0.02)
                intro.stop()

        #retry function..
        mid.play()
        typing(BLUE+"\n➤  🤖 Rokz: Dubara try karne ha kya, sir ji? Ho sakta hai is baar kuch zabardast ho jaye! 😎✨\n"+RESET,0.02)
        dm=input(CYAN+"‣ 😎 User: "+RESET)
        if dm=='yes' or dm=="ha":
            mid.stop()
            ai()
        else:
            typing(MAGENTA+"\n➤  🤖 Rokz: ✅ Okk sir ji! Shukriya mujhe istemal karne ke liye! 😎🫡\n"+RESET,0.02)
            mid.stop()
            sys.exit()

    except Exception as e:
        typing(RED + f"\n➤  🤖 Rokz: Arre bhai! Kuch toh gadbad ho gayi 😵‍💫\nError: {e}" + RESET, 0.02)


if __name__=="__main__":
    ai()