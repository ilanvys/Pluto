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