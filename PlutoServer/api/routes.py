# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import request, send_file
from flask_restx import Api, Resource, fields

from api.models import db, Datas
from api.chatGPTRequests import *
from api.mathpixRequests import *
from api.helpers import *

rest_api = Api(version="1.0", title="Datas API")

# Used to validate input data for creation
create_model = rest_api.model('CreateModel', {"data": fields.String(required=True, min_length=1)})

# Used to validate input data for update
update_model = rest_api.model('UpdateModel', {"data": fields.String(required=True, min_length=1)})

"""
    Flask-Restx routes
"""                
###################################################################
####  PlutoServer
###################################################################
@rest_api.route('/test')
class Items(Resource):
    def get(self):
        return {"success" : True,
                "msg"     : "Hello you",
                "datas"   : "Hello you2" }, 200


    @rest_api.expect(create_model, validate=True)
    def post(self):

        # Read ALL input  
        req_data = request.get_json()

        # Get the url    
        original_test_url = req_data.get("data")

        # translate to latex
        latex_translation = get_latex_from_pdf(original_test_url)

        # generate tests
        # genreated_easy_test = clean_text_for_latex(get_genreated_easy_test(latex_translation))
        # genreated_medium_test =  clean_text_for_latex(get_genreated_medium_test(test_data))
        # genreated_hard_test =  clean_text_for_latex(get_genreated_hard_test(test_data))
        genreated_easy_test = None
        genreated_medium_test = None
        genreated_hard_test = None

        # Create new object
        new_item = Datas(original_latex=latex_translation, 
                         type="test",
                         generated_test_latex_easy=genreated_easy_test, 
                         generated_test_latex_medium=genreated_medium_test, 
                         generated_test_latex_hard=genreated_hard_test) 

        # Save the data
        new_item.save()
        
        return {"success": True,
                "msg"    : "Item successfully created",
                "data": new_item.id }, 200

# Return all data of a test by id
@rest_api.route('/test/<int:id>')
class ItemManager(Resource):
    """
       Return all data by id
    """
    def get(self, id):

        item = Datas.get_by_id(id)
        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  item.toJSON()}, 200
  
#  Return easy version of a test by id if exists
@rest_api.route('/test/easy_test/<int:id>')
class ItemManager(Resource):
    """
       Return easy version of a test by id if exists

    """
    def get(self, id):
        item = Datas.get_by_id(id)

        if not item.generated_test_latex_easy:
            return {"success": False,
                    "msg": "Item not found."}, 400

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  item.generated_test_latex_easy}, 200
    
    def put(self, id):
        item = Datas.get_by_id(id)
        if not item:
            return {"success": False, "msg": "Item not found."}, 400
        
        genreated_easy_test = clean_text_for_latex(get_genreated_easy_test(item.original_latex))
        Datas.update_generated_test_latex_easy(item, genreated_easy_test)
        
        # create latex file and export PDF file
        save_to_pdf(pdf_begin + genreated_easy_test + pdf_end, "test_easy_version")

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  genreated_easy_test}, 200
    

#  Return medium version of a test by id if exists
@rest_api.route('/test/medium_test/<int:id>')
class ItemManager(Resource):

    """
       Return all data by id
    """
    def get(self, id):
        item = Datas.get_by_id(id)

        if not item.generated_test_latex_medium:
            return {"success": False,
                    "msg": "Item not found."}, 400

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  item.generated_test_latex_medium}, 200
    
    def put(self, id):
        item = Datas.get_by_id(id)
        if not item:
            return {"success": False, "msg": "Item not found."}, 400
        
        genreated_medium_test = clean_text_for_latex(get_genreated_medium_test(item.original_latex))
        Datas.update_generated_test_latex_medium(item, genreated_medium_test)
        
        # create latex file and export PDF file
        save_to_pdf(pdf_begin + genreated_medium_test + pdf_end, "test_medium_version")

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  genreated_medium_test}, 200
    

#  Return hard version of a test by id if exists
@rest_api.route('/test/hard_test/<int:id>')
class ItemManager(Resource):
    """
       Return all data by id
    """
    def get(self, id):
        item = Datas.get_by_id(id)

        if not item.generated_test_latex_hard:
            return {"success": False,
                    "msg": "Item not found."}, 400

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  item.generated_test_latex_hard}, 200

    def put(self, id):
        item = Datas.get_by_id(id)
        if not item:
            return {"success": False, "msg": "Item not found."}, 400
        
        genreated_hard_test = clean_text_for_latex(get_genreated_hard_test(item.original_latex))
        Datas.update_generated_test_latex_hard(item, genreated_hard_test)
        
        # create latex file and export PDF file
        save_to_pdf(pdf_begin + genreated_hard_test + pdf_end, "test_hard_version")

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  genreated_hard_test}, 200


