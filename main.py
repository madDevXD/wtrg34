import flet as ft
from plyer import notification

def main(page: ft.Page):
    def show_notification():

        
        notification.notify(
            title='Flet App Notification',
            message='This is a test notification from your Flet app!',
            app_icon=None,  # e.g. 'path/to/icon.png'
            timeout=10,  # seconds
        )


    page.title = "Flet with Plyer Notification"
    
    btn = ft.ElevatedButton("Show Notification", on_click=lambda _: show_notification())
    page.add(btn)

ft.app(target=main)