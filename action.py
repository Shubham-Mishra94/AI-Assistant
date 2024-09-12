import webbrowser

import Text_to_Speech
import Speech_to_text
import datetime
import weather


def action(data):
    user_data = data.lower()  # (Speech_to_text.speech_to_text())

    if "what is your name" in user_data:
        Text_to_Speech.text_to_speech("My Name is Tom, a virtual assistant")
        return "My Name is Tom, a virtual assistant"

    elif "hello" in user_data:
        Text_to_Speech.text_to_speech("hey, how can I help you?")
        return "hey, how can I help you?"

    elif "good morning" in user_data:
        Text_to_Speech.text_to_speech("good Morning, sir")
        return "good Morning, sir"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = str(current_time) + "Hour: ", str(current_time.minute) + "Minute"
        Text_to_Speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        Text_to_Speech.text_to_speech("Ok, Sir")
        return "Ok, Sir"

    elif "youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        Text_to_Speech.text_to_speech("Youtube is ready for you")
        return "Youtube is ready for you"

    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        Text_to_Speech.text_to_speech("Google is ready for you ")
        return "Google is ready for you "

    elif "naukri" in user_data:
        webbrowser.open("https://www.naukri.com/")
        Text_to_Speech.text_to_speech("Naukri login is ready for you")
        return "Naukri login is ready for you"

    elif "Linkedin" in user_data:
        webbrowser.open("https://www.linkedin.com/")
        Text_to_Speech.text_to_speech("Linkedin Login is ready for you")
        return "Linkedin Login is ready for you"

    elif "weather" in user_data:
        ans = weather.weather()
        Text_to_Speech.text_to_speech(ans)
        return ans

    else:
        Text_to_Speech.text_to_speech("I am Unable to understand")
        return "I am Unable to understand"
