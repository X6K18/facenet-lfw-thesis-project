from views.app_view import AppView
from controllers.app_controller import AppController

if __name__ == "__main__":
    view = AppView()
    controller = AppController(view)
    view.mainloop()