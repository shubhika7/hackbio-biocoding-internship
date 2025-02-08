# Hackbio Biocoding Internship - Stage 0 Task
# GitHub Repository: https://github.com/shubhika7/hackbio-biocoding-internship

'''
[1] Hey! I am Shubhika Kumar 
[2] The codon assigned to me was UCU (Serine)
[3] This is my Stage-0 Task
[4] I have used nested dictionaries as a data structure to solve this task
[5] Team Member 1, Uwidia Osalodion Emmanuel is our Team Leader
'''

'''
[1] Hey! I am Shubhika Kumar 
[2] The codon assigned to me was UCU (Serine)
[3] This is my Stage-0 Task
[4] I have used nested dictionaries as a data structure to solve this task.
[5] Team Member 1, Uwidia Osalodion Emmanuel is our Team Leader
'''

serine02_members = {
    "Member 1": {
        "name": "Uwidia Osalodion Emmanuel",
        "slack username": "uwidia",
        "email": "uwidiaosalodion@gmail.com",
        "hobby": "Reading and taking walks",
        "country": "Nigeria",
        "discipline": "Medical Biochemistry",
        "preferred programming language": "Python"
    },
    "Member 2": {
        "name": "Shubhika Kumar",
        "slack username": "shubhika",
        "email": "shubhikakumar09@gmail.com",
        "hobby": "Exploring, Upskilling, Watching crime documentaries",
        "country": "India",
        "discipline": "Biological Sciences and Engineering",
        "preferred programming language": "Python"
    },
    "Member 3": {
        "name": "Saurabh Mazumdar",
        "slack username": "Saurabh",
        "email": "saurabhmazumdar7@gmail.com",
        "hobby": "Coding, exploring new things, listening to songs, and watching movies",
        "country": "India",
        "discipline": "Bioinformatics and Computational Biology",
        "preferred programming language": "Python"
    },
    "Member 4": {
        "name": "Sochima",
        "slack username": "Sochi",
        "email": "sochima.m@gmail.com",
        "hobby": "Exploring",
        "country": "Nigeria",
        "discipline": "Pharmacy",
        "preferred programming language": "Python"
    }
}

# Printing each member's details (NO LOOPS)
print(f"""
Hi! My name is {serine02_members["Member 1"]["name"]}!
Here are my details:
Email: {serine02_members["Member 1"]["email"]}
Slack Username: {serine02_members["Member 1"]["slack username"]}
Hobbies: {serine02_members["Member 1"]["hobby"]}
Country: {serine02_members["Member 1"]["country"]}
Discipline: {serine02_members["Member 1"]["discipline"]}
My preferred programming language: {serine02_members["Member 1"]["preferred programming language"]}
{"-"*75}

Hi! My name is {serine02_members["Member 2"]["name"]}!
Here are my details:
Email: {serine02_members["Member 2"]["email"]}
Slack Username: {serine02_members["Member 2"]["slack username"]}
Hobbies: {serine02_members["Member 2"]["hobby"]}
Country: {serine02_members["Member 2"]["country"]}
Discipline: {serine02_members["Member 2"]["discipline"]}
My preferred programming language: {serine02_members["Member 2"]["preferred programming language"]}
{"-"*75}

Hi! My name is {serine02_members["Member 3"]["name"]}!
Here are my details:
Email: {serine02_members["Member 3"]["email"]}
Slack Username: {serine02_members["Member 3"]["slack username"]}
Hobbies: {serine02_members["Member 3"]["hobby"]}
Country: {serine02_members["Member 3"]["country"]}
Discipline: {serine02_members["Member 3"]["discipline"]}
My preferred programming language: {serine02_members["Member 3"]["preferred programming language"]}
{"-"*75}

Hi! My name is {serine02_members["Member 4"]["name"]}!
Here are my details:
Email: {serine02_members["Member 4"]["email"]}
Slack Username: {serine02_members["Member 4"]["slack username"]}
Hobbies: {serine02_members["Member 4"]["hobby"]}
Country: {serine02_members["Member 4"]["country"]}
Discipline: {serine02_members["Member 4"]["discipline"]}
My preferred programming language: {serine02_members["Member 4"]["preferred programming language"]}
{"-"*75}
""")
