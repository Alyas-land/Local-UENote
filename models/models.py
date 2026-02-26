from extensions import db
from persiantools.jdatetime import JalaliDateTime

class Project(db.Model):
    __tablename__ = 'projects'
    __table_args__ = {'extend_existing': True}   # add this as table arguments

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.String(200), nullable=False, default= JalaliDateTime.now().strftime("%Y/%m/%d -- %H:%M"))

    def __ini__(self, title, description):
        self.title = title
        self.description = description

        
    def __repr__(self):
        return f'{self.title} project was created at {self.created_at}'
    
    note = db.relationship('Note', backref='project', lazy=True)

    

class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.String(200), nullable=False, default= JalaliDateTime.now().strftime("%Y/%m/%d -- %H:%M"))

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
