import csv

def add_new_question(question , answer):
    with open("CSV/entities_exported.csv", "a") as file:
        feildNames = ["/@type","/acceptedAnswer/@type","/acceptedAnswer/text","/name"]
        writter = csv.DictWriter(file, fieldnames=feildNames)
        writter.writerow({"/@type":"Question","/acceptedAnswer/@type":"Answer","/acceptedAnswer/text": answer,"/name": question})
    return



