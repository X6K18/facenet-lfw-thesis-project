from views.pages.home_page import HomePage


class AppController:
    def __init__(self, view):
        self.view = view
        self.view.set_controller(self)
        self.view.bind_events()

        # load mặc định
        self.show_home()

    def show_home(self):
        self.view.main_view.show_frame(HomePage)

