from flask import Flask, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def current_time():
    now = datetime.utcnow() + timedelta(hours=3)
    bg_color = request.args.get('bgcolor', '#ffffff')
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Текущее время</title>
        <style>
            body {{
                background-color: {bg_color};
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-size: 2rem;
            }}
        </style>
    </head>
    <body>
        <div>Текущее время: {now.strftime('%H:%M:%S')}</div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)