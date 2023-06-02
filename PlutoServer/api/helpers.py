import subprocess
import os

def clean_text_for_latex(text):
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

def save_to_pdf(input_string, output_file_name):
    # Specify the file path and name
    file_path = output_file_name + ".tex"

    # Write the .tex content to a file
    with open(file_path, "w") as f:
        f.write(input_string)

    subprocess.run(["pdflatex", "-interaction=nonstopmode", file_path])
    
    os.remove(output_file_name + ".aux")
    os.remove(output_file_name + ".log")
    os.remove(output_file_name + ".out")
    os.remove(output_file_name + ".tex")

pdf_begin  = r"""\documentclass[10pt]{article}
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

"""

pdf_end = r"""
\end{document}"""