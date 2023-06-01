
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json
import openai
import os
import time
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
tex_with_gar = r"""\documentclass[10pt]{article}
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
  \item Forward elimination changes \(A \mathbf{x}=\mathbf{b}\) to a row reduced \(R \mathbf{x}=\mathbf{d}\) : the complete solution is

\end{enumerate}

\[
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
\]

(a) (14 points) What is the 3 by 3 reduced row echelon matrix \(R\) and what is \(\mathbf{d}\) ?

(b) (10 points) If the process of elimination subtracted 3 times row 1 from row 2 and then 5 times row 1 from row 3 , what matrix connects \(R\) and \(\mathbf{d}\) to the original \(A\) and \(\mathbf{b}\) ? Use this matrix to find \(A\) and \(\mathbf{b}\). 2. Suppose \(A\) is the matrix

\[
A=\left[\begin{array}{llll}
0 & 1 & 2 & 2 \\
0 & 3 & 8 & 7 \\
0 & 0 & 4 & 2
\end{array}\right]
\]

(a) (16 points) Find all special solutions to \(A x=0\) and describe in words the whole nullspace of \(A\).

(b) (10 points) Describe the column space of this particular matrix A. "All combinations of the four columns" is not a sufficient answer.

(c) (10 points) What is the reduced row echelon form \(R^{*}=\operatorname{rref}(B)\) when \(B\) is the 6 by 8 block matrix

\[
B=\left[\begin{array}{cc}
A & A \\
A & A
\end{array}\right] \text { using the same } A ?
\]

\begin{enumerate}
  \setcounter{enumi}{2}
  \item (16 points) Circle the words that correctly complete the following sentence:
\end{enumerate}

(a) Suppose a 3 by 5 matrix \(A\) has rank \(r=3\). Then the equation \(A x=b\) ( always / sometimes but not always )

has ( a unique solution / many solutions / no solution ).

(b) What is the column space of \(A\) ? Describe the nullspace of \(A\). 4. Suppose that \(A\) is the matrix

\[
A=\left[\begin{array}{ll}
2 & 1 \\
6 & 5 \\
2 & 4
\end{array}\right]
\]

(a) (10 points) Explain in words how knowing all solutions to \(A \mathbf{x}=\mathbf{b}\) decides if a given vector \(\mathbf{b}\) is in the column space of \(A\).

(b) (14 points) Is the vector \(\mathbf{b}=\left[\begin{array}{c}8 \\ 28 \\ 14\end{array}\right]\) in the column space of \(A\) ? MIT OpenCourseWare

\href{http://ocw.mit.edu}{http://ocw.mit.edu}

\subsection{Linear Algebra}
Spring 2010

For information about citing these materials or our Terms of Use, visit: \href{http://ocw.mit.edu/terms}{http://ocw.mit.edu/terms}.


\end{document}k;ldsak;ldska;lfjd;ajk;sa"""

pdf_url_global = "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/e9bbec7a9a25a87715e8edd75e21d7b9_MIT18_06S10_exam1_s10.pdf"
app_id = "sahar_aharon_mail_huji_ac_il_3c7cbb_0e2a12"
app_key = "4f4bc73d80dd02413096cb9d6bc8ea8e9c17936956fda1e669f944e484f17b99"
def save_as_tex_file(tex_string):

    # Specify the file path and name
    file_path = "new_file.tex"

    # Write the .tex content to a file
    with open(file_path, "w") as f:
        f.write(tex_string)

    print("TeX file generated successfully.")

def clean_txt(text):
    index = text.find("\\documentclass")
    if index != -1:
        cleaned_text = text[index:]
    else:
        cleaned_text = text

    cleaned_text_index = text.find("end{document}")
    if index != -1:
        cleaned_text_end = cleaned_text[:cleaned_text_index + len("end{document}") ]
    else:
        cleaned_text_end = cleaned_text
    return cleaned_text_end

def check_answer(q_url , a_url):
    q_tex = req_from_mathpix(q_url)
    a_tex = req_from_mathpix_img(a_url)
    return "is my answer correct?" + q_tex +a_tex


