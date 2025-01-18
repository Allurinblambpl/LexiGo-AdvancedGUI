import os

class SystemUtils:
    @staticmethod
    def clear_screen():
        """Czyści ekran"""
        os.system('cls' if os.name == 'nt' else 'clear')
