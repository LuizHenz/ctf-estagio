from flask import Flask, request, render_template_string
import base64
app = Flask(__name__)

@app.route('/')
def index():
    return r'''
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
        </head>
        <body>
            <pre class="glitch">          
  _   _  ____     _____  ____  _____   _____    _   _  ____    _  _______ _   _  _____  _____     ____  _   _ _  __     __  ______ _               _____  _____ 
 | \ | |/ __ \   / ____|/ __ \|  __ \ / ____|  | \ | |/ __ \  | |/ /_   _| \ | |/ ____|/ ____|   / __ \| \ | | | \ \   / / |  ____| |        /\   / ____|/ ____|
 |  \| | |  | | | |  __| |  | | |  | | (___    |  \| | |  | | | ' /  | | |  \| | |  __| (___    | |  | |  \| | |  \ \_/ /  | |__  | |       /  \ | |  __| (___  
 | . ` | |  | | | | |_ | |  | | |  | |\___ \   | . ` | |  | | |  <   | | | . ` | | |_ |\___ \   | |  | | . ` | |   \   /   |  __| | |      / /\ \| | |_ |\___ \ 
 | |\  | |__| | | |__| | |__| | |__| |____) |  | |\  | |__| | | . \ _| |_| |\  | |__| |____) |  | |__| | |\  | |____| |    | |    | |____ / ____ \ |__| |____) |
 |_| \_|\____/   \_____|\____/|_____/|_____( ) |_| \_|\____/  |_|\_\_____|_| \_|\_____|_____( )  \____/|_| \_|______|_|    |_|    |______/_/    \_\_____|_____/ 
                                           |/                                               |/                                                                  
                                                                                                                                                                
            </pre>
            <img src="/static/luffy-chamas.gif" width="1000" alt="O mais bravo não é aquele que ganha mais batalhas, mas sim aquele que encara seus medos.">
            <p class="glitch">Enquanto eu estiver vivo, terei chances infinitas!</p>
        </body>
    </html>
    '''

@app.route('/zoro', methods=['GET'])
def roronoa():
    return '''
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
        </head>
        <body>
            <img src="/static/zoro.gif" width="600">
            <p class="glitch">Quando o <a href="estrelas" class="no-underline">mundo</a> é ruim com você, você tem que lidar com isso!</p>
        </body>
    </html>
    '''

@app.route('/estrelas', methods=['GET'])
def estrelas():
    return '''
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
        </head>
        <body style="background-color:black; color:white; text-align:center;">
            <img src="/static/geocentrismo.jpg" width="900">
            <p class="glitch">Mortal como sou, sei que nasci por um dia, mas quando sigo a multidão cerrada de estrelas em seu curso circular, meus pés não tocam mais a terra.
             Subo até o próprio Zeus para me banquetear com ambrosia, a comida dos deuses.</p>
             <!-- O que os olhos veem, o coração sente… mas a mente precisa decifrar: Os deuses escondem segredos onde os mortais menos procuram. -->
        </body>
    </html>
    '''
@app.route('/4lm4g3st0', methods=['GET'])
def almagesto_block():
    return '''
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
        </head>
        <body style="background-color:black; color:white; text-align:center;">
            <h1 class="glitch">Só porque está na sua frente, não quer dizer que você encontrou.</h1><br>
            <img src="/static/naogrita.jpeg" width="500">
            <p class="glitch">EU SI DIVIRTO HAHAHAHAHA</p>
            <script src="/static/typing.js"></script>
        </body>
    <html>    
    '''

@app.route('/4lm4g3st0', methods=['POST'])
def final():
    auth_cookie = request.cookies.get('auth')
    if auth_cookie == 'super-estagiarios':
        return '''
        <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
        </head>
            <body style="background-color:black; color:white; text-align:center;">
                <h1 class="glitch>Parabéns</h1>
                <p class="glitch>Flag: CTF{CEAPE-ESTAGIARIOS}</p>
            </body>
        </html>
        '''
    else:
        hint = base64.b64encode(b'auth=super-estagiarios').decode()
        return f'''
        <html>
            <head>
                <link rel="stylesheet" type="text/css" href="/static/style.css">
            </head>
            <body style="background-color:black; color:white; text-align:center;">
                <!--Até mesmo as constelações têm segredos. Vai encarar ou vai desistir?... {hint}-->
            </body>
    </html>
        ''', 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)