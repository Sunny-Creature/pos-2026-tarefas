import requests

api_url = "http://jsonplaceholder.typicode.com/users"

def list_users():
    users = requests.get(api_url)
    if users.status_code == 200:
        return users.json()
    else:
        return False
    
def detail_user(user_id):
    user = requests.get(api_url + f"/{user_id}")
    if user.status_code == 200:
        return user.json()
    else:
        return False
    
def create_user(user_data):
    new_user = requests.post(api_url, json=user_data)
    if new_user.status_code == 201:
        return new_user.json()
    else:
        return False
    
def update_user(user_id, user_data):
    updated_user = requests.patch(api_url + f"/{user_id}", json=user_data)
    if updated_user.status_code == 200:
        return updated_user.json()
    else:
        return False
    
def delete_user(user_id):
    deleted_user = requests.delete(api_url + f"/{user_id}")
    print(deleted_user)
    if deleted_user.status_code == 200:
        return True
    else:
        return False