@rest_api.route('/question')
class Items(Resource):
    @rest_api.expect(create_model, validate=True)
    def post(self):

        # Read ALL input  
        req_data = request.get_json()

        # Get the url    
        original_question_url = req_data.get("data")

        # translate to latex
        latex_translation = get_latex_from_pdf(original_question_url)

        # generate tests

        # Create new object
        new_item = Datas(original_latex=latex_translation, 
                         type="question",
                         generated_test_latex_easy=None, 
                         generated_test_latex_medium=None, 
                         generated_test_latex_hard=None) 

        # Save the data
        new_item.save()
        
        return {"success": True,
                "msg"    : "Item successfully created",
                "data": new_item.id }, 200
    

@rest_api.route('/question/solution/<int:id>')
class Items(Resource):
    def get(self, id):

        item = Datas.get_by_id(id)

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        genreated_answer = clean_text_for_latex(
            ask_chat_gpt(
                "can you solve this question in latex: " + item.original_latex))
        
        # create latex file and export PDF file
        save_to_pdf(pdf_begin + genreated_answer + pdf_end, "solution")

        
        
        return {"success": True,
                "msg"    : "Item successfully created"}, 200
    
@rest_api.route('/question/hint/<int:id>')
class Items(Resource):
    def get(self, id):

        item = Datas.get_by_id(id)

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        genreated_answer = clean_text_for_latex(
            ask_chat_gpt(
                "can you give me a small hint? just the first stage in the solution of this question: " + item.original_latex))
        
        # create latex file and export PDF file
        save_to_pdf(pdf_begin + genreated_answer + pdf_end, "hint")

        return {"success": True,
                "msg"    : "Item successfully created"}, 200

#  Return easy version of a test by id if exists
@rest_api.route('/question/easy_question/<int:id>')
class ItemManager(Resource):
    def get(self, id):
        item = Datas.get_by_id(id)
        
        if not item:
            return {"success": False, "msg": "Item not found."}, 400
        
        genreated_easy_question = clean_text_for_latex(
            ask_chat_gpt("can you give me a new question that is easier than this one in latex:" + item.original_latex))
        
        # create latex file and export PDF file
        save_to_pdf(pdf_begin + genreated_easy_question + pdf_end, "test_easy_version")

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  genreated_easy_question}, 200
    

#  Return medium version of a question by id if exists
@rest_api.route('/question/medium_question/<int:id>')
class ItemManager(Resource):
    def get(self, id):
        item = Datas.get_by_id(id)
        
        if not item:
            return {"success": False, "msg": "Item not found."}, 400
        
        genreated_medium_question = clean_text_for_latex(
            ask_chat_gpt("can you give me a new question that is similar in difficulty to this one in latex:" + item.original_latex))
        
        # create latex file and export PDF file
        save_to_pdf(pdf_begin + genreated_medium_question + pdf_end, "test_medium_version")

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  genreated_medium_question}, 200
    
#  Return hard version of a question by id if exists
@rest_api.route('/question/hard_question/<int:id>')
class ItemManager(Resource):
    def get(self, id):
        item = Datas.get_by_id(id)
        
        if not item:
            return {"success": False, "msg": "Item not found."}, 400
        
        genreated_hard_question = clean_text_for_latex(
            ask_chat_gpt("can you give me a new question that is similar in difficulty to this one in latex:" + item.original_latex))
        
        # create latex file and export PDF file
        save_to_pdf(pdf_begin + genreated_hard_question + pdf_end, "test_hard_version")

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  genreated_hard_question}, 200
    
#  Return hard version of a question by id if exists
@rest_api.route('/question/feedback/img_answer')
class ItemManager(Resource):
    def get(self):

        # Read ALL input  
        req_data = request.get_json()

        # Get the url    
        url_question = req_data.get("url_question")
        url_answer = req_data.get("url_answer")

        # translate to latex
        question_tex = get_latex_from_pdf(url_question)
        answer_tex = get_latex_from_img(url_answer)
        
        genreated_answer = clean_text_for_latex(
            ask_chat_gpt("is my answer correct?" + question_tex + "," + answer_tex))
        
        # create latex file and export PDF file
        save_to_pdf(genreated_answer, "feedback")

        return {"success" : True,
                "msg"     : "Successfully return item",
                "data"    :  genreated_answer}, 200

@rest_api.route('/question/feedback')
class ItemManager(Resource):
    def get(self):

        # Read ALL input  
        req_data = request.get_json()

        # Get the url    
        data = req_data.get("data")

        # translate to latex
        data_tex = get_latex_from_img(data)
        
        feedback = pdf_begin
        feedback += clean_text_for_latex(
            ask_chat_gpt("is my answer correct?" + data_tex))
        feedback += pdf_end
        # create latex file and export PDF file
        save_to_pdf(feedback, "feedback")

        return {"success" : True,
                "msg"     : "Successfully return item",
                "data"    :  feedback}, 200

    
# requires saving the whole conversation
# @rest_api.route('/question/anotherhint') 
# class Items(Resource):
#     def get(self):

#         item = Datas.get_by_id(id)

#         if not item.generated_test_latex_medium:
#             return {"success": False,
#                     "msg": "Item not found."}, 400

#         ask_chat_gpt("can you give me a small hint? just the first stage in the solution of this question: " + item.original_latex)
        
#         return {"success": True,
#                 "msg"    : "Item successfully created"}, 200


