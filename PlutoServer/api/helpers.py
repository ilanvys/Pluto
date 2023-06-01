import subprocess

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
    