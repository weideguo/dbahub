from flask import Flask, send_from_directory

@app.route('/')
def index():
    """前端页面"""
    return send_from_directory('.', 'index.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
    