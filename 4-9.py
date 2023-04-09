#웹게시판 만들기
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Board %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        board_title = request.form['title']
        board_content = request.form['content']
        new_board = Board(title=board_title, content=board_content)

        try:
            db.session.add(new_board)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your board'

    else:
        boards = Board.query.order_by(Board.date_created).all()
        return render_template('index.html', boards=boards)
    
@app.route('/delete/<int:id>')
def delete(id):
    board_to_delete = Board.query.get_or_404(id)

    try:
        db.session.delete(board_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that board'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    board = Board.query.get_or_404(id)

    if request.method == 'POST':
        board.title = request.form['title']
        board.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your board'

    else:
        return render_template('update.html', board=board)
    
if __name__ == "__main__":
    app.run(debug=True)





