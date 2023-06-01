
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

pdf_url_global = "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/e9bbec7a9a25a87715e8edd75e21d7b9_MIT18_06S10_exam1_s10.pdf"
app_id = "sahar_aharon_mail_huji_ac_il_3c7cbb_0e2a12"
app_key = "4f4bc73d80dd02413096cb9d6bc8ea8e9c17936956fda1e669f944e484f17b99"

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
    pdf_url_global = "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/e9bbec7a9a25a87715e8edd75e21d7b9_MIT18_06S10_exam1_s10.pdf"
    print(req_from_mathpix(pdf_url_global))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
