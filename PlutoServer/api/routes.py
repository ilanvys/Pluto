# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import request
from flask_restx import Api, Resource, fields
import subprocess

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
        print("new_item: ")
        print(new_item)
        
        return {"success": True,
                "msg"    : "Item successfully created"}, 200

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
        latex_file = "test_mit_latex.tex"
        subprocess.run(["pdflatex", "-interaction=nonstopmode", latex_file])

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
        
        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  genreated_hard_test}, 200
