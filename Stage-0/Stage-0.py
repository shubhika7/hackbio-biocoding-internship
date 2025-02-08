'''
[1] Hey! I am Shubhika Kumar 
[2] The codon assigned to me was UCU (Serine)
[3] This is my Stage-0 Task
[4] I have used nested dictionaries as a data structure to solve this task
[5] Team Member 1, Uwidia Osalodion Emmanuel is our Team Leader
'''
serine02_members = {
 "Member 1" : {
     "name" : "Uwidia Osalodion Emmanuel",
 "slack username" : "uwidia",
 "email" : "uwidiaosalodion@gmail.com",
 "hobby" : "Reading and taking walks",
 "country" : "Nigeria",
 "discipline" : "Medical Biochemistry",
 "preferred programming language" : "Python"
     
 },
 "Member 2" : {
     "name" : "Shubhika Kumar",
 "slack username" : "shubhika",
 "email" : "shubhikakumar09@gmail.com",
 "hobby" : "Exploring, Upskilling, Watching crime documentaries",
 "country" : "India",
 "discipline" : "Biological Sciences and Engineering",
 "preferred programming language" : "Python"
 },
  "Member 3" : {
    "name" : "Saurabh mazumdar",
 "slack username" : "Saurabh",
 "email" : "saurabhmazumdar7@gmail.com",
 "hobby" : "Coding ,exploring new things, listening songs and watching movies",
 "country" : "India",
 "discipline" : "Bioinformatics and Computational biology",
 "preferred programming language" : "Python"
 },
  "Member 4" : {
     "name" : "Sochima",
 "slack username" : "Sochi",
 "email" : "sochima.m@gmail.com",
 "hobby" : "Exploring",
 "country" : "Nigeria",
 "discipline" : "Pharmacy",
 "preferred programming language" : "Python"
 }
  
}

for i in serine02_members:
    print(f"Hi I am {i}.\nHere are my details-")
    print(f"Name : {serine02_members[i]['name']}")
    print(f"Email : {serine02_members[i]['email']}")
    print(f"Slack Username : {serine02_members[i]['slack username']}")
    print(f"Hobbies : {serine02_members[i]['hobby']}")
    print(f"Country : {serine02_members[i]['country']}")
    print(f"Discipline : {serine02_members[i]['discipline']}")
    print(f"My Preferred programming language : {serine02_members[i]['preferred programming language']}")
    print("-"*75)
