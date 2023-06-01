
import requests
import time
from api.helpers import clean_text_for_latex

pdf_url_global = "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/e9bbec7a9a25a87715e8edd75e21d7b9_MIT18_06S10_exam1_s10.pdf"
app_id = "sahar_aharon_mail_huji_ac_il_3c7cbb_a77038"
app_key = "464f5b5e141d1f0f05fb35bb152fd1096c21fea56f6a8e79d8d88ee413a04cd6"
def get_latex_from_pdf(pdf_url):
    app_id = "sahar_aharon_mail_huji_ac_il_3c7cbb_a77038"
    app_key = "464f5b5e141d1f0f05fb35bb152fd1096c21fea56f6a8e79d8d88ee413a04cd6"
    url = "https://api.mathpix.com/v3/pdf"
    payload = {
        "url": pdf_url_global,
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
        print(url + "/" + pdf_id)
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

    return clean_text_for_latex(text)
