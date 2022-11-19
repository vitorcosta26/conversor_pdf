from flask import Flask, render_template, request, send_file
from docx2pdf import convert
import tempfile


app = Flask(__name__)
app.config['UPLOADS_DIR'] = tempfile.mkdtemp(prefix='uploads')
app.config['DOWNLOADS_DIR'] = tempfile.mkdtemp(prefix='downloads')

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == 'POST':
        arquivo_docx = request.files['docx']
        arquivo_docx.save(f'{app.config["UPLOADS_DIR"]}/{arquivo_docx.filename}')
        arquivo_pdf = convert(f'{app.config["UPLOADS_DIR"]}/{arquivo_docx.filename}', \
                              f'{app.config["DOWNLOADS_DIR"]}/{arquivo_docx.filename[0:-4]}pdf')

        return send_file(f'{app.config["DOWNLOADS_DIR"]}/{arquivo_docx.filename[0:-4]}pdf')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5500)