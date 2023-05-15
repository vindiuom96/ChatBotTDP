
import CheckMatching
import format_csv
import getAnswer
from mongoOperations import insert_question

df1 = format_csv.format_csv()

def check_answers(text):
    max_matching = 0
    context = ""
    max_context = ""
    matching_count = 0
    for index, row in df1.iterrows():
        text_matching = CheckMatching.check_matching_value(text ,row['/name'])
        if max_matching<=text_matching:
            max_matching = text_matching
            if text_matching>= 0.7:
                max_context = row['/acceptedAnswer/text']
                context+= row['/acceptedAnswer/text']
                matching_count+=1
    if max_matching>=1:
        response = {
            "state" : True,
            "type":1,
            "question": text,
            "max_matching":max_matching,
            "max_context":max_context
        }
    elif max_matching>=0.7 and matching_count>1:
        response = {
            "state": True,
            "type": 2,
            "question": text,
            "context": context,
            "max_matching": max_matching,
        }
    elif max_matching>=0.7:
        response = {
            "state": True,
            "type": 3,
            "question": text,
            "max_matching": max_matching,
            "max_context": max_context
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
        if response['type'] == 2:
            answer = getAnswer.getAnswer(question=response['question'] ,context=response['context'])
            res = {
                "state": True,
                "answer": answer['answer'],
                "score" : answer['score'],
                "max_matching": response['max_matching']

            }
        else:
            res = {
                "state": True,
                "answer": response['max_context'],
                "max_matching": response['max_matching']

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



