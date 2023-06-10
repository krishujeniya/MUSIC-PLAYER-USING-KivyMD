from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.list import OneLineListItem
from pygame import mixer
import os


Window.size = (300, 500)


class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class cdll:

    def __init__(self):
        self.first = None

    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node

    def insert_at_end(self, new_node):
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.first.prev, new_node)

    def display(self):
        if self.first is None:
            return
        current = self.first
        print("Doubly Linked List:")
        while True:
            print("<---{}--->".format(current.data), end=' ')
            current = current.next
            if current == self.first:
                break


class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )
        self.LL = cdll()
        mixer.init()

    def build(self):
        self.title = "AI Music Player"
        self.theme_cls.primary_palette = "Lime"
        self.theme_cls.theme_style = "Dark"

        return Builder.load_file("GUI.kv")

    def file_manager_open(self):
        # output manager to the screen
        self.file_manager.show(os.path.expanduser("~"))
        self.manager_open = True

    def select_path(self, path: str):
        self.exit_manager()
        self.path = path
        if self.path:
            os.chdir(self.path)
            # return list of files
            songs = os.listdir(self.path)
            for song in songs:
                # check which .mp3 file
                if song.endswith(".mp3"):
                    self.s = Node(song)
                    # insert .mp3 file in Linked list
                    self.LL.insert_at_end(self.s)
                    # insert .mp3 file for listbox
                    self.root.ids.SongList.add_widget(
                        OneLineListItem(text=song, size_hint_y=None, height=(50)))
            # first node of linked list
            self.s = self.LL.first
            self.root.ids.songname.title = self.s.data
            self.LL.display()

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def Play_Music(self):
        mixer.music.load(self.s.data)
        mixer.music.play()
        self.root.ids.songname.right_action_items = [["skip-previous", lambda x: self.playpri(
        )], ["pause", lambda x: self.pause()], ["skip-next", lambda x: self.playnext()]]

    def resume(self):
        mixer.music.unpause()
        self.root.ids.songname.right_action_items = [["skip-previous", lambda x: self.playpri(
        )], ["pause", lambda x: self.pause()], ["skip-next", lambda x: self.playnext()]]

    def pause(self):
        mixer.music.pause()
        self.root.ids.songname.right_action_items = [["skip-previous", lambda x: self.playpri(
        )], ["play", lambda x: self.resume()], ["skip-next", lambda x: self.playnext()]]

    def playnext(self):
        self.s = self.s.next
        mixer.music.load(self.s.data)
        mixer.music.play()
        self.root.ids.songname.title = self.s.data
        self.root.ids.songname.right_action_items = [["skip-previous", lambda x: self.playpri(
        )], ["pause", lambda x: self.pause()], ["skip-next", lambda x: self.playnext()]]

    def playpri(self):
        self.s = self.s.prev
        mixer.music.load(self.s.data)
        mixer.music.play()
        self.root.ids.songname.title = self.s.data
        self.root.ids.songname.right_action_items = [["skip-previous", lambda x: self.playpri(
        )], ["pause", lambda x: self.pause()], ["skip-next", lambda x: self.playnext()]]


if __name__ == "__main__":
    app = Example()
    app.run()
