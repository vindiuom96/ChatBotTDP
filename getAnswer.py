from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
model_name = "deepset/tinyroberta-squad2"
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def getAnswer(question , context):
    QA_input ={
        'question': question,
        'context': context
    }

    response  = nlp(QA_input)
    return {
        "score" : response['score'],
        "answer" : response['answer']
    }