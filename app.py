from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Kimsebaşgöz</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        html { scroll-behavior: smooth; }
        body {
            background-color: #111;
            color: #eee;
            font-family: Arial, sans-serif;
            margin: 0;
        }
        nav {
            background-color: #222;
            padding: 10px 20px;
            position: sticky;
            top: 0;
            z-index: 1000;
            text-align: center;
        }
        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 20px;
            font-weight: bold;
        }
        nav a:hover {
            color: #0af;
        }
        section {
            padding: 80px 20px;
            max-width: 800px;
            margin: auto;
        }
        h1, h2 {
            color: #0af;
        }
        img {
            width: 100%%;
            max-width: 400px;
            margin: 10px;
            border-radius: 10px;
        }
        a {
            color: #0af;
        }
    </style>
</head>
<body>

<nav>
    <a href="#hakkinda">Hakkımda</a>
    <a href="#iletisim">İletişim</a>
    <a href="#foto">Fotoğraflar</a>
</nav>

<section id="hakkinda">
    <h1>Hakkımda</h1>
    <p>Selamün aleyküm. Ben namıdiğer <strong>Kimsebaşgöz</strong>.</p>
    <p>İsmim <strong>Ahmet Utku Can</strong>'dır.</p>
    <p>Aşağıdaki bilgiler iletişim içindir. Her türlü sanal işlem için ulaşabilirsiniz.</p>
</section>

https://raw.githubusercontent.com/kbgyazilim46/kbgyazilimsite/main/logo.png

<section id="iletisim">
    <h2>İletişim</h2>
    <p><strong>WhatsApp:</strong> <a href="https://wa.me/639092363984" target="_blank">+63 909 236 3984</a></p>
    <p><strong>Instagram:</strong> <a href="https://instagram.com/_kimsebasgoz_" target="_blank">@_kimsebasgoz_</a></p>
    <p><strong>E-posta:</strong> <a href="mailto:kimsebasgozedemez@mail.com">kimsebasgozedemez@mail.com</a></p>
</section>

<section id="foto">
    <h2>Güvence Fotoğrafları</h2>
    <img src="https://raw.githubusercontent.com/kbgyazilim46/kbgyazilimsite/main/g1.png" alt="Güvence 1">
    <img src="https://raw.githubusercontent.com/kbgyazilim46/kbgyazilimsite/main/g2.png" alt="Güvence 2">
    <img src="https://raw.githubusercontent.com/kbgyazilim46/kbgyazilimsite/main/g3.jpg" alt="Güvence 3">
</section>

</body>
</html>
"""

@app.route('/')
def site():
    return HTML_PAGE

if __name__ == '__main__':
    app.run(debug=True)