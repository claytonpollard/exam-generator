import pandas as pd
import glob
import pathlib
from pathlib import Path

marks = pd.read_excel(r'questions.xlsx')
marksDF = pd.DataFrame(marks)
topicMarks = {}
for index, row in marksDF.iterrows():
    topic = row['Topic']
    target_data = {
        'total_marks': row['TotalMarks'],
        'difficulty': {'1': row['EasyMarks'], '2': row['MediumMarks'], '3': row['HardMarks']}
    }
    topicMarks[topic] = target_data

topics = marksDF['Topic'].values.tolist()
questionLists = {}
for i in topics:
    questionLists[i] = []
for i in questionLists:
    path = Path('questions') / i
    for filename in glob.glob(str(path/'*.txt')):
        questionLists[i].append(
            # Remove newline characters
            [s.strip() for s in open(filename).read().split('***')]
        )

questionDFs = {}
for i, j in questionLists.items():
    questionDFs[i] = pd.DataFrame(
        j, columns=['Marks', 'Difficulty', 'Question'])

for i, j in questionDFs.items():
    questionDFs[i]['Marks'] = questionDFs[i]['Marks'].astype(int)

with open('questions.tex', 'w') as f_out:
    pass

questions = {}

max_attempts = 1000  # Set a maximum number of attempts to prevent infinite looping

for topic, target_data in topicMarks.items():
    current_marks = 0
    target_difficulty = target_data['difficulty']
    topicQuestions = []
    attempts = 0
    while current_marks != target_data['total_marks'] and attempts < max_attempts:
        attempts += 1
        topicQuestions = []
        for difficulty in ['1', '2', '3']:
            target_difficulty_marks = target_difficulty[difficulty]
            selected_questions = questionDFs[topic][questionDFs[topic]['Difficulty'] == difficulty].sample(
                frac=1, replace=True)
            difficulty_marks = 0
            for _, question in selected_questions.iterrows():
                if (difficulty_marks + question['Marks']) <= target_difficulty_marks:
                    difficulty_marks += question['Marks']
                    topicQuestions.append(question)
                if difficulty_marks == target_difficulty_marks:
                    break
        current_marks = sum(question['Marks'] for question in topicQuestions)
        if current_marks != target_data['total_marks']:
            current_marks = 0
            topicQuestions = []
        else:
            questions[topic] = topicQuestions

    if attempts == max_attempts:
        # Debug print
        print(
            f"Failed to select questions for topic '{topic}' after {max_attempts} attempts.")

with open('questions.tex', 'a') as f_out:
    for topic, questions_list in questions.items():
        sorted_questions = sorted(
            questions_list, key=lambda x: x['Difficulty'])
        f_out.write('% NEW TOPIC: ' + topic + '\n')
        for question in sorted_questions:
            f_out.write(
                '\question[' + str(question.at['Marks']) + '] ' + question.at['Question'] + '\n')
        f_out.write('\n')
