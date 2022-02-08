import requests
import json
import pandas as pd

data = pd.read_csv("/home/bavalpreet/citybot/Utah Adult Ed Bot Planning - FAQ Testing (2).csv")
# print(data)
question_list = []
original_answer_list = []
bot_answer_list = []
for index, row in data.iterrows():
    question = row["Question"]
    orig_ans = row["Approved Answer"]

    payload = json.dumps(dict(sender="rasa", message=question))

    # print(payload)
    print(payload)
    r = requests.post( url='http://localhost:5005/webhooks/rest/webhook', data=payload)
    print(r)
    # response = json.loads(r)
    # print(r.text)
    # print(r.json()[0]["text"])
    # print()
    answer = r.json()[0]["text"]
    question_list.append(question)
    original_answer_list.append(orig_ans)
    bot_answer_list.append(answer)
    print(answer)
    print(orig_ans)

df = pd.DataFrame({"quest": question_list, "bot_answer": bot_answer_list, "orginal_answer": original_answer_list })

df.to_csv("test.csv", index=False)