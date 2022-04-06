from flask import Flask, render_template, request
from todocore.reqs.sign_in import sign_in_request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
   if request.method == 'GET':
      return render_template('test.html', name = 'Neel')
   else:
      email = request.form['email']
      password = request.form['password']
      print(sign_in_request(email, password))
      return "This is a response for POST request"
   

if __name__ == '__main__':
   app.run()