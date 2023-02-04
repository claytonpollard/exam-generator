import pandas as pd
import glob
import pathlib
from pathlib import Path

marks = pd.read_excel(r'questions.xlsx')
marksDF = pd.DataFrame(marks)
topicMarks = {}
for index, row in marksDF.iterrows():
    topic = row['Topic']
    marks = row['Marks']
    topicMarks[topic] = marks

topics = marksDF['Topic'].values.tolist()
questionLists = {}
for i in topics:
    questionLists[i] = []
for i in questionLists:
    path = Path('questions') / i
    for filename in glob.glob(str(path/'*.txt')):
        questionLists[i].append(
            open(filename).read().split('***')
        )

questionDFs = {}
for i, j in questionLists.items():
    questionDFs[i] = pd.DataFrame(j, columns=['Marks', 'Difficulty', 'Question'])

for i, j in questionDFs.items():
    questionDFs[i]['Marks'] = questionDFs[i]['Marks'].astype(int)

with open('questions.tex', 'w') as f_out:
    pass

questions = {}

for topic, target_marks in topicMarks.items():
    current_marks = 0
    topicQuestions = []
    while current_marks != target_marks:
        for j in questionDFs[topic].sample(frac=1).iterrows():
            if (current_marks + j[1]['Marks']) <= target_marks:
                current_marks += j[1]['Marks']
                topicQuestions.append(j[1])
            if current_marks == target_marks:
                break
        if current_marks != target_marks:
            current_marks = 0
            topicQuestions = []
        else:
            questions[topic] = topicQuestions


for topic, topic_questions in questions.items():
    sorted_questions = sorted(topic_questions, key=lambda x: x['Difficulty'])
    questions[topic] = sorted_questions

with open('questions.tex', 'a') as f_out:
    for i, j in questions.items():
        f_out.write('% NEW TOPIC: ' + i + '\n')
        for question in j:
            f_out.write('\question[' + str(question.at['Marks']) + '] ' + question.at['Question'] + '\n')
        f_out.write('\n')