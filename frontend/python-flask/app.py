from cProfile import run
import re
from flask import Flask, render_template, request, redirect, url_for, make_response
from urllib3 import Retry
from todocore.reqs.sign_in import sign_in_request
from todocore.reqs.fetch_by_user import read_task
from todocore.reqs.create_task import create_task
from todocore.reqs.delete_task import delete_task

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
   if request.method == 'GET':
      return render_template('test.html', name = 'Neel')
   else:
      email = request.form['email']
      password = request.form['password']
      _, objectId = sign_in_request(email, password)
      
      return make_response(render_template('handle_login.html', id = objectId))

@app.route('/profile', methods=['GET'])
def profile():
   try:
      token = request.args['token']
   except:
      return redirect(url_for('hello_world'))
   tasks = read_task(token)
   tasks.reverse()
   print(len(tasks))
   return render_template('profile.html', tasks = tasks)

@app.route('/logout', methods=['GET'])
def logout():
   return render_template('logout.html')

@app.route('/create_task', methods=['GET','POST'])
def create():
   if request.method == 'GET':
      return render_template('create_task.html')
   else:
      task = request.form['task']
      token = request.form['token']
      if task == "" :
         return render_template('create_task.html', error = True)
      message = create_task(token, task)
      if message == 'Task saved':
         return render_template('create_task.html', successful = True)
      return render_template('create_task.html')

@app.route('/complete_task', methods=['POST'])
def done_task():
   task_id = request.form['task_id']
   try:
      delete_task(task_id)
      return "success", 200
   except:
      return "failed", 500
      
   
      
   
if __name__ == '__main__':
   app.run()