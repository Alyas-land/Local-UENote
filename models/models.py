from app import db
from persiantools.jdatetime import JalaliDateTime

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Colummn(db.String(200), nullable=False, default= JalaliDateTime.now().strftime("%Y/%m/%d -- %H:%M"))

    def __repr__(self):
        return f'{self.title} project was created at {self.created_at}'
    
    note = db.relationship('product', backref='project', lazy=True)

    

class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=True)
    created_at = db.Colummn(db.String(200), nullable=False, default= JalaliDateTime.now().strftime("%Y/%m/%d -- %H:%M"))

    project_id = db.Column(db.Integer, db.ForeingKey('projects.id'), nullable=False)
