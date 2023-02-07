# Importação de módulos
import os
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
import validators


class App:
    # Declaração de constantes
    JANELA_NOME      = 'Pylhado'
    JANELA_TAMANHO   = '500x300'
    COR_LARANJA      = '#F38722'
    COR_CINZA_ESCURO = '#303030'


    def __init__(self):
        self.criar_Janela()
        self.criar_Menu()
        self.criarFrames()

        self.janela.mainloop()


    def criar_Janela(self):
        self.janela = tkinter.Tk()

        x = self.janela.winfo_screenwidth() // 2 - 500 // 2
        y = self.janela.winfo_screenheight() // 2 - 300 // 2
        # Configurações da janela
        self.janela.title(App.JANELA_NOME)
        self.janela.resizable(False, False)
        self.janela.geometry('{}+{}+{}'.format(App.JANELA_TAMANHO, x, y))
        self.janela.configure(background=App.COR_CINZA_ESCURO)
        self.janela.iconphoto(False, tkinter.PhotoImage(file=os.path.join(os.path.dirname(__file__), "pasta.png")))


    def criar_Menu(self):
        self.menu_principal = tkinter.Menu(self.janela)

        # App
        self.menu_app = tkinter.Menu(self.menu_principal, tearoff=0, background='#FFF')
        self.menu_app.add_command(label='Preferências')
        self.menu_app.add_separator()
        self.menu_app.add_command(label='Sobre Pylhado', accelerator='F1')
        self.menu_app.add_command(label='Ajuda & Suporte')
        self.menu_app.add_command(label='Verificar Atualizações...')
        self.menu_app.add_separator()
        self.menu_app.add_command(label='Fechar', command=self.janela.destroy)

        # Ferramentas
        self.menu_editar = tkinter.Menu(self.menu_principal, tearoff=0, background='#FFF')
        self.menu_editar.add_radiobutton(label='Baixar', accelerator='Ctrl+1')
        self.menu_editar.add_radiobutton(label='Converter', accelerator='Ctrl+2')
        self.menu_editar.add_separator()
        self.menu_editar.add_command(label='Abrir YouTube no navegador')

        # Menu Principal
        self.menu_principal.add_cascade(label='Aplicativo', menu=self.menu_app)
        self.menu_principal.add_cascade(label='Ferramentas', menu=self.menu_editar)

        self.janela.config(menu=self.menu_principal)


    def criarFrames(self):
        self.tipoDownload  = tkinter.StringVar()
        self.tipoDownload.set('a')
        self.urlVideo = tkinter.StringVar()
        self.frame_baixar  = tkinter.Frame(self.janela, background='#303030').place(x=0, y=240, width=500, height=40)
        self.lbl_titulo    = tkinter.Label(self.frame_baixar, text='BAIXAR VIDEOS DO YOUTUBE', foreground='#399DD5', background='#303030', font='Roboto 11 bold').place(x=75, y=35)
        self.ent_urlVideo  = EntryWithPlaceholder(self.frame_baixar, textvariable=self.urlVideo).place(x=75, y=60, width=350, height=30)
        self.lbl_limpar    = btn_limpar(self.frame_baixar, text='LIMPAR', foreground='#606060', background='#303030', font='Roboto 11 bold').place(x=360, y=90)
        self.lbl_titulo    = tkinter.Label(self.frame_baixar, text='TIPO DE MIDIA', foreground='#399DD5', background='#303030', font='Roboto 11 bold').place(x=75, y=110)
        self.rad_tipoAudio = pylhado_Radiobutton(self.frame_baixar, variable=self.tipoDownload, value='a', text='Áudio').place(x=75, y=130)
        self.rad_tipoVideo = pylhado_Radiobutton(self.frame_baixar, variable=self.tipoDownload, value='v', text='Vídeo', background='#303030', foreground='#909090', font='Roboto 10', selectcolor='#404040', activebackground='#303030', activeforeground='#FFFFFF').place(x=140, y=130)
        self.btn_baixar    = HoverButton(self.frame_baixar, text='VALIDAR URL', background='#399DD5', relief='solid',  command=self.validarUrl).place(x=170, y=175, width=170, height=30)

        # Frame Footer
        self.rodape = tkinter.Frame(self.janela, background='#fff').place(x=0, y=240, width=500, height=40)
        image = Image.open(os.path.join(os.path.dirname(__file__), "Logo.png"))
        resize_image = image.resize((60, 25))
        img = ImageTk.PhotoImage(resize_image)
        self.img_ma = tkinter.Label(self.rodape, image=img, background='#FFFFFF')
        self.lbl_observacoes = tkinter.StringVar()
        self.lbl_statusDownload = tkinter.Label(self.rodape, textvariable=self.lbl_observacoes, background='#FFFFFF').place(x=10, y=250)
        self.img_ma.image = img
        self.img_ma.place(x=420, y=246)


    def validarUrl(self):
        self.lbl_observacoes.set("Validando link do YouTube...")
        
        if self.urlVideo.get().strip() == '' or self.urlVideo.get().strip() == 'Url do Vídeo':
            self.lbl_observacoes.set("Cole o link do vídeo que deseja baixar no campo acima.")
            return

        if validators.url(self.urlVideo.get().strip()): 
            self.lbl_observacoes.set("Valido")
            print(self.tipoDownload)
            self.janela_baixar = tkinter.Tk()
            self.janela_baixar.title('Baixar')




            self.janela_baixar.mainloop()
            
            

            

        else:
            self.lbl_observacoes.set("Url não é valido")

          

