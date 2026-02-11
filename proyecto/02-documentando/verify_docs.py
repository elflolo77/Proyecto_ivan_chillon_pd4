
import importlib
import inspect
import sys
import os

# Add project root to path so imports work
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, 'cine_multiplex')
sys.path.append(current_dir) # Add 02-documentando
sys.path.append(os.path.join(current_dir, '..', '..')) # Add project root if needed for absolute imports

# Adjust imports to match file structure
# Assuming structure:
# 02-documentando/
#   cine_multiplex/
#     domain/
#     application/
#     infrastructure/
#     presentation/

try:
    from cine_multiplex.domain import pelicula, sala, sesion, entrada, repositorio
    from cine_multiplex.application import servicio_cine
    from cine_multiplex.infrastructure import repositorio_memoria, datos_iniciales
    from cine_multiplex.presentation import menu
except ImportError as e:
    print(f"Error importing modules: {e}")
    # Try adding parent directory to path
    sys.path.append(os.path.dirname(current_dir))
    try:
        from cine_multiplex.domain import pelicula, sala, sesion, entrada, repositorio
        from cine_multiplex.application import servicio_cine
        from cine_multiplex.infrastructure import repositorio_memoria, datos_iniciales
        from cine_multiplex.presentation import menu
    except ImportError as e:
        print(f"Critical import error: {e}")
        sys.exit(1)

modules_to_check = [
    pelicula, sala, sesion, entrada, repositorio,
    servicio_cine, repositorio_memoria, menu, datos_iniciales
]

def check_docstrings(module, module_name):
    print(f"\nChecking module: {module_name}")
    if not module.__doc__:
        print(f"  [MISSING] Module docstring for {module_name}")
    else:
        print(f"  [OK] Module docstring present.")

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and obj.__module__ == module.__name__:
            print(f"  Checking class: {name}")
            if not obj.__doc__:
                print(f"    [MISSING] Class docstring for {name}")
            else:
                print(f"    [OK] Class docstring present.")
            
            # Check methods
            for method_name, method in inspect.getmembers(obj):
                if inspect.isfunction(method) or inspect.ismethod(method):
                     # Skip inherited methods strictly from object if not overridden, 
                     # but here we care about our code.
                     if method.__module__ == module.__name__:
                        if not method.__doc__:
                            # Init is special, check class docstring usually covers, but we added to init specifically
                            print(f"      [MISSING] Method docstring for {method_name}")
                        else:
                            print(f"      [OK] Method docstring for {method_name}")

if __name__ == "__main__":
    print("Starting Docstring Verification...")
    for mod in modules_to_check:
        check_docstrings(mod, mod.__name__)
    print("\nVerification Complete.")
