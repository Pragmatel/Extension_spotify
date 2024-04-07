from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_playlist', methods=['POST'])
def generate_playlist():
    bpm_min = request.form['bpm_min']
    bpm_max = request.form['bpm_max']
    # Appel aux fonctions pour rechercher les chansons et créer la playlist
    # Ajoutez ici l'appel aux fonctions définies précédemment
    return "Playlist générée avec succès!"

if __name__ == '__main__':
    app.run(debug=True)
