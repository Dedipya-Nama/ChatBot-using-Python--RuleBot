import re
import random 

class RuleBot: 
    negative_responses = ("no","nah","nope","naw","naawww","not a chance","will not","do not","none","sorry","disagree")
    exit_commands = ("quit","pause","stop","goodbye","later","bye")
    random_questions = ("why are you here?","are there any humans like you?\n"
                        "What do you consume for living?\n",
                        "Is there any other intelligent life on planet Earth?\n",
                        "Does Earth have a leader","What planets have you visited?\n",
                        "What technology do you have on this planet?\n")
    

    def __intit__(self):
        self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
                             'answer_why_intent': r'why\sare.*',
                             'about_intellipat': r'.*\s*intellipaat'}
        

    def greet(self):
        self.name = input("What is you name?\n")
        will_help = input(
            f"Hi {self.name}, I am a Rule-Bot. Will you help me learn about your planet?\n")
        if will_help in self.negative_responses:
            print("Okay!, fine then, go and have a great day! lol!\n")
            return 
        self.chat()

    def make_exit(self,reply):
        for command in self.exit_commands:
            if reply == command:
                print("Okay, have a nice day on your planet!")
                return True
            
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self,reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == "describe_planet_intent":
                return self.describe_planet_intent()
            elif found_match and intent == "answer_why_intent" : 
                return self.answer_why_intent()
            elif found_match and intent == 'about_intellipat' : 
                return self.about_intellipat()
            
        if not found_match : 
            return self.no_match_intent()
        
    def describe_planet_intent(self):
        responses = ("My planet is where we live and your planet is where you live. We do all those things that you do on your planet. Our technology, however is far more better than yours..lol!\n","i mean, why should i tell you?\n","I aksed you the question first?\n")
        return random.choice(responses)
    
    def answer_why_intent(self):
        responses = ("You see, obviously resources in my planet got dried up. So I came here.\n",
                     "But we come inpeace though, we want to make a deal, we will give you some of our technology and you will give me some of your resources.\n",
                     "This technology, though far more advanced than yours, when time comes, you an use it explore the galaxy for resources youself!\n")
        return random.choice(responses)
    
    def about_intellipat(self):
        responses = ("Intellipat is world's largest professional educational company.\n","I am obviously an alien, what else do you think i am?\n")
        return random.choice(responses)
    
    
    def no_match_intent(self):
        responses = ("Please tell me more\n","Tell me more!\n","I see. Can you elaborate?\n","Oh! Is that what you think?\n","Wow, I love to know more about it!\n")
        return random.choice(responses)
    
Alienbot = RuleBot()
Alienbot.greet()