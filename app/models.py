from app import db
from datetime import datetime


class Quiz(db.Model):
    """
    Model Class representing the quiz object.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    flavor_text = db.Column(db.Text, default="")
    created_date = db.Column(db.DateTime, default=datetime.utcnow())
    publish_date = db.Column(db.DateTime, default=datetime.utcnow())
    rounds = db.relationship('Round', cascade='all, delete',
                             backref='quiz', lazy='dynamic')
    
    def __repr__(self):
        return '<Quiz %r>' % (self.title)


class Round(db.Model):
    """
    Each round of the Quiz
    """
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    title = db.Column(db.String(256))
    decay = db.Column(db.Integer, default=1)
    max_score = db.Column(db.Integer, default=1)
    questions = db.relationship('Question', cascade='all, delete',
                                backref='round', lazy='dynamic')

    def __repr__(self):
        return '<QuizRound %r>' % (self.title)


class Question(db.Model):   
    """
    Each question in the the round of quiz
    """
    
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text)
    answer_text = db.Column(db.Text)
    max_score = db.Column(db.Integer, default=1)
    decay = db.Column(db.Integer, default=1)
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'))
    
    def __repr__(self):
        return '<Question %r %r %r %r >' % (self.question_text,
                                                self.answer_text,
                                                self.max_score,
                                                self.decay)
