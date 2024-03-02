from flask import Flask, render_template
from src.model import Staff, Shift 
from src.DAO import DAO

app = Flask(__name__, template_folder='src/templates')

@app.route('/')
def index():
    # dao= DAO()
    # staff = dao.get(entity="staff", id=1)
    # print(staff)
    return render_template('index.html')

# @app.route('/shift/start/<staff_id>', methods=['POST'])
# def record(staff_id):
#     dao = DAO()
#     staff = dao.get(entity="staff", id=staff_id)
    
#     staff_role = staff['role']
#     new_shift = Shift(id = get_uuid(),
#                       start_time=get_datetime(),
#                       date = get_datetime(),
#                       role=get_role(staff_id))
#     dao.save(new_shift)
    
#     return f'<html><body><h1>Shift Recorder</h1><h2> DevOps Prac </h2></body></html>'

@app.route('/shift/end/<shift_id>', methods=['POST'])
def end(id):
    pass

@app.route('/shift/<staff_id>', methods=['GET'])
def get_staff_shift(staff_id):
    return f'<html><body><h1>Shift Recorder</h1><h2> DevOps Prac </h2><h3> Staff({staff_id}) records: </h3>></body></html>'

@app.route('/staff', methods=['GET'])
def get_staff(staff_id):
    return staff_id

def get_uuid():
    import uuid
    new_id = uuid.uuid4().hex
    return new_id

def get_datetime():
    import datetime
    return datetime.datetime.now().strftime('%m/%d/%Y %H/%M/%S')

def get_role(id):
    return "Hero"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)