Here is a script that uses python and LaTeX to generate an exam.

It randomly selects questions adding to the totals provided for each topic in `questions.xlsx`.

You need to add questions to the question bank under `/questions/` sorted by topic. These topics **must** match the the topics in the first column of `questions.xlsx`.

When adding questions the formatting is as follows:

```
# Marks
***
# Difficulty (1-3)
***
Question written in LaTeX.
```

Currently it only sorts questions from easiest (1) to hardest (3), but in future I might add the ability to choose the number of marks for each difficulty.

After running `generate.py` it will create a `questions.tex` file containing all the randomly chosen questions.

Compile `main.tex` to generate your exam.

To change the formatting of the exam, simply edit `main.tex`, `/include/coverpage.tex`/, `/include/style.tex` and `/include/crest.png`.

The provided exam template is from my [SACE mathematics exam template](https://github.com/claytonpollard/latex-templates/tree/master/sace-mathematics-exam)