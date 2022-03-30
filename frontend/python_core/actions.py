from reqs.sign_in import sign_in_request

class ParseAction:
    def sign_in(self, email, password):
        return sign_in_request(email=email, password=password)
    
    def view_tasks(self, user_id):
        pass
    
    def create_task(self, task, due_date, user_id):
        pass
    
    def complete_task(self, task_id):
        pass