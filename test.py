# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json
import openai
import os
pdf_latex =r"""\documentclass[10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage[version=4]{mhchem}
\usepackage{stmaryrd}
\usepackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=blue, filecolor=magenta, urlcolor=cyan,}
\urlstyle{same}

\begin{document}
Your PRINTED name is:

1.

Your recitation number or instructor is 2.

\begin{enumerate}
  \setcounter{enumi}{2}
  \item 
  \item 
  \item Forward elimination changes $A \mathbf{x}=\mathbf{b}$ to a row reduced $R \mathbf{x}=\mathbf{d}$ : the complete solution is

\end{enumerate}

$$
\mathbf{x}=\left[\begin{array}{l}
4 \\
0 \\
0
\end{array}\right]+\mathbf{c}_{1}\left[\begin{array}{l}
2 \\
1 \\
0
\end{array}\right]+\mathbf{c}_{2}\left[\begin{array}{l}
5 \\
0 \\
1
\end{array}\right]
$$

(a) (14 points) What is the 3 by 3 reduced row echelon matrix $R$ and what is $\mathbf{d}$ ?

(b) (10 points) If the process of elimination subtracted 3 times row 1 from row 2 and then 5 times row 1 from row 3 , what matrix connects $R$ and $\mathbf{d}$ to the original $A$ and $\mathbf{b}$ ? Use this matrix to find $A$ and $\mathbf{b}$. 2. Suppose $A$ is the matrix

$$
A=\left[\begin{array}{llll}
0 & 1 & 2 & 2 \\
0 & 3 & 8 & 7 \\
0 & 0 & 4 & 2
\end{array}\right]
$$


\end{document}"""
def req_from_chat(question):
    # openai.api_key = os.getenv("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")
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question
             }
        ]
    )
    return completion.choices[0].message

# def req_from_mathpix(pdf):
#     # openai.api_key = os.getenv("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")
#
#     # !/usr/bin/env python
#     import requests
#     import json
#
#     r = requests.post("https://api.mathpix.com/v3/text",
#                       json={
#                           "src": pdf,
#                           "conversion_formats": {
#             "docx": true,
#             "tex.zip": true
#         }
#                       headers={
#                           "app_id": "APP_ID",
#                           "app_key": "APP_KEY",
#                           "Content-type": "application/json"
#                       }
#                       )
#     print(json.dumps(r.json(), indent=4, sort_keys=True))

# openai.api_key = os.getenv("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")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(req_from_chat("can you make a new test at the same level as this one :"+pdf_latex).content)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
