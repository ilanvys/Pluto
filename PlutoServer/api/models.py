# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime

import json

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Datas(db.Model):

    test_id           = db.Column(db.Integer()   , primary_key=True)
    date_created = db.Column(db.DateTime()  , default=datetime.utcnow)
    test_data_latex         = db.Column(db.UnicodeText , nullable=False)
    generated_test_latex         = db.Column(db.UnicodeText, nullable=False)

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
    
    def get_test_by_id(cls, id):
        return (cls.query.filter_by(id=id).first())['test_data_latex']
    
    def get_generated_test_by_id(cls, id):
        return (cls.query.filter_by(id=id).first())['generated_test_latex']

    def toDICT(self):

        cls_dict         = {}
        cls_dict['_id']  = self.id
        cls_dict['test_data_latex'] = self.test_data_latex
        cls_dict['generated_test_latex'] = self.generated_test_latex

        return cls_dict

    def toJSON(self):

        return self.toDICT()
