
import CheckMatching
import format_csv
import getAnswer
from mongoOperations import insert_question

df1 = format_csv.format_csv()

def check_answers(text):
    max_matching = 0
    context = ""
    for index, row in df1.iterrows():
        print(row)
        text_matching = CheckMatching.check_matching_value(text ,row['/name'])
        if max_matching<=text_matching:
            max_matching = text_matching
            context = row['/acceptedAnswer/text']
    if max_matching>=0.7:
        response = {
            "state" : True,
            "question": text,
            "context":context,
            "max_matching":max_matching
        }
    else:
        response = {
            "state": False,
            "max_matching": max_matching
        }
    return response

def get_answer_by_model(text):
    response = check_answers(text=text)
    if response['state']:
        answer = getAnswer.getAnswer(question=response['question'] ,context=response['context'])
        res = {
            "state":True,
            "answer":answer['answer'],
            "score" : answer['score'],
            "max_matching":response['max_matching']

        }
    else:
        #add to mongoDB
        if response['max_matching']>= 0.5:
            insert_question(text)
        res = {
            "state": False,
            "message":"No Matching",
            "max_matching": response['max_matching']
        }
    return res

def get_dataframe():
    return df1




