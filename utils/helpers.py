import importlib

def load_page(module_name):
    """Carga dinámicamente un módulo y ejecuta su lógica."""
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "run"):
            module.run()  # Ejecuta la función 'run' del módulo cargado
        else:
            raise AttributeError(f"El módulo '{module_name}' no tiene una función 'run'.")
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(f"No se pudo encontrar el módulo: {module_name}") from e
