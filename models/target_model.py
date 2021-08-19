from db import db

class TargetModel(db.Model):
    __tablename__ = "targets"
    
    id = db.Column(db.Integer, primary_key=True)
    first_number = db.Column(db.Integer())
    second_number = db.Column(db.Integer())
    third_number = db.Column(db.Integer())
    target_type = db.Column(db.String(20))
    description = db.Column(db.String())
    name = db.Column(db.String())
    
    def __init__(self, first_number, second_number, third_number, target_type, description, name):
        self.first_number = first_number
        self.second_number = second_number
        self.third_number = third_number
        self.target_type = target_type
        self.description = description
        self.name = name
                
    def to_json(self):
        return {"name": self.name,
                "id": self.id,
                "description": self.description,
                "first_number": self.first_number,
                "second_number": self.second_number,
                "third_number": self.third_number,
                "target_type": self.target_type,
                "target_title": self.get_target_title()}
    
    def get_target_title(self):
        return str(self.first_number) + "." + str(self.second_number) + "." + str(self.third_number) + " " + self.target_type
    
    def save (self):
        db.session.add(self)
        db.session.commit()
        
    def deleteMe(self):
        db.session.delete(self)
        db.session.commit()
        
        
    @classmethod
    def get_all_targets(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()