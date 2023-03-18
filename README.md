Here is a script that uses python and LaTeX to generate an exam.

Now you can choose how many marks for each difficulty in `questions.xlsx` and it will randomly select questions adding to the totals provided for each topic and level of difficulty. After selecting the questions it will also sort from easiest to hardest within each topic.

You need to add questions to the question bank under `/questions/` sorted by topic. These topics **must** match the the topics in the first column of `questions.xlsx`.

When adding questions the formatting is as follows:

```
# Marks
***
# Difficulty (1-3)
***
Question written in LaTeX.
```

After running `generate.py` it will create a `questions.tex` file containing all the randomly chosen questions.

Compile `main.tex` to generate your exam.

To change the formatting of the exam, simply edit `main.tex`, `/include/coverpage.tex`/, `/include/style.tex` and `/include/crest.png`.

The provided exam template is from my [SACE mathematics exam template](https://github.com/claytonpollard/latex-templates/tree/master/sace-mathematics-exam)
