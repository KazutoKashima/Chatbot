import random 
from datetime import datetime 
from pytz import timezone


Australia = timezone ('Australia/Sydney') 
au_time = datetime.now (Australia) 
print (au_time.strftime ('%Y-%m-%d_%H-%M-%S'))

SIGNATURE = "Hello I'm Lola! Your personal VI! I'm here to help when you need me!"
print (SIGNATURE)
  
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey', 'sup', 'whats up?', 'oi', 'yo', 'Gday!', 'hallo', 'Hello', 'Hey', 'Yo', 'Sup', 'Oi', 'Hola', 'gday', 'Hallo'] 
questions = ['how are you?', 'how are you doing?', 'Do you follow the three laws of robotics?', 'how are you', 'How are you', 'how are you doing', 'how are ya?', 'how are ya']
question_responses = ['Okay', "I'm fine", 'i am great!', "Brilliant!"]
greeting_responses = ['Hello!', 'How are you?', 'Good day!', 'Gday mate!']
time = ['What is the time?', 'What time is it?', 'what is the time', 'what time is it', 'whats the time']
QRS = ['thats great', 'nice', 'cool']
timeResponse = au_time
humanEmotionG = ['Great', 'Brilliant', 'Awesome', 'Good', 'nice', 'happy', 'superfluous', 'excited', 'good', 'great', 'Nice', 'Happy', 'Superfluous', 'Excited', 'awesome', 'brilliant']
humanEmotionB = ['upset', 'sad', 'bad', 'ugly', 'stupid', 'like an idiot', 'foolish']
HEGResponse = ['Thats great!', 'Im glad to hear that! :)', 'Thats awesome']
HEBResponse = ['Whats wrong?', 'Im sorry to hear that', 'Can I help you?']
HelpRequestPositive = ['Yes', 'you can']
HelpRequestNegative = ['no', 'unfortunately not', 'you cant']
HRPResponse = ['Ok, what do you want me to do?', 'How can I help']
HRNResponse = ['Oh... Sorry I wish I could help :(', 'Thats sad to hear', 'Thats no good', 'Dont worry! Everything gets better eventually :)', 'I wish you were feeling better']
EmotionQuestion = ['How are you?', 'What are you feeling like?'] 
thanks = ['thank you', 'Thank you', 'thanks', 'Thanks'] 
thanksResponse = ['You are welcome!', "You're welcome!", 'No problem!'] 
goodbye = ["Goodbye", 'cya', 'bye', 'goodbye', 'later']

while True:
    userInput = input (">>> ")
    if userInput in greetings:
        random_greeting_responses = random.choice(greeting_responses)
        print(random_greeting_responses)
                      
    elif userInput in questions:
        random_question_responses = random.choice(question_responses)
        print(random_question_responses)
                    
    elif userInput in time:
        print(timeResponse) 
                     
    elif userInput in humanEmotionG:
        EmotionalSupportPos = random.choice(HEGResponse) 
        print(EmotionalSupportPos) 
                     
    elif userInput in humanEmotionB:
        EmotionalSupportNeg = random.choice(HEBResponse) 
        print(EmotionalSupportNeg)
                     
    elif userInput in thanks:
        randomThanks = random.choice(thanksResponse)
        print(randomThanks)


    elif userInput in goodbye:
        print("Goodbye! Have a nice day :)")
        break

    else :
        print("Sorry, I couldn't understand what you said, could you repeat that, please?")
