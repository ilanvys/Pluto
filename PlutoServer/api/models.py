# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime

import json

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Datas(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    original_latex = db.Column(db.UnicodeText, nullable=False)
    type = db.Column(db.String(), nullable=False)

    generated_test_latex_easy = db.Column(db.UnicodeText, nullable=True, default=None)
    generated_test_latex_medium = db.Column(db.UnicodeText, nullable=True, default=None)
    generated_test_latex_hard = db.Column(db.UnicodeText, nullable=True, default=None)

    def __repr__(self):
        return str( self.id ) 

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def update_data(self, new_data):
    #     self.data = new_data

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    def get_original_test_by_id(cls, id):
        return (cls.query.filter_by(id=id).first())

    def update_generated_test_latex_easy(self, new_value):
        self.generated_test_latex_easy = new_value
        db.session.commit()
    
    def update_generated_test_latex_medium(self, new_value):
        self.generated_test_latex_medium = new_value
        db.session.commit()

    def update_generated_test_latex_hard(self, new_value):
        self.generated_test_latex_medium = new_value
        db.session.commit()

    def toDICT(self):
        cls_dict = {}
        cls_dict['_id'] = self.id
        cls_dict['original_latex'] = self.original_latex
        cls_dict['type'] = self.type
        cls_dict['generated_test_latex_easy'] = self.generated_test_latex_easy
        cls_dict['generated_test_latex_medium'] = self.generated_test_latex_medium
        cls_dict['generated_test_latex_hard'] = self.generated_test_latex_hard

        return cls_dict

    def toJSON(self):
        return self.toDICT()
