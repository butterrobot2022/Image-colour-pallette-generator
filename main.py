from colorthief import ColorThief
from flask import Flask, render_template, request


color_names = []

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    global color_names
    img_url = 'https://th.bing.com/th/id/OIP.kAbBMskLTtjt6z4tZaSZzwHaE8?pid=ImgDet&rs=1'
    if request.method == 'POST':
        ct = ColorThief(f"/Users/motin/Downloads/{request.form.get('file')}")
        palette = ct.get_palette(color_count=11)
        color_names = []
        n = 1

        img_url = f"/Users/motin/Downloads/{request.form.get('file')}"
        for color in palette:
            color_names.append(f"{n}: #{color[0]:02x}{color[1]:02x}{color[2]:02x}")
            n += 1
        return render_template("home.html", palette=color_names, img_url=img_url)
    return render_template("home.html", palette=color_names, source=f"/Users/motin/Downloads/{request.form.get('file')}", img_url=img_url)


if __name__ == '__main__':
    app.run(debug=True)

