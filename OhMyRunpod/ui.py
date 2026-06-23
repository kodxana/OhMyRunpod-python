from rich.console import Console
from rich.text import Text
from OhMyRunpod.utils.menu import BaseMenu


class InteractiveMenu:
    def __init__(self):
        self.console = Console()
        self.options = [
            ("SSH Setup", "Configure SSH server and create connection scripts"),
            ("Pod Information", "Display Runpod environment information"),
            ("File Transfer", "Setup file transfer with croc or SFTP"),
            ("ComfyUI", "Install and manage ComfyUI"),
            ("Exit", "Exit the application"),
        ]

    def run(self) -> int:
        menu = BaseMenu(
            title="OhMyRunpod",
            subtitle="Runpod Environment Management Tool",
            options=self.options,
            breadcrumbs=["Home"],
            help_lines=[
                "SSH Setup: Enables SSH, generates a password, and creates helper scripts.",
                "Pod Information: Shows RAM, IP, GPU count, CUDA info, and more.",
                "File Transfer: Use Croc or SFTP to send/receive files easily.",
                "ComfyUI: Manage templates, custom nodes, models, and manager GUI.",
                "Tip: Numbers + Enter works in all terminals.",
            ],
        )
        idx = menu.run()
        # Credits
        try:
            self.console.print(Text("\nCreated by Madiator2011", style="dim italic"))
        except Exception:
            pass
        return idx
