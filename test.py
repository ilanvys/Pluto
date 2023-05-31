<<<<<<< HEAD
print("Pluto!")
print("shani")
print("secfgfgound try")
=======
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    response = requests.get("https://google.com/")
    print(response)


# openai.api_key = os.getenv("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")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    import openai
    import os

    # openai.api_key = os.getenv("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")
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "can you "
                                        "please solve the following question:"
             }
        ]
    )

    print(completion.choices[0].message)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
>>>>>>> b35e72d8da00d526d1c42ddfba70bce2e0108687
