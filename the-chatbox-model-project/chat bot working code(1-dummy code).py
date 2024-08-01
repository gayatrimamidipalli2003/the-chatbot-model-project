import random

# Define a list of possible bot responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thanks for asking!", "I'm fine, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "who are You":[" iam a chat bot from thub to make clear your doughts more faster and easier"],
    "what is thub": ["The demand-supply gap scenario, exponential opportunities and dynamic challenges in the 21st century call for a change in our thinking on engineering practice and education. A transformation on the current engineering education is the need of the hour Growth of new knowledge together with rapidly evolving technological skills, the skill to communicate across disciplines, the ability to lead team-centered projects, contextualized problem formulation and hands-on experience are the present demands of the global industry. On contrary to the present demands, students churned out from engineering colleges are not equipped to meet the current industry needs due to the growing gap between engineering practice, education and research which requires a lot of concern. As a timely response, it is this concern for the student that has led Aditya to initiate Technical Hub a perfect launch pad to the job world. Technical Hub trains students in various disciplines beyond technological labels besides equipping them with skills and creativity required for advancement in their careers. Through its various programs Technical Hub provides adequate opportunities for an unmatched knowledge base by imparting all necessary skills to students and make them job ready"],
    "who is the founder of thub": ["MR.BABJI NEELAM"],
    "what are the activities in thub": ["1)t-connect  2)code(heat)   3)project-space   4)IN-Campus Intership 5)T-Shaped engineer 6)t-target 7)makers-squares  8)skill-up  9)hackathon"],
    "21mh1a05a9": ["name:gayatri mamidipalli" "s/o :srinu mamidipalli" "contact no:7997470919" "collage:ACOE" "Branch:CSE"  "section:cse-b"],
    "who is the trainer for tse java 2025":["mr.srinu sir"],
    "who is the trainer for redhat":["mr.veerababu sir"],
    "who is the trainer for softskills":["mr.kiran sir"],
    "who is the trainer for compitative codeing":["mr.Ashok sir"],
    "who is the best c-programming trainer":["mr.pavan sir"],
    "who is the best python trainer in thub":["mr .Rajesh sir"], 
    "who is the best designer of thub" :["mr. kiran immandi"],
    "21mh1a0593":["harshitha grandhe   s/0 hema sundaram   contact no:7893381519  collage :acoe   branch :cse    section:cse-b"],
    "default": ["I'm sorry, I don't understand. Can you please rephrase?", "I'm not sure what you mean. Can you please clarify?"],
    "thank you":["with pleasure!", "your most welcome!"], 
}

# Define a function to handle user input
def handle_input(user_input):
    user_input = user_input.lower()
    
    for key in responses.keys():
        if user_input == key:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

while True:
    user_input = input("YOU: ")
    
    bot_response = handle_input(user_input)
        
    print("Thub:", bot_response)
    
    if user_input.lower() == "bye":
        break

