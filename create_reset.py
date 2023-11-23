import firebase_admin
from firebase_admin import auth
import pyrebase

# Inicialize o SDK do Firebase Admin
cred = firebase_admin.credentials.Certificate('credentials/tarefas-fabrica-cb7ec-firebase-adminsdk-5y1rn-8916fa2870.json')
firebase_admin.initialize_app(cred)

def reset_password(email):
    try:
        # Envia um e-mail para redefinir a senha
        auth.generate_password_reset_link(email)
        print("Um e-mail para redefinição de senha foi enviado para", email)
    except firebase_admin.auth.AuthError as e:
        print("Erro ao enviar e-mail de redefinição de senha:", e)
        
reset_password('thaysmartines18@gmail.com')

# def create_user(email, password):
#     try:
#         user = auth.create_user(email=email, password=password)
#         print("Usuário criado com sucesso:", user.uid)
#         return user.uid
#     except ValueError as e:
#         print("Erro ao criar usuário:", e)
#         return None

# # Chamando a função para criar um novo usuário
# uid = create_user('thaysmartines18@gmail.com', '12345678')