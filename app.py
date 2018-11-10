from flask import Flask, render_template, request

bob = Flask(__name__)
application = bob # FastComet hosting (CPanel) uses Phusion Passenger, and needs application

@bob.route('/')
def slash():
    return render_template('index.html')

@bob.route('/cv')
def cv():
    return render_template('cv.html')

@bob.route('/engineering')
def engineering():
    return render_template('engineering.html')

@bob.route('/research')
def research():
    return render_template('research.html')

@bob.route('/photography')
def photography():
    return render_template('photography.html')

# @bob.route('/lay')
# def layout():
#     return render_template('layout.html')

if __name__ == "__main__":
    bob.run(debug=True)