def req_from_mathpix_img(img_url):
    app_id = "sahar_aharon_mail_huji_ac_il_3c7cbb_0e2a12"
    app_key = "4f4bc73d80dd02413096cb9d6bc8ea8e9c17936956fda1e669f944e484f17b99"
    url = "https://api.mathpix.com/v3/text"

    r = requests.post("https://api.mathpix.com/v3/text",
                      json={
                          "src": img_url,
                          "math_inline_delimiters": ["$", "$"],
                          "rm_spaces": True
                      },
                      headers={
                          "app_id": app_id,
                          "app_key": app_key,
                          "Content-type": "application/json"
                      }
                      )
    return r.json()['text']

    # response = requests.get(url + "/" + pdf_id , headers = headers)
    # while(response.json()["status"] != "completed") :
    #     time.sleep(1)
    #     response = requests.get(url + "/" + pdf_id , headers = headers)
    # # print("Processing done!")
    #
    #
    # response = requests.get( "https://api.mathpix.com/v3/converter/" + pdf_id , headers= headers)
    # while(response.json()["conversion_status"]["tex.zip"]["status"] != "completed") :
    #     time.sleep(1)
    #     response = requests.get("https://api.mathpix.com/v3/converter/" + pdf_id, headers=headers)
    # # print("Processing latex done!")
    #
    #
    # headers = {
    #     "app_key": app_key,
    #     "app_id": app_id
    # }
    # url = f"https://api.mathpix.com/v3/pdf/{pdf_id}.tex"
    # response = requests.get(url, headers=headers)
    # # print("all done!")
    # text = response.text
    #
    # index = text.find("\\documentclass")
    # if index != -1:
    #     cleaned_text = text[index:]
    # else:
    #     cleaned_text = text
    #
    # cleaned_text_index = text.find("end{document}")
    # if index != -1:
    #     cleaned_text_end = cleaned_text[:cleaned_text_index + len("end{document}") ]
    # else:
    #     cleaned_text_end = cleaned_text
    # return cleaned_text_end
def req_from_mathpix(pdf_url):
    app_id = "sahar_aharon_mail_huji_ac_il_3c7cbb_0e2a12"
    app_key = "4f4bc73d80dd02413096cb9d6bc8ea8e9c17936956fda1e669f944e484f17b99"
    url = "https://api.mathpix.com/v3/pdf"
    payload = {
        "url": pdf_url,
        "conversion_formats": {
            "docx": True,
            "tex.zip": True
        }
    }
    headers = {
        "app_id": app_id,
        "app_key": app_key,
        "Content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    pdf_id = response.json()["pdf_id"]

    response = requests.get(url + "/" + pdf_id , headers = headers)
    while(response.json()["status"] != "completed") :
        time.sleep(1)
        response = requests.get(url + "/" + pdf_id , headers = headers)
    # print("Processing done!")


    response = requests.get( "https://api.mathpix.com/v3/converter/" + pdf_id , headers= headers)
    while(response.json()["conversion_status"]["tex.zip"]["status"] != "completed") :
        time.sleep(1)
        response = requests.get("https://api.mathpix.com/v3/converter/" + pdf_id, headers=headers)
    # print("Processing latex done!")


    headers = {
        "app_key": app_key,
        "app_id": app_id
    }
    url = f"https://api.mathpix.com/v3/pdf/{pdf_id}.tex"
    response = requests.get(url, headers=headers)
    # print("all done!")
    text = response.text

    index = text.find("\\documentclass")
    if index != -1:
        cleaned_text = text[index:]
    else:
        cleaned_text = text

    cleaned_text_index = text.find("end{document}")
    if index != -1:
        cleaned_text_end = cleaned_text[:cleaned_text_index + len("end{document}") ]
    else:
        cleaned_text_end = cleaned_text
    return cleaned_text_end

    # openai.api_key = "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"
    # completion = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "user", "content": question
    #          }
    #     ]
    # )
    # return completion.choices[0].message

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
    # pdf_url_global = "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/e9bbec7a9a25a87715e8edd75e21d7b9_MIT18_06S10_exam1_s10.pdf"
    # print(req_from_mathpix(pdf_url_global))
    # save_as_tex_file(pdf_latex)
    # print(clean_txt(tex_with_gar))
    # print(tex_with_gar)
    req_from_mathpix_img("https://i.ibb.co/30Pc9bc/Whats-App-Image-2023-06-01-at-23-03-22.jpg")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
