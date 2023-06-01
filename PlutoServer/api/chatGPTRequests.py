import json
import requests



url = "https://api.openai.com/v1/chat/completions"
api_key = "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"
pdf_latex = "hello there"
pdf_latex2 =r"""\documentclass[10pt]{article}
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

(a) (16 points) Find all special solutions to $A x=0$ and describe in words the whole nullspace of $A$.

(b) (10 points) Describe the column space of this particular matrix A. "All combinations of the four columns" is not a sufficient answer.

(c) (10 points) What is the reduced row echelon form $R^{*}=\operatorname{rref}(B)$ when $B$ is the 6 by 8 block matrix

$$
B=\left[\begin{array}{cc}
A & A \\
A & A
\end{array}\right] \text { using the same } A ?
$$

\begin{enumerate}
  \setcounter{enumi}{2}
  \item (16 points) Circle the words that correctly complete the following sentence:
\end{enumerate}

(a) Suppose a 3 by 5 matrix $A$ has rank $r=3$. Then the equation $A x=b$ ( always / sometimes but not always )

has ( a unique solution / many solutions / no solution ).

(b) What is the column space of $A$ ? Describe the nullspace of $A$. 4. Suppose that $A$ is the matrix

$$
A=\left[\begin{array}{ll}
2 & 1 \\
6 & 5 \\
2 & 4
\end{array}\right]
$$

(a) (10 points) Explain in words how knowing all solutions to $A \mathbf{x}=\mathbf{b}$ decides if a given vector $\mathbf{b}$ is in the column space of $A$.

(b) (14 points) Is the vector $\mathbf{b}=\left[\begin{array}{c}8 \\ 28 \\ 14\end{array}\right]$ in the column space of $A$ ? MIT OpenCourseWare

\href{http://ocw.mit.edu}{http://ocw.mit.edu}

\subsection{Linear Algebra}
Spring 2010

For information about citing these materials or our Terms of Use, visit: \href{http://ocw.mit.edu/terms}{http://ocw.mit.edu/terms}.


\end{document}"""
pdf_latex_short = r"""\documentclass[10pt]{article}
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


\begin{enumerate}
  \setcounter{enumi}{0}
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

(b) (10 points) If the process of elimination subtracted 3 times row 1 from row 2 and then 5 times row 1 from row 3 , what matrix connects $R$ and $\mathbf{d}$ to the original $A$ and $\mathbf{b}$ ? Use this matrix to find $A$ and $\mathbf{b}$. 

\end{document}
"""

def get_genreated_easy_test(test_to_send):
    payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "messages": [
        {
        "role": "user",
        "content": "can you make a new test at an easier level than this one in latex:" + test_to_send
        }
    ],
    "temperature": 1,
    "top_p": 1,
    "n": 1,
    "stream": False,
    #   "max_tokens": 250,
    "presence_penalty": 0,
    "frequency_penalty": 0
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    "Authorization": "Bearer " + api_key
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.content)['choices'][0]['message']['content']

def get_genreated_medium_test(test_to_send):
    payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "messages": [
        {
        "role": "user",
        "content": "can you make a new test at the same level as this one in latex:" + test_to_send
        }
    ],
    "temperature": 1,
    "top_p": 1,
    "n": 1,
    "stream": False,
    #   "max_tokens": 250,
    "presence_penalty": 0,
    "frequency_penalty": 0
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    "Authorization": "Bearer " + api_key
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.content)['choices'][0]['message']['content']

def get_genreated_hard_test(test_to_send):
    payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "messages": [
        {
        "role": "user",
        "content": "can you make a new test that is harder than this one in latex:" + test_to_send
        }
    ],
    "temperature": 1,
    "top_p": 1,
    "n": 1,
    "stream": False,
    #   "max_tokens": 250,
    "presence_penalty": 0,
    "frequency_penalty": 0
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    "Authorization": "Bearer " + api_key
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.content)['choices'][0]['message']['content']