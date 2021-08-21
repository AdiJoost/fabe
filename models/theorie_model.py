from db import db

class TheorieModel(db.Model):
    __tablename__ = "theories"
    
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.String())
    name = db.Column(db.String())
    picture = db.Column(db.String())
    
    def __init__(self, name, html, picture):
        self.name = name
        self.html = html
        self.picture = picture
                
    def to_json(self):
        return {"name": self.name,
                "id": self.id,
                "picture": self.picture,
                "html": self.html}
    
    
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