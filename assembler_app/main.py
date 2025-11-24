import tracemalloc
from handlers import ApplicationController

def main():
    tracemalloc.start()
    app = ApplicationController()
    app.run()
    print(tracemalloc.get_traced_memory())
    
if __name__ == "__main__":
    main()
