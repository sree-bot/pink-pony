from app import db
from datetime import datetime


class Quiz(db.Model):
    """
    Model Class representing the quiz object.
    """
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    flavor_text = db.Column(db.Text)
    created_date = db.Column(db.DateTime)
    publish_date = db.Column(db.DateTime)
    no_of_rounds = db.Column(db.Integer)
    #rounds = db.relationship('QuizRound', backref = 'quiz', lazy = 'dynamic')
    
    def __repr__(self):
        return '<Quiz %r , created on %r to be published on %r with %r rounds>' % (title, created_date, publish_date, rounds)


class Round(db.Model):
    """
    Each round of the Quiz
    """
    id = db.Column(db.Integer, primary_key = True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    title = db.Column(db.String(256))
    no_of_questions = db.Column(db.Integer, default = 1)
    decay = db.Column(db.Integer, default = 1)
    max_score = db.Column(db.Integer)
    
    def __repr__(self):
        return '<QuizRound title %r no_of_questions %r decay rate %r max_score_per_question %r>' % (title, no_of_question, decay, max_score)


class Question(db.Model):
    """
    Each question in the the round of quiz
    """
    
    id = db.Column(db.Integer, primary_key = True)
    question_text = db.Column(db.Text)
    answer_text = db.Column(db.Text)
    max_score = db.Column(db.Integer)
    decay = db.Column(db.Integer)
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'))
    
    def __repr__(self):
        return '<Question %r %r %r %r >' % (question_text, answer_text, max_score, decay)