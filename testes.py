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

KV = '''
<TarefaListItem@TwoLineAvatarIconListItem>:
    text: root.text
    secondary_text: root.secondary_text

    CheckboxLeftWidget:
        id: checkbox

    BoxLayout:
        orientation: "horizontal"
        size_hint_x: None
        size_hint_y: None
        size: self.minimum_size
        padding: "5dp"
        spacing: "10dp"
        pos_hint: {"right": 1, "top": 1}

        IconRightWidget:
            id: delete_icon
            icon: 'trash-can-outline'
            theme_text_color: "Custom"
            text_color: 1, 0.043, 0 
            on_release: root.delete_task()

        IconRightWidget:
            id: edit_icon
            icon: "pencil"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            on_release: root.edit_task()
            

<ContentNavigationDrawer>:



    MDList:
        OneLineAvatarListItem:
            text: "Concluidas"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 5"
            IconLeftWidget:
                icon: "check-circle-outline"

        OneLineAvatarListItem:
            text: "Tarefas"
            on_press:
                app.listar_tarefas()
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"
            IconLeftWidget:
                icon: "format-list-checkbox"

        OneLineAvatarListItem:
            text: "Adicionar Tarefas"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 3"
            IconLeftWidget:
                icon: "plus-circle-outline"




MDScreen:



    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager
            
#  --------------------------------------------Tela inicial -----------------------------------------------------------------------------
            MDScreen:
                name: "scr 0"
                
                
                FloatLayout: 
                        

                    Image:
                        source: "images/logo_listview.png"
                        size_hint:(0.8, 0.8)
                        pos_hint: {"center_x": 0.5, "center_y": 0.7 }
                        
                    MDLabel:
                        text: "Seja bem vindo!"
                        font_style:'H5'
                        bold: True
                        halign: 'center'
                        pos_hint: {"center_x": 0.5, "center_y": 0.4 }
                        
                        
                        
                        
                    MDFillRoundFlatButton:
                        text: 'Começar'
                        elevation: 1
                        text_color: 1, 1, 1, 1
                        pos_hint: {"center_x": 0.5, "center_y": 0.2}
                        size_hint_x: .8
                        on_release: app.comecar()
                        
                    MDRectangleFlatIconButton:
                        text: "Não tem conta? Cadastre-se"
                        icon: "account-plus"
                        line_color: 0, 0, 0, 0
                        pos_hint: {"center_x": .5, "center_y": .1}
                        padding: '10dp'
                        on_release: app.nao_tem_conta_cadastre()



# ------------------------------------------------------------ tela de login -------------------------------------------------------------

            MDScreen:
                name: "scr 1"
                
                
                FloatLayout: 
                
                    MDTopAppBar:
                        md_bg_color: 1,1,1,0
                        elevation: 0
                        pos_hint: {"top": 1}
                        left_action_items: [["arrow-left", lambda x: app.callback()]]

                        
                    
                    Image:
                        source: "images/user.png"
                        size_hint:(0.5, 0.5)
                        pos_hint: {"center_x": 0.5, "center_y": 0.7 }
                        
                    MDLabel:
                        text: "Seja bem vindo!"
                        font_style:'H5'
                        bold: True
                        halign: 'center'
                        pos_hint: {"center_x": 0.5, "center_y": 0.6 }
                        
                    MDLabel:
                        text: "Faça o login para continuar"
                        font_style:'Caption'
                        halign: 'center'
                        pos_hint: {"center_x": 0.5, "center_y": 0.55 }
                        
                    MDTextField:
                        id: username
                        hint_text:"Email"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5 }
                        size_hint_x: .8
                        icon_right: 'email'
                        
                    MDTextField:
                        id: password
                        hint_text:"Senha"
                        pos_hint: {"center_x": 0.5, "center_y": 0.4 }
                        size_hint_x: .8
                        icon_right: 'lock'
                        password: True
                        multiline: True
                        
                    MDRectangleFlatIconButton:
                        text: "Esqueci minha senha"
                        line_color: 0, 0, 0, 0
                        pos_hint: {"center_x": .5, "center_y": .3}
                        padding: '10dp'
                        
                        
                        
                    MDFillRoundFlatButton: 
                        text: 'Entrar'
                        on_release: app.login()
                        elevation: 1
                        text_color: 1,1,1,1
                        pos_hint: {"center_x": 0.5, "center_y": 0.2 }
                        size_hint_x: .8
                        
                        
                    MDRectangleFlatIconButton:
                        text: "Não tem conta? Cadastre-se"
                        icon: "account-plus"
                        line_color: 0, 0, 0, 0
                        pos_hint: {"center_x": .5, "center_y": .1}
                        padding: '10dp'
                        on_release: app.nao_tem_conta_cadastre()


                                                        
                            # ---------------------------------------------------------LISTANDO TAREFAS ---------------------------------------------------
            MDScreen:
                name: "scr 2"

                GridLayout:
                    cols: 1

                    MDTopAppBar:
                        title: "Tarefas"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        

                    ScrollView:
                        MDList:
                            id: tarefas_list
                            
                            
                           # ------------------------------------------------tarefas concluidas------------------------------------------------------------------------
                           
            MDScreen:
                name: "scr 5"

                GridLayout:
                    cols: 1

                    MDTopAppBar:
                        title: "Concluidas"
                        elevation: 10
                        pos_hint: {"top": 1}
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        

                    ScrollView:
                        MDList:
                            id: historico
                           
                    
                           # -------------------------------------------CADASTRANDO USUÁRIOOOOOO -----------------------------
            MDScreen:
                name: "scr 4"
                
                
                FloatLayout: 

                        
                         
                    MDLabel:
                        text: "Cadastre-se!"
                        font_style:'H5'
                        bold: True
                        halign: 'center'
                        pos_hint: {"center_x": 0.5, "center_y": 0.8 }
                    
                        
                    MDTextField:
                        id: email_user
                        hint_text:"Email"
                        pos_hint: {"center_x": 0.5, "center_y": 0.7 }
                        size_hint_x: .8
                        icon_right: 'email'
                        
                    MDTextField:
                        id: tel_user
                        hint_text:"Telefone"
                        pos_hint: {"center_x": 0.5, "center_y": 0.6 }
                        size_hint_x: .8
                        icon_right: 'phone-settings'
                        
                    MDTextField:
                        id: cpf_user
                        hint_text:"CPF"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5 }
                        size_hint_x: .8
                        icon_right: 'id-card'
                        
                    MDTextField:
                        id: password_user
                        hint_text:"Crie uma senha"
                        pos_hint: {"center_x": 0.5, "center_y": 0.4 }
                        size_hint_x: .8
                        icon_right: 'lock'
                        password: True
                        
                    MDLabel:
                        text: "A senha deve ter pelo menos 8 caracteres."
                        font_style:'Caption'
                        halign: 'left'
                        pos_hint: {"center_x": 0.6, "center_y": 0.35 }
                        
                    MDLabel:
                        text: "A senha deve conter letras e números."
                        font_style:'Caption'
                        halign: 'left'
                        pos_hint: {"center_x": 0.6, "center_y": 0.32 }
                        
                    MDLabel:
                        text: "A senha deve conter caracteres especiais."
                        font_style:'Caption'
                        halign: 'left'
                        pos_hint: {"center_x": 0.6, "center_y": 0.29 }
                        
                        
                        
                    MDFillRoundFlatButton: 
                        text: 'Criar conta'
                        on_release: app.cadastrar_user()
                        elevation: 1
                        text_color: 1,1,1,1
                        pos_hint: {"center_x": 0.5, "center_y": 0.2 }
                        size_hint_x: .8
                        
                MDTopAppBar:
                    elevation: 0
                    pos_hint: {"top": 1}
                    left_action_items: [["arrow-left", lambda x: app.voltar_login()]]

#  --------------------------------------------------------------CADASTRANDO TAREFAS -------------------------------------------------
            MDScreen:
                name: "scr 3"
                
                MDTopAppBar:
                    elevation: 0
                    pos_hint: {"top": 1}
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                MDLabel:
                    text: "Cadastrar Tarefas"
                    font_style:'H5'
                    bold: True
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                    size_hint_x: .5

                MDTextField:
                    id: nome
                    hint_text: "Titulo"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .6}
                    size_hint_x: .5
                    icon_right: 'format-title'

                MDTextField:
                    id: descricao
                    hint_text: "Descrição"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint_x: .5
                    icon_right: 'comment-alert-outline'

                MDBoxLayout:
                    adaptive_height: True
                    md_bg_color: app.theme_cls.primary_color

                MDTextField:
                    id: status
                    hint_text: "Status da tarefa"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .4}
                    size_hint_x: .5
                    icon_right: 'check-circle'
                    on_focus: app.show_status_menu(self) if self.focus else None

                MDTextField:
                    id: data
                    hint_text: "Data de conclusão"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .3}
                    size_hint_x: .5
                    icon_right: 'calendar-today'

                MDRoundFlatIconButton:
                    id: cadastro_tarefa
                    on_press: app.cadastrar(nome.text, descricao.text, status.text, data.text)
                    text: "Cadastrar"
                    icon: "content-save-check"
                    icon_color: "white"
                    text_color: "white"
                    line_color: "white"
                    md_bg_color: "#428F58"
                    pos_hint: {"center_x": .5, "center_y": .1}
                    size_hint_x: .2


        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer


'''


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
        # Add functionality to edit the task here
        app = MDApp.get_running_app()
        app.edit_task(self.tarefa_id, self.text, self.secondary_text)
        
    def edit_task(self):
            app = MDApp.get_running_app()
            app.show_edit_task_popup(self.tarefa_id, self.text, self.secondary_text)
        



class Example(MDApp):
        
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)
    
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


    def show_password_error_dialog(self, message):
        dialog = MDDialog(
            title="Erro na Senha",
            text=message,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

            

    def nao_tem_conta_cadastre(self):
        self.root.ids.screen_manager.current = "scr 4"

    def comecar(self):
        self.root.ids.screen_manager.current = "scr 1"


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
        # Implemente a funcionalidade de edição aqui
        # Você pode querer criar um diálogo ou uma tela para editar os detalhes da tarefa
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








Example().run()
