from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp

languege = False

KVR = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Текст в речь"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Речь в текст"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
            OneLineListItem:
                text: "Настройки"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"


Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 20
        title: ""
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"

                MDLabel:
                    text: "Текст в речь:"
                    pos_hint: {"center_x": .57, "center_y": .945}

            Screen:
                name: "scr 2"

                MDLabel:
                    text: "Речь в текст:"
                    pos_hint: {"center_x": .57, "center_y": .945}
            Screen:
                name: "scr 3"

                MDLabel:
                    text: "Настройки:"
                    pos_hint: {"center_x": .57, "center_y": .945}
                MDLabel:
                    text: "Язык:"
                    pos_hint: {"center_x": .57, "center_y": .845}
                MDRaisedButton:
                    text: "Сохранить"
                    pos_hint: {"center_x": .87, "center_y": .1}
                    md_bg_color: 0, 0, 1, 1
                    on_release: app.restart()
                MDChooseChip:
                    pos_hint: {"center_x": .67, "center_y": .845}

                    MDChip:
                        text: 'Русский'
                        selected_chip_color: .21176470535294, .098039627451, 1, 1

                    MDChip:
                        text: 'Английский'
                        on_release: app.lang_eng(), app.build()
                        selected_chip_color: .21176470535294, .098039627451, 1, 1

    
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

'''
KVE = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Text to speech"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Speech to text"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
            OneLineListItem:
                text: "Settings"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"


Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 20
        title: ""
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"

                MDLabel:
                    text: "Текст в речь:"
                    pos_hint: {"center_x": .57, "center_y": .945}

            Screen:
                name: "scr 2"

                MDLabel:
                    text: "Речь в текст:"
                    pos_hint: {"center_x": .57, "center_y": .945}
            Screen:
                name: "scr 3"

                MDLabel:
                    text: "Настройки:"
                    pos_hint: {"center_x": .57, "center_y": .945}
                MDLabel:
                    text: "Язык:"
                    pos_hint: {"center_x": .57, "center_y": .845}
                MDRaisedButton:
                    text: "Сохранить"
                    pos_hint: {"center_x": .87, "center_y": .1}
                    md_bg_color: 0, 0, 1, 1
                MDChooseChip:
                    pos_hint: {"center_x": .67, "center_y": .845}

                    MDChip:
                        text: 'Русский'
                        selected_chip_color: .21176470535294, .098039627451, 1, 1

                    MDChip:
                        text: 'Английский'
                        selected_chip_color: .21176470535294, .098039627451, 1, 1

    
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TSA(MDApp):
    def lang_eng(self):
        global languege
        languege = True
    def lang_rus(self):
        global languege
        languege = True
    def restart(self):
        TSA().restart()
    def build(self):
        self.theme_cls.theme_style = "Dark"
        if languege==False:
            return Builder.load_string(KVR)
        if languege==True:
            return Builder.load_string(KVE)



TSA().run()
