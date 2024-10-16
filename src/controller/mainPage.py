from src import app

@app.route('/')
def root():
    return "Hello World"