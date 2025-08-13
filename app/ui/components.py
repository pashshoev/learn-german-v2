from nicegui import ui

class Header:
    """Reusable header component with consistent styling."""
    
    @staticmethod
    def main(text: str):
        """Main app header with large, bold styling."""
        return ui.label(text).classes('text-3xl font-bold text-center mb-8 mx-auto')
    
    @staticmethod
    def sub(text: str):
        """Sub header with medium size and gray color."""
        return ui.label(text).classes('text-xl text-center text-gray-600 mb-8 mx-auto')
    
    @staticmethod
    def section(text: str):
        """Section header for content areas."""
        return ui.label(text).classes('text-2xl font-semibold mb-6 mx-auto')

class Button:
    """Reusable button component with consistent styling."""
    
    @staticmethod
    def primary(text: str, on_click=None, **kwargs):
        """Primary button with full width and consistent styling."""
        classes = 'w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded'
        return ui.button(text, on_click=on_click, **kwargs).classes(classes)
    
    @staticmethod
    def secondary(text: str, on_click=None, **kwargs):
        """Secondary button with outline style."""
        classes = 'w-full border border-gray-300 hover:bg-gray-50 text-gray-700 font-medium py-2 px-4 rounded'
        return ui.button(text, on_click=on_click, **kwargs).classes(classes)

class Card:
    """Reusable card component with consistent styling."""
    
    @staticmethod
    def container(**kwargs):
        """Standard card container."""
        return ui.card().classes('w-full max-w-md mx-auto shadow-md hover:shadow-lg transition-shadow')
    
    @staticmethod
    def title(text: str):
        """Card title with consistent styling."""
        return ui.label(text).classes('text-lg font-bold mb-2')
    
    @staticmethod
    def description(text: str):
        """Card description with consistent styling."""
        return ui.label(text).classes('text-gray-600 mb-4')

class Progress:
    """Reusable progress components."""
    
    @staticmethod
    def label(text: str):
        """Progress label with consistent styling."""
        return ui.label(text).classes('text-sm text-gray-500')
    
    @staticmethod
    def percentage(value: int):
        """Progress percentage with consistent styling."""
        return ui.label(f'{value}%').classes('text-sm font-medium ml-auto')
    
    @staticmethod
    def bar(value: int):
        """Progress bar with consistent styling."""
        return ui.linear_progress(value / 100).classes('w-full mb-4')
