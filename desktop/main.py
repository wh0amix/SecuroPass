# ==================== main.py ====================
import os
import sys
import customtkinter as ctk
from views.login_view import LoginView
from utils.theme import Theme

class SecuroPassApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("SecuroPass - Gestionnaire de mots de passe")
        self.root.geometry("1200x700")
        self.root.minsize(800, 600)
        
        # Configuration du thème
        Theme.setup()
        
        # Icône de l'application (chemin absolu vers desktop/assets/logo.ico)
        if sys.platform.startswith('win'):
            # __file__ pointe vers .../SecuroPass/desktop/main.py
            base_dir = os.path.dirname(os.path.abspath(__file__))
            icon_path = os.path.join(base_dir, 'assets', 'logo.ico')
            
            if not os.path.exists(icon_path):
                raise FileNotFoundError(
                    f"Fichier d'icône introuvable : {icon_path}"
                )
            self.root.iconbitmap(icon_path)
        
        # Centrer la fenêtre
        self.center_window()
        
        # Démarrer avec la vue de connexion
        self.current_view = LoginView(self.root, self)
        
    def center_window(self):
        self.root.update_idletasks()
        width  = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth()  // 2) - (width  // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def switch_view(self, view_class, **kwargs):
        """Changer de vue"""
        if self.current_view:
            self.current_view.destroy()
        self.current_view = view_class(self.root, self, **kwargs)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SecuroPassApp()
    app.run()
