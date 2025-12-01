import tracemalloc
from handlers import ApplicationController

def main():
    tracemalloc.start()
    
    app = ApplicationController()
    app.run()
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"Memoria actual: {current / 1024:.2f} KB")
    print(f"Memoria pico: {peak / 1024:.2f} KB")
    
if __name__ == "__main__":
    main()
