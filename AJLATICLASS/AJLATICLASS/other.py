import requests
import json

BASE_URL= "http://127.0.0.1:8000"
# HEADERS = {'content-type':'application/json'}

def get_data(id=None):
    json_data=None
    url=f'{BASE_URL}/EmployeeApi/'
    response=requests.get(url=url)
    new_data=response.json()
    print(new_data)
# get_data()



# POST
def post_data():
    url = f'{BASE_URL}/Employeeapi/'

    data = {
        'name':'rahul',
        'mobile': 14294,
        'city': 'bangalore'
    }
    json_data = json.dumps(data)
    response = requests.post(url=url, data=json_data)
    print(response)
    res = response.json()
    print(f'Result is {res}')
post_data()


def update_data():
    # url = "http://127.0.0.1:8000" + "/empcreate/"
    url = f'{BASE_URL}/Employeeapi/'
    data = {
        'id': 2,
        'name': 'monaj raj',

    }
    json_data = json.dumps(data)
    response = requests.put(url=url, data=json_data)
    print(response)
    res = response.json()
    print(f'Result is {res}')
# update_data()

def delete_data():
    # url = "http://127.0.0.1:8000" + "/empcreate/"
    url = f'{BASE_URL}/Employeeapi/'
    data = { 'id': 3}
    json_data = json.dumps(data)
    response = requests.delete(url=url, data=json_data)
    print(response)
    res = response.json()
    print(f'Result is {res}')
# delete_data()