class btn_limpar(tkinter.Label):
    def __init__(self, pai, **kw):
        tkinter.Label.__init__(self, master=pai, **kw)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self['foreground'] = '#D0D0D0'

    def on_leave(self, event):
        self['foreground'] = '#606060'
            

class pylhado_Radiobutton(tkinter.Radiobutton):
    def __init__(self, pai, **kw):
        tkinter.Radiobutton.__init__(self, master=pai, **kw)
        self['background']='#303030'
        self['foreground']='#909090'
        self['font']='Roboto 10'
        self['selectcolor']='#404040'
        self['activebackground']='#303030'
        self['activeforeground']='#FFFFFF'


class HoverButton(tkinter.Button):
    def __init__(self, pai, **kw):
        tkinter.Button.__init__(self,master=pai,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self['activebackground'] = '#399DD5'
        self['activeforeground'] = '#FFFFFF'
        self['font']='Roboto 11 bold'
        self['relief']='solid'
        self['border']=0,
        self['foreground']='#FFF'
    def on_enter(self, event):
        self['background'] = '#40B1F0'

    def on_leave(self, event):
        self['background'] = '#399DD5'


class pylhado_Combobox(ttk.Combobox):

    def __init__(self, pai, **kw):
        ttk.Combobox.__init__(self, pai, **kw)
        style= ttk.Style()
        style.theme_use('clam')
        style.configure('TCombobox', background='#606060', fieldbackground='#0f0', lightcolor='#303030', darkcolor='#303030', selectbackground='#303030')
        self['values'] = ['Áudio', 'Vídeo']
     

# Componentes
class pylhado_Frame(tkinter.Frame): 
    def __init__(self, pai, **kw):
        tkinter.Frame.__init__(self, master=pai, **kw)

        # Configurações do Frame
        self['background'] = App.COR_CINZA_ESCURO


class EntryWithPlaceholder(tkinter.Entry):
    def __init__(self, pai, **kw):
        tkinter.Entry.__init__(self, master=pai, **kw)

        self['border'] = 0
        self['relief'] = 'solid' 
        self['font'] = 'Roboto 10'
        self['background'] = '#404040'
        self['insertbackground'] = '#FFF'
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)
        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, 'Url do Vídeo')
        self['fg'] = '#909090'

    def foc_in(self, *args):
        if self['fg'] == '#909090':
            self.delete('0', 'end')
            self['fg'] = '#D0D0D0'

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


class pylhado_Button(tkinter.Button): 
    def __init__(self, pai, **kw):
        tkinter.Button.__init__(self, master=pai, **kw)

        # Configurações do Button
    
    def on_hover(self, event):
        self['background'] = self['activebackground']

    def on_leave(self, event):
        self['background'] = self.defaultBackground


class pylhado_Entry(tkinter.Entry):    
    def __init__(self, pai, **kw):
        tkinter.Entry.__init__(self, master=pai, **kw)

        # Configurações do Entry
        self['background'] = App.COR_CINZA_ESCURO


class pylhado_Label(tkinter.Label): 
    def __init__(self, pai, **kw):
        tkinter.Label.__init__(self, master=pai, **kw)

        # Configurações da Label
        self['foreground'] = App.COR_LARANJA
        self['background'] = App.COR_CINZA_ESCURO


class pylhado_ProgessBar(ttk.Progressbar): 
    def __init__(self):
        pass


class pylhado_Button_Notebook(ttk.Notebook): 
    def __init__(self):
        pass
