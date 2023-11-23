from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
import pyrebase
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivy.factory import Factory
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivy.uix.checkbox import CheckBox
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.utils import get_color_from_hex
from kivymd.uix.button import MDFlatButton




config = {
    "apiKey": "AIzaSyDvxqlbNSDmWQxi0NvQ4dnAbDnjWr4P6Gg",
    "authDomain": "tarefas-fabrica-cb7ec.firebaseapp.com",
    "databaseURL": "https://tarefas-fabrica-cb7ec-default-rtdb.firebaseio.com",
    "projectId": "tarefas-fabrica-cb7ec",
    "storageBucket": "tarefas-fabrica-cb7ec.appspot.com",
    "messagingSenderId": "815717806231",
    "appId": "1:815717806231:web:4467768c5769b182be39d2",
    "measurementId": "G-T36N0ZQEF7"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    
    def voltar_para_tela_inicial(self):
        self.screen_manager.current = "scr 0"
    

class EditTaskDialogContent(MDBoxLayout):
    def __init__(self, tarefa_nome, tarefa_descricao, **kwargs):
        super(EditTaskDialogContent, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.height = "100dp"
        self.spacing = "10dp" 

        self.nome_input = MDTextField(
            hint_text="Nome da tarefa",
            text=tarefa_nome,
            
        )

        self.descricao_input = MDTextField(
            hint_text="Descrição da tarefa",
            text=tarefa_descricao
            
        )

        self.add_widget(self.nome_input)
        self.add_widget(self.descricao_input)

    def get_edited_task_details(self):
        return {
            'nome': self.nome_input.text,
            'descricao': self.descricao_input.text
        }
        
          

class TarefaListItem(TwoLineAvatarIconListItem):
    checkbox = ObjectProperty()
    tarefa_id = ObjectProperty()  

    def __init__(self, text, secondary_text, tarefa_id, checkbox_active=False, **kwargs):
        super(TarefaListItem, self).__init__(text=text, secondary_text=secondary_text, **kwargs)
        self.tarefa_id = tarefa_id 


    def add_checkbox(self):
        if not self.checkbox:
            self.checkbox = CheckBox(active=False)  
            self.add_widget(self.checkbox)


    def delete_task(self):
        app = MDApp.get_running_app()
        app.confirmar_excluir(self.tarefa_id)
        
  
        
    def edit_task(self):
            app = MDApp.get_running_app()
            app.show_edit_task_popup(self.tarefa_id, self.text, self.secondary_text)
        



class Example(MDApp):
        
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        return Builder.load_file("views/main.kv")
    
    def callback(self):
        self.root.ids.screen_manager.current = "scr 0"
        
    def voltar_login(self):
        self.root.ids.screen_manager.current = "scr 1"
        
    def on_password_change(self, instance, value):
        self.update_password_color(value)
        
        self.root.ids.password.bind(text=self.on_password_change)
    
    
    def show_status_menu(self, instance_textfield):
        if instance_textfield.focus:
            menu_items = [
                {
                    "viewclass": "OneLineListItem",
                    "text": "A Fazer",
                    "on_release": lambda x=f"A Fazer": self.set_status(instance_textfield, x)
                },
                {
                    "viewclass": "OneLineListItem",
                    "text": "Em Andamento",
                    "on_release": lambda x=f"Em Andamento": self.set_status(instance_textfield, x)
                },
                {
                    "viewclass": "OneLineListItem",
                    "text": "Pendente",
                    "on_release": lambda x=f"Pendente": self.set_status(instance_textfield, x)
                },
            ]
            menu = MDDropdownMenu(
                caller=instance_textfield,
                items=menu_items,
                width_mult=4
            )
            menu.open()

    def set_status(self, instance_textfield, text):
        instance_textfield.text = text

    
    def cadastrar(self, nome, descricao, status_tarefa, data_tarefa):
        db.child("tarefas").push({
            'nome':nome,
            'descricao':descricao,
            "status_tarefa":status_tarefa,
            "data_tarefa":data_tarefa
        })
        self.show_success_dialog()
        self.limpar_campos_tarefa()
        

    def delete_task(self, tarefa_id):
        try:
            db.child("tarefas").child(tarefa_id).remove()
            self.listar_tarefas()
            print(f"Tarefa com ID {tarefa_id} excluída com sucesso no banco de dados.")
        except Exception as e:
            print(f"Erro ao excluir tarefa no banco de dados: {str(e)}")
            

    

    def login(self):
        username = self.root.ids.username.text
        password = self.root.ids.password.text
        autenticacao = firebase.auth()
        try:
            username = autenticacao.sign_in_with_email_and_password(username, password)
            print("Login bem-sucedido.")
            self.root.ids.screen_manager.current = "scr 3"
        except Exception as e:
            print(f"Erro ao fazer login: {str(e)}")
            self.show_error_dialog()
            

        

    def senha_forte(self, password):
        # Verifica o comprimento da senha
        if len(password) < 8:
            return False, "A senha deve ter pelo menos 8 caracteres."

        # Verifica se a senha contém caracteres alfanuméricos
        has_alpha = any(char.isalpha() for char in password)
        has_digit = any(char.isdigit() for char in password)
        if not (has_alpha and has_digit):
            return False, "A senha deve conter letras e números."

        # Verifica se a senha contém caracteres especiais
        special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
        has_special = any(char in special_characters for char in password)
        if not has_special:
            return False, "A senha deve conter caracteres especiais."

        return True, "Senha forte!"

    def cadastrar_user(self):
        email = self.root.ids.email_user.text
        senha = self.root.ids.password_user.text

        # Verificação de senha forte
        is_strong_password, message = self.senha_forte(senha)
        if not is_strong_password:
            self.show_password_error_dialog(message)
            return

        autenticacao = firebase.auth()
        try:
            new_user = autenticacao.create_user_with_email_and_password(email, senha)
            print("Usuário criado com sucesso!")
            

            # ARMAZENA INFORMAÇÕES A MAIS CRIANDO UM JSON
            user_data = {
                "cpf": self.root.ids.cpf_user.text,
                "telefone": self.root.ids.tel_user.text
            }
            db.child("usuarios").child(new_user['localId']).set(user_data)

            self.show_success_account()  # Mostra o diálogo de sucesso
            self.root.ids.screen_manager.current = "scr 1"
        except Exception as e:
            print(f"Erro ao criar usuário: {str(e)}")
            self.limpar_cadastro_user()
        

    def esqueci_senha(self, email):
        autenticacao = firebase.auth()
        try:
            autenticacao.send_password_reset_email(email)
            print("Email de redefinição de senha enviado com sucesso!")
            # Adicione aqui o código para exibir uma mensagem de sucesso
        except Exception as e:
            print(f"Erro ao enviar email de redefinição de senha: {str(e)}")


    def nao_tem_conta_cadastre(self):
        self.root.ids.screen_manager.current = "scr 4"

    def comecar(self):
        self.root.ids.screen_manager.current = "scr 1"

    def abrir_edicao_senha(self):
            self.root.ids.screen_manager.current = "scr 6"
            
    def listar_tarefas(self):
            tarefas_list = self.root.ids.tarefas_list
            tarefas_list.clear_widgets()

            tarefas = db.child("tarefas").get()
            if tarefas.each():
                for tarefa in tarefas.each():
                    tarefa_nome = tarefa.val()['nome']
                    tarefa_descricao = tarefa.val()['descricao']

                    tarefa_id = tarefa.key()  

                    tarefa_label = TarefaListItem(
                        text=f"{tarefa_nome}",
                        secondary_text=f"{tarefa_descricao}",
                        tarefa_id=tarefa_id 
                    )

                    tarefas_list.add_widget(tarefa_label)
                    
    def edit_task(self, tarefa_id, tarefa_nome, tarefa_descricao):
        print(f"Editando tarefa com ID: {tarefa_id}")
        print(f"Nome atual: {tarefa_nome}")
        print(f"Descrição atual: {tarefa_descricao}")
        
        
    def show_edit_task_popup(self, tarefa_id, tarefa_nome, tarefa_descricao):
        dialog_content = EditTaskDialogContent(tarefa_nome, tarefa_descricao)
        largura = "400dp"
        altura = "500dp"
        dialog = MDDialog(
            title="",
            type="custom",
            content_cls=dialog_content,
            buttons=[
                MDRaisedButton(
                    text="Salvar",
                    on_release=lambda *args: (self.save_edited_task(tarefa_id, dialog_content.get_edited_task_details()), dialog.dismiss())
                ),
                MDRaisedButton(
                    text="Cancelar",
                    on_release=lambda *args: dialog.dismiss()
                )
            ],
            size_hint=(None, None),  # Desativa o redimensionamento automático
            size=(largura, altura)
        )
        dialog.open()

    
  
        
    def save_edited_task(self, tarefa_id, edited_task_details):
            print(f"Salvando detalhes editados para a tarefa ID: {tarefa_id}")
            print("Novo Nome:", edited_task_details['nome'])
            print("Nova Descrição:", edited_task_details['descricao'])

            # Verifica se a descrição está vazia
            if not edited_task_details['descricao']:
                edited_task_details['descricao'] = "Descrição Vazia"  # ou adicione qualquer outro texto padrão

            # Atualiza os detalhes da tarefa no Firebase
            try:
                db.child("tarefas").child(tarefa_id).update(edited_task_details)
                self.listar_tarefas()
                print(f"Tarefa com ID {tarefa_id} atualizada com sucesso.")
            except Exception as e:
                print(f"Erro ao atualizar tarefa no banco de dados: {str(e)}")

# ----------------------------------------------------------------------LIMPAR DADOS---------------------------------------------------------
    def limpar_cadastro_user(self, dialog):
        dialog.dismiss()
        # Limpa os campos após os dados serem salvos
        self.root.ids.email_user.text = ""
        self.root.ids.tel_user.text = ""
        self.root.ids.cpf_user.text = ""
        self.root.ids.password_user.text = ""
        
        
    def limpar_campos_tarefa(self):
        self.root.ids.nome.text = ""
        self.root.ids.descricao.text = ""
        self.root.ids.status.text = ""
        self.root.ids.data.text = ""

#  ----------------------------------------------------------------------- POP UPS -----------------------------------------------------------


    def show_error_dialog(self):
        dialog = MDDialog(
            title="Erro de Login",
            text="Usuário ou senha incorretos.",
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()
        
    def show_success_dialog(self):

        dialog = MDDialog(
            title="Tarefa Cadastrada",
            text="Tarefa cadastrada com sucesso.",
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()
        
    def show_success_account(self):

        dialog = MDDialog(
            title="Conta Criada",
            text="Conta criada com sucesso.",
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: self.limpar_cadastro_user(dialog)
                )
            ]
        )

        dialog.open()

    def confirmar_excluir(self, tarefa_id):
            def delete_instance(instance):
                try:
                    self.delete_task(tarefa_id)  # Exclui a tarefa do banco de dados
                    dialog.dismiss()
                except Exception as e:
                    print(f"Erro ao excluir tarefa: {str(e)}")

            dialog = MDDialog(
                title="Confirmação",
                text="Tem certeza que deseja excluir?",
                buttons=[
                    MDRaisedButton(
                        text="Sim",
                        on_release=delete_instance
                    ),
                    MDRaisedButton(
                        text="Não",
                        on_release=lambda *args: dialog.dismiss()
                    ),
                ]
            )
            dialog.open()
            
    def show_reset_success_dialog(self):
        dialog = MDDialog(
            title="Email Enviado",
            text="Um email de redefinição de senha foi enviado.",
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def show_reset_error_dialog(self):
        dialog = MDDialog(
            title="Erro",
            text="Erro ao enviar o email de redefinição de senha.",
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()









Example().run()

