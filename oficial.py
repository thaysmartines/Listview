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

        OneLineListItem:
            text: "Concluidas"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 5"

        OneLineListItem:
            text: "Tarefas"
            on_press:
                app.listar_tarefas()
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"


        OneLineListItem:
            text: "Adicionar Tarefas"
            on_press:

                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 3"



MDScreen:



    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager
#  --------------------------------------------LOGIN DO USUÁRIO -----------------------------------------------------------------------------
            MDScreen:
                name: "scr 1"
                
                MDTopAppBar:
                    title: "Listview"
                    elevation: 0
                    pos_hint: {"top": 1}
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    

                MDCard:
                    size_hint: None, None
                    size: "300dp", "250dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.6}

                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'

                        MDLabel:
                            text: "Login"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                            halign: "center"
                            pos_hint: {"center_x": .5, "center_y": .8}
                            size_hint_x: .5
                            

                        MDTextField:
                            id: username
                            hint_text: "Usuário"
                            multiline: True

                        MDTextField:
                            id: password
                            hint_text: "Senha"
                            password: True
                            multiline: True

                        MDRaisedButton:
                            text: "Entrar"
                            on_release: app.login()
                            pos_hint: {"center_x": .5, "center_y": .8}
                            size_hint_x: .5
                            
                        MDRectangleFlatIconButton:
                            text: "Não tem conta? Cadastre-se"
                            icon: "account-plus"
                            line_color: 0, 0, 0, 0
                            pos_hint: {"center_x": .5, "center_y": .5}
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
                            
                            
                           # ------------------------------------------------HISTORICOS------------------------------------------------------------------------
                           
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

                MDCard:
                    size_hint: None, None
                    size: "300dp", "350dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    BoxLayout:
                        orientation: 'vertical'
                        padding: '10dp'

                        MDLabel:
                            text: "Cadastre-se"
                            halign: "center"
                            pos_hint: {"center_x": .5, "center_y": .5}
                            size_hint_x: .5
                            

                        MDTextField:
                            id: email_user
                            hint_text: "e-mail"
                            multiline: True

                        MDTextField:
                            id: tel_user
                            hint_text: "Telefone"
                            multiline: True

                        MDTextField:
                            id: cpf_user
                            hint_text: "CPF"
                            multiline: True

                        MDTextField:
                            id: password_user
                            hint_text: "Digite a senha"
                            password: True
                            multiline: True

                        MDRaisedButton:
                            text: "Criar conta"
                            on_release: app.cadastrar_user()
                            pos_hint: {"center_x": .5, "center_y": .8}
                            size_hint_x: .5

                MDTopAppBar:
                    title: "Casdastrar"
                    elevation: 0
                    pos_hint: {"top": 1}
                    left_action_items: [["exit-to-app", lambda x: app.exit_app()]]

#  --------------------------------------------------------------CADASTRANDO TAREFAS -------------------------------------------------
            MDScreen:
                name: "scr 3"
                
                MDTopAppBar:
                    title: "Cadastrar Tarefas"
                    elevation: 0
                    pos_hint: {"top": 1}
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                MDLabel:
                    text: "Cadastrar Tarefas"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                    size_hint_x: .5

                MDTextField:
                    id: nome
                    hint_text: "Titulo"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .6}
                    size_hint_x: .5

                MDTextField:
                    id: descricao
                    hint_text: "Descrição"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint_x: .5

                MDBoxLayout:
                    adaptive_height: True
                    md_bg_color: app.theme_cls.primary_color

                MDTextField:
                    id: status
                    hint_text: "Status da tarefa"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .4}
                    size_hint_x: .5

                MDTextField:
                    id: data
                    hint_text: "Data de conclusão"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .3}
                    size_hint_x: .5

                MDRoundFlatIconButton:
                    id: cadastro_tarefa
                    on_press: app.cadastrar(nome.text, descricao.text, status.text, data.text)
                    text: "Cadastrar"
                    icon: "content-save-check"
                    icon_color: "white"
                    text_color: "white"
                    line_color: "white"
                    md_bg_color: "#428F58"
                    pos_hint: {"center_x": .7, "center_y": .1}
                    size_hint_x: .2

                MDRoundFlatIconButton:
                    text: "Voltar"
                    icon: "arrow-left"
                    icon_color: "white"
                    text_color: "white"
                    line_color: "white"
                    md_bg_color: "#2496F2"
                    pos_hint: {"center_x": .3, "center_y": .1}
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
            
        
    def cadastrar_user(self):
        email = self.root.ids.email_user.text
        senha = self.root.ids.password_user.text

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

            

    def nao_tem_conta_cadastre(self):
        self.root.ids.screen_manager.current = "scr 4"



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
