import flet
from flet import (ElevatedButton, 
                  FilePicker, 
                  FilePickerResultEvent, 
                  FilledButton, 
                  Row, 
                  TextField, 
                  ProgressBar, 
                  SnackBar, 
                  Text, 
                  icons)

from pytube import YouTube


def main(page):

    page.title = "AmorosoTube"
    
    # Open directory dialog
    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelled!"
        directory_path.update()

    def download(code):
        yt = YouTube("https://youtu.be/" + code)        
        yd = yt.streams.get_highest_resolution()
        print(directory_path.value)
        yd.download(directory_path.value)

    def button_download(e):
        page.splash = ProgressBar()
        button.disabled = True
        page.update()
        
        try:
            download(text.value)
            page.snack_bar = SnackBar(Text("Download realizado com sucesso!"))
            text.value = ''
        except:
            page.snack_bar = SnackBar(Text("Nao foi possível baixar video"))
            
        page.snack_bar.open = True
        page.splash = None
        button.disabled = False
        page.update() 
        
        
    text = TextField(label="Digite o código:", width=300)
    button = FilledButton(text="Download", on_click=button_download)
    
    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()
    
    # hide all dialogs in overlay
    page.overlay.extend([get_directory_dialog])

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(
        Row( controls = [ 
                ElevatedButton(
                    "Selecione diretório:",
                    icon=icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
                directory_path
            ],
            alignment="center",
        ),
        Row(
            controls = [    
                text, button  
            ],
            alignment="center",
        ),
    )

flet.app(target=main)