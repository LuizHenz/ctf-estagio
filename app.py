from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
        <head>
            <style>
                body {
                    background-color: black;
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    flex-direction: column;
                }
                img {
                    max-width: 80%;
                    height: auto;
                }
            </style>
        </head>
        <body>
            <img src="/static/luffy-chamas.gif" width="1000" alt="O mais bravo não é aquele que ganha mais batalhas, mas sim aquele que encara seus medos.">
            <p>Enquanto eu estiver vivo, terei chances infinitas!</p>
        </body>
    </html>
    '''
# @app.route('/zoro', methods=['GET'])
# def admin_block():
    # return "Método não permitido", 403

@app.route('/zoro', methods=['GET'])
def admin_flag():
    return '''
    <html>
        <head>
            <style>
                body {
                    background-color: black;
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    flex-direction: column;
                }
                img {
                    max-width: 80%;
                    height: auto;
                }
            </style>
        </head>
        <body>
            <img src="/static/zoro.gif" width="1000">
            <p>Quando o mundo é ruim com você, você tem que lidar com isso!</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)