from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Используем render_template_string для простоты
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Текущая дата и время</title>
    </head>
    <body>
        <h1>Текущая дата и время</h1>
        <p>{{ time }}</p>
    </body>
    </html>
    """
    return render_template_string(html, time=current_time)

if __name__ == '__main__':
    app.run(debug=True)