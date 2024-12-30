import importlib

def load_page(module_name):
    """Carga dinámicamente un módulo y ejecuta su lógica."""
    module = importlib.import_module(module_name)
    if hasattr(module, "run"):
        module.run()
    else:
        raise AttributeError(f"El módulo '{module_name}' no tiene una función 'run'.")
