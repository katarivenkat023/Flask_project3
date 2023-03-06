from flask import Flask,render_template
AI=Flask(__name__)


@AI.route('/wish')
def wish():
    return '<h1>good morning...!!</h1>'
@AI.route('/venkat/<na>')
def venkat(na):
    return f'<h1>Good morning...{na}<h1>'
@AI.route('/honny')
def honny():
    return render_template('first.html')


if __name__=='__main__':
    AI.run(debug=True)