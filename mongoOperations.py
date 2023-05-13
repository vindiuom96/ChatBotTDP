import time
from bson import ObjectId
import Authentications.generateToken as jwt
import connection_mongo
import updateCSV

db_name = connection_mongo.connect_mongo_db()
collection_queston = db_name['question']
collection_admin = db_name['admin']

def get_object(obj):
    try:
        if '_id' in obj:
            obj['id'] = str(obj['_id'])
            del obj['_id']
        return obj
    except:
        return {
            "state": False,
            "message": "error"
        }

def get_objects(objs):
    return list(map(lambda obj: get_object(obj), objs))

def login_admin(id , password):
    try:
        result = collection_admin.find_one({'_id': ObjectId(id)})
        if result['password'] == password:
            token = jwt.generate_token_super(password=password , id=id)
            return {
                "state": True,
                "message": "success",
                "token": token,
            }
        else:
            return {
                "state": False,
                "message": "error password"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }


def insert_question(question):
    try:
        result = collection_queston.find({'question': question})
        result_list = list(result)
        print(len(result_list))
        if len(result_list)>0:
            return {
                "state": True,
                "message": "No matching answer",
                "hint":"already added to db"
            }
        body = {
            "question": question,
            "time": time.time(),
            "answers": [],
            "added_users": [],
            "liked_users": [],
            "state": "answering"
        }
        result = collection_queston.insert_one(body)
        return {
            "state": True,
            "message": "No matching answer"
        }
    except:
        return {
            "state": False,
            "message": "error"
        }


def get_answering_questions():
    try:
        result = collection_queston.find()
        response = []
        for question in result:
            response.append(question)
        return {
            "state": True,
            "message": "success",
            "result": get_objects(response)
        }
    except:
        return {
            "state": False,
            "message": "error"
        }

def add_answer(qid ,answer):
    try:
        question = collection_queston.find_one({'_id': ObjectId(qid)})
        question = question['question']
        print(question)
        updateCSV.add_new_question(question=question, answer=answer)
        collection_queston.delete_one({'_id': ObjectId(qid)})
        return {
            "state": True,
            "message": "success"
        }
    except:
        return {
            "state": False,
            "message": "error"
        }
