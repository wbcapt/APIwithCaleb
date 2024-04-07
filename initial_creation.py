import requests
import json

#define a response variable which is returned back from the URL when you query it
response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

print(f'Printing the Response: {response}')
print("Printing the Response in JSON: \n" , response.json(),"\n")
print("Printing the Responsed as a list of items \n" , response.json()['items'], "\n")

#iterate through the JSON response lists and return each question
print("list of questions:\n")
for question in response.json()['items']:
    print(question['title'])
    print(question['link'])

#only return questions with an answer count greater than 0
for question in response.json()['items']:
    if question['answer_count'] == 0:
        print(question['title'])
        print("Answer Count:" , question['answer_count'])
        print(question['link'])