import csv

def add_new_question(question , answer):
    with open("CSV/entities_exported.csv", "a") as file:
        feildNames = ["/@type","/acceptedAnswer/@type","/name", "/acceptedAnswer/text"]
        writter = csv.DictWriter(file, fieldnames=feildNames)
        writter.writerow({"/@type":"Question","/acceptedAnswer/@type":"Answer","/name": question, "/acceptedAnswer/text": answer})
    return


