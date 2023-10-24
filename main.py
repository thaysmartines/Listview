from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
import pyrebase
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivy.factory import Factory

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.properties import BooleanProperty
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivy.uix.checkbox import CheckBox


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

<ContentNavigationDrawer>:

    MDList:

        OneLineListItem:
            text: "Login"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"

        OneLineListItem:
            text: "Tarefas"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"

        OneLineListItem:
            text: "Lista de tarefas"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 3"

MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        title: "Listview"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

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
                                                        
                            
            MDScreen:
                name: "scr 2"

                GridLayout:
                    cols: 1

                    MDTopAppBar:
                        title: "Tarefas"
                        elevation: 10
                        pos_hint: {"top": 1}

                    ScrollView:
                        MDList:
                            id: tarefas_list

                MDRaisedButton:
                    text: "Listar Tarefas"
                    on_release: app.listar_tarefas()
                    pos_hint: {"center_x": .5, "center_y": .1}


                        

            MDScreen:
                name: "scr 3"

                MDLabel:
                    text: "Cadastrar Tarefas"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                    size_hint_x: .5

                MDTextField:
                    id: nome
                    hint_text: "Nome da tarefa"
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
                    hint_text: "Data da tarefa"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .3}
                    size_hint_x: .5

                MDRoundFlatIconButton:
                    id: cadastro_tarefa
                    on_press: app.cadastrar(nome.text, descricao.text, status.text, data.text)
                    text: "Cadastrar"
                    icon: "account-plus"
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
    
class TarefaListItem(TwoLineAvatarIconListItem):
    checkbox = ObjectProperty()

    def __init__(self, text, secondary_text, checkbox_active=False, **kwargs):
        super(TarefaListItem, self).__init__(text=text, secondary_text=secondary_text, **kwargs)
        self.checkbox = CheckBox(active=checkbox_active)
        self.add_widget(self.checkbox)


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

    def listar_tarefas(self):
        tarefas_list = self.root.ids.tarefas_list
        tarefas_list.clear_widgets()

        tarefas = db.child("tarefas").get()
        if tarefas.each():
            for tarefa in tarefas.each():
                tarefa_nome = tarefa.val()['nome']
                tarefa_descricao = tarefa.val()['descricao']

                tarefa_label = TarefaListItem(
                    text=f"Nome: {tarefa_nome}",
                    secondary_text=f"Descrição: {tarefa_descricao}"
                )
                tarefas_list.add_widget(tarefa_label)

    def show_error_dialog(self):
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.button import MDRaisedButton
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


Example().run()
