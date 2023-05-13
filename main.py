import checkCSV
import mongoOperations
from flask import Flask,request
from flask_cors import CORS , cross_origin
app = Flask(__name__)
CORS(app , resources={r"/":{"origins":"*"}})

@app.route("/")
def main():
    return "hello world"

@app.route("/getAnswer", methods=["GET"])
@cross_origin()
def getAnswer():
    question = request.args.get('question')
    return checkCSV.get_answer_by_model(text=question)

@app.route("/loginAdmin" , methods = ["POST"])
@cross_origin()
def loginAdmin():
    try:
        if request.data:
            return mongoOperations.login_admin(id=request.json['id'], password=request.json['password'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }

@app.route("/getQuestions", methods=["GET"])
@cross_origin()
def getAnsweringQuestions():
    return mongoOperations.get_answering_questions()


@app.route("/addAnswer" , methods = ["POST"])
@cross_origin()
def addAnswer():
    try:
        if request.data:
            return mongoOperations.add_answer(qid=request.json['qid'], answer=request.json['answer'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=5000)