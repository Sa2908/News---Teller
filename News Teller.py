import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin now")
    print("What Category news do you want to listen :")
    speak("What Category news do you want to listen :")
    print("1 : Business\n2 : Entertainment\n3 : Health\n4 : Science\n5 : Sports\n6 : Technology\n7 : All ")
    speak("Enter the corresponding number for the respective category")
    cat = int(input())
    cat1  = ""
    if cat == 1:
        cat1 = "&category=business"
        print("You have chosen Business")
        speak("You have chosen Business")
    elif cat == 2:
        cat1 = "&category=entertainment"
        print("You have chosen Entertainment")
        speak("You have chosen Entertainment")
    elif cat == 3:
        cat1 = "&category=health"
        print("You have chosen health")
        speak("You have chosen health")
    elif cat == 4:
        cat1 = "&category=science"
        print("You have chosen Science")
        speak("You have chosen Science")
    elif cat == 5:
        cat1 ="&category=sports"
        print("You have chosen Sports")
        speak("You have chosen Sports")
    elif cat == 6:
        cat1 = "&category=technology"
        print("You have chosen Technology")
        speak("You have chosen Technology")
    elif cat == 7:
        cat1 = ""
        print("You have chosen all categories")
        speak("You have chosen all categories")
    else :
        print("You have entered wrong number! Program terminates ")
        speak("You have entered wrong number! Program terminates ")
        exit()


    c = 0
    api_key = "              "      # Enter your api key which you get from newsapi.org
    url = f"http://newsapi.org/v2/top-headlines?country=in{cat1}&apiKey={api_key}"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    number  = news_dict['totalResults']
    speak("Lets begin with the first news")
    for article in arts:
        c = c + 1
        print(article['title'])
        speak(article['title'])
        print(article['description'])
        speak(article['description'])
        print(article['url'])
        print()
        speak("Refer the following link for more")
        if c == number:
            speak("That's it for today")
        else:
            speak("Moving on to the next news please Listen Carefully")

    speak("Thanks for listening...")
