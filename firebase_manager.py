import firebase_admin
from firebase_admin import credentials, db

class FirebaseManager:
    def __init__(self, credential_path, database_url):
        self.cred = credentials.Certificate(credential_path)
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': database_url
        })
    
    def get_projects(self):
        return db.reference('projects').get()
    
    def create_project(self, project_name):
        return db.reference('projects').push({
            'name': project_name,
            'created_at': {'.sv': 'timestamp'}
        })
    
    def save_conversation(self, project_id, conversation_data):
        return db.reference(f'projects/{project_id}/conversations').push(conversation_data)
    
    def update_conversation(self, project_id, conversation_id, updated_data):
        return db.reference(f'projects/{project_id}/conversations/{conversation_id}').update(updated_data)
    
    def delete_conversation(self, project_id, conversation_id):
        return db.reference(f'projects/{project_id}/conversations/{conversation_id}').delete()