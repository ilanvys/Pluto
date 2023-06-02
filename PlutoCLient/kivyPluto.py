import requests
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest
import json
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton



class MainWindow(Screen):
    pass

class TestWindow(Screen):
    pass

class QuestionWindow(Screen):
    pass

class FeedbackWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class MyApp(App):
    def on_request_success(self, req, result):
        # response_data = result  # Assuming the response is in JSON format
        # response_text = json.dumps(response_data)  # Convert the response data to a string
        # self.response_label.text = response_text
        # Present only msg from the dict
        msg_value = result.get("msg", "")  # Extract the value of the "msg" key
        self.response_label.text = msg_value

    def on_request_failure(self, req, result):
        self.response_label.text = "Request failed"  # Display an error message

    def make_request(self, instance):
        # Make a request to the server
        url = "http://132.64.33.111:5000/chat"  # Replace with your server's endpoint
        headers = {'Content-Type': 'application/json'}  # Replace with appropriate headers
        body = '{"data": "value"}'  # Replace with the request body, if needed

        request = UrlRequest(url, method='POST', req_headers=headers, req_body=body,
                             on_success=self.on_request_success,
                             on_failure=self.on_request_failure)
        # You can pass additional parameters to the request if required

    def make_get_request(self, instance):
        # Make a GET request to the server
        url = "http://132.64.33.111:5000/chat"  # Replace with your server's GET endpoint
        headers = {'Content-Type': 'application/json'}  # Replace with appropriate headers

        request = UrlRequest(url, req_headers=headers,
                             on_success=self.on_request_success,
                             on_failure=self.on_request_failure)
        # You can pass additional parameters to the request if required

    def build(self):
        # Create the screen manager
        sm = WindowManager()

        # Create the main window screen
        main_window = MainWindow(name='main')
        main_layout = FloatLayout(size=(1000, 1000))
        Window.clearcolor = (1, 1, 1, 1)

        # Create an Image widget
        title_image = Image(source='mail.jpeg',
                            size_hint=(.5, .3), pos=(400, 800))
        title_image.background_color = (0, 0, 0, 0)
        # # Add the Image widget to the layout
        main_layout.add_widget(title_image)

        response_label = Label(text="[b]Woof Woof my best friend!\n        How can I help you?[/b]", markup = True,
                                    size_hint=(.1, .1), pos=(700,650), font_size=80, color=(0, 0, 0, 1))
        main_layout.add_widget(response_label)

        image_button_1 = Button(background_normal='eceee516-8078-4d8a-bf55-7fe8d70c78b6.JPG',
                                background_down='eceee516-8078-4d8a-bf55-7fe8d70c78b6.JPG'
                              ,size_hint=(.3, .15), pos=(100,200))
        image_button_1.bind(on_press=self.switch_generate_test_window)
        main_layout.add_widget(image_button_1)

        image_button_2 = Button(background_normal='PHOTO-2023-06-02-02-01-34.jpg',
                                background_down='PHOTO-2023-06-02-02-01-34.jpg'
                              ,size_hint=(.3, .15), pos=(1100, 200))
        image_button_2.bind(on_press=self.switch_single_question_window)
        main_layout.add_widget(image_button_2)

        image_button_3 = Button(background_normal='feedback.png',
                                background_down='feedback.png'
                                , size_hint=(.3, .15), pos=(600, 200))
        image_button_3.bind(on_press=self.switch_feedback_window)
        main_layout.add_widget(image_button_3)




        main_window.add_widget(main_layout)

        # create new window
        test_window = TestWindow(name='test_window')
        test_layout = FloatLayout()

        text_input = TextInput(hint_text='Enter PDF url', multiline=False, size_hint=(.4, .1), pos=(500,600))

        label = Label(text='Select a difficulty:', size_hint=(.2, .1), pos=(400,550))
        slider = Slider(min=1, max=3, )

        self.slider_value = 0  # Variable to store the slider value

        slider = Slider(min=1, max=3, value=self.slider_value, step=1, size_hint=(.2, .1), pos=(800, 150))
        slider.bind(on_touch_move=self.on_slider_value_change)





        test_layout.add_widget(label)
        test_layout.add_widget(slider)

        send_pdf_url = Button(text='Send', on_release=lambda instance: self.send_test_url(text_input.text,slider),
                              size_hint=(.1, .1), pos=(400,600))
        test_layout.add_widget(text_input)
        test_layout.add_widget(send_pdf_url)
        test_window.add_widget(test_layout)






        question_window = QuestionWindow(name='question_window')
        question_layout = FloatLayout()

        hint_button = ToggleButton(text='Get Hint', group='options', size_hint=(.2, .05), pos=(450,250))
        hint_button.bind(on_press=lambda instance: self.option_pressed(instance, 'hint'))

        solution_button = ToggleButton(text='Get Solution', group='options', size_hint=(.2, .05), pos=(450,200))
        solution_button.bind(on_press=lambda instance: self.option_pressed(instance, 'solution'))

        generate_button = ToggleButton(text='Generate question', group='options', size_hint=(.2, .05), pos=(450,150))
        generate_button.bind(on_press=lambda instance: self.option_pressed(instance, 'generate'))

        self.option1_pressed = False
        self.option2_pressed = False
        self.option3_pressed = False

        question_layout.add_widget(hint_button)
        question_layout.add_widget(solution_button)
        question_layout.add_widget(generate_button)

        text_input = TextInput(hint_text='Enter PDF url', multiline=False, size_hint=(.4, .1), pos=(500,600))

        difficulty_label = Label(text='Select a difficulty:', size_hint=(.2, .1), pos=(400, 550))

        slider = Slider(min=1, max=3, value=self.slider_value, step=1, size_hint=(.2, .1), pos=(800, 150))
        slider.bind(on_touch_move=self.on_slider_value_change)


        question_layout.add_widget(difficulty_label)
        question_layout.add_widget(slider)

        send_pdf_url = Button(text='Send', on_release=lambda instance: self.send_question_url
        (text_input.text, slider, self.option1_pressed, self.option2_pressed, self.option3_pressed),
                              size_hint=(.1, .1), pos=(400, 600))
        question_layout.add_widget(text_input)
        question_layout.add_widget(send_pdf_url)
        question_window.add_widget(question_layout)

        feedback_window = FeedbackWindow(name='feedback_window')
        feedback_layout = FloatLayout()

        text_input = TextInput(hint_text='Enter JPEG url', multiline=False, size_hint=(.4, .1), pos=(500, 600)
                               ,font_size=60)

        send_jpeg_url = Button(text='Send', on_release=lambda instance: self.send_feedback_url(text_input.text),
                              size_hint=(.1, .1), pos=(300, 600), font_size=40)
        feedback_layout.add_widget(text_input)
        feedback_layout.add_widget(send_jpeg_url)
        feedback_window.add_widget(feedback_layout)

        # Add the screens to the screen manager
        sm.add_widget(main_window)
        sm.add_widget(test_window)
        sm.add_widget(question_window)
        sm.add_widget(feedback_window)


        return sm


    def on_button_press(self, instance):
                print("Image button pressed")

    def switch_generate_test_window(self, instance):
        self.root.current = 'test_window'  # Switch to the 'new' screen

    def switch_single_question_window(self, instance):
        self.root.current = 'question_window'  # Switch to the 'new' screen

    def switch_feedback_window(self, instance):
        self.root.current = 'feedback_window'

    def on_slider_value_change(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.slider_value = instance.value
            label = instance.parent.children[1]
            label.text = str(self.slider_value)

    def send_test_url(self, text, difficulty):

        # Perform the HTTP POST request
        url = "http://132.64.33.111:5000/test"

        payload = json.dumps({
            "data": text
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            print('Request sent successfully')
        else:
            print('Failed to send request')

        if difficulty == 1:
            url = 'http://132.64.33.111:5000/test/easy_test/1'
        elif difficulty == 2:
            url = 'http://132.64.33.111:5000/test/medium_test/1'
        else:
            url = 'http://132.64.33.111:5000/test/hard_test/1'

        response = requests.put(url, headers=headers, data=payload)

        if response.status_code == 200:
            print('Request sent successfully')
        else:
            print('Failed to send request')

    def send_question_url(self, text, difficulty, get_hint, get_solution, generate_question):

        url = "http://132.64.33.111:5000/question"

        payload = json.dumps({
            "data": text
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            print('Request sent successfully')
        else:
            print('Failed to send request')

        if generate_question:
            if difficulty == 1:
                url = 'http://132.64.33.111:5000/question/easy_question/1'
            elif difficulty == 2:
                url = 'http://132.64.33.111:5000/question/medium_question/1'
            else:
                url = 'http://132.64.33.111:5000/question/hard_question/1'
        elif get_hint:
            url = 'http://132.64.33.111:5000/question/hint/1'
        else:
            url = 'http://132.64.33.111:5000/question/solution/1'

        # data = {'text': text}
        # response = requests.post(url, json=data)

        response = requests.request("GET", url, headers=headers, data=payload)

        # Process the response if needed
        if response.status_code == 200:
            print('Request sent successfully')
        else:
            print('Failed to send request')

    def send_feedback_url(self, text):
        url = "http://132.64.33.111:5000/question/feedback"

        payload = json.dumps({
            "data": text
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        # Process the response if needed
        if response.status_code == 200:
            print('Request sent successfully')
        else:
            print('Failed to send request')


    def option_pressed(self, instance, option_name):
        if option_name == 'hint':
            self.option1_pressed = True
            self.option2_pressed = False
            self.option3_pressed = False
        elif option_name == 'solution':
            self.option1_pressed = False
            self.option2_pressed = True
            self.option3_pressed = False
        elif option_name == 'generate':
            self.option1_pressed = False
            self.option2_pressed = False
            self.option3_pressed = True






if __name__ == "__main__":
    MyApp().run()
