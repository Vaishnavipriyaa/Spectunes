# from flask import Flask, request, jsonify, render_template

# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.db' # Replace mydb.db with the name of your database
# db = SQLAlchemy(app)

# class Song(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     artist = db.Column(db.String(50), nullable=False)
#     album = db.Column(db.String(50), nullable=False)
#     playlist = db.relationship('PlaylistSong', backref='song', lazy=True)

# class PlaylistSong(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)
#     song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)

# class Playlist(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     songs = db.relationship('PlaylistSong', backref='playlist', lazy=True)

# @app.route('/add_to_playlist', methods=['POST'])
# def add_to_playlist():
#     song_id = request.form.get('song_id')
#     playlist_id = 1  # Replace with the appropriate playlist ID
#     playlist_song = PlaylistSong.query.filter_by(song_id=song_id, playlist_id=playlist_id).first()

#     if not playlist_song:
#         playlist_song = PlaylistSong(song_id=song_id, playlist_id=playlist_id)
#         db.session.add(playlist_song)
#         db.session.commit()
#         return jsonify({'message': 'Song added to playlist successfully.'})
#     else:
#         return jsonify({'message': 'Song already in playlist.'})
        
# @app.route('/playlist')
# def playlist():
#     playlist_songs = PlaylistSong.query.all()
#     return render_template('playlist.html', playlist_songs=playlist_songs)

# @app.route('/delete_from_playlist', methods=['POST'])
# def delete_from_playlist():
#     song_id = request.form.get('song_id')
#     playlist_id = 1  # Replace with the appropriate playlist ID
#     playlist_song = PlaylistSong.query.filter_by(song_id=song_id, playlist_id=playlist_id).first()

#     if playlist_song:
#         db.session.delete(playlist_song)
#         db.session.commit()
#         return jsonify({'message': 'Song removed from playlist successfully.'})
#     else:
#         return jsonify({'message': 'Song not found in playlist.'})

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/artists.html')
def artists():
    return render_template('artists.html')

# @app.route('/playlist.html')
# def playlist():
#     return render_template('playlist.html')

@app.route('/search.html')
def search():
    return render_template('search.html')


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/spotlight.html')
def spotlight():
    return render_template('spotlight.html')


@app.route('/artist01-albums.html')
def artist01albums():
    return render_template('artist01-albums.html')

@app.route('/artist02-albums.html')
def artist02albums():
    return render_template('artist02-albums.html')

@app.route('/artist03-albums.html')
def artist03albums():
    return render_template('artist03-albums.html')

@app.route('/artist04-albums.html')
def artist04albums():
    return render_template('artist04-albums.html')

@app.route('/artist05-albums.html')
def artist05albums():
    return render_template('artist05-albums.html')

@app.route('/artist06-albums.html')
def artist06albums():
    return render_template('artist06-albums.html')


@app.route('/album01-songs.html')
def album01songs():
    return render_template('album01-songs.html')

@app.route('/album02-songs.html')
def album02songs():
    return render_template('album02-songs.html')

@app.route('/album03-songs.html')
def album03songs():
    return render_template('album03-songs.html')

@app.route('/album04-songs.html')
def album04songs():
    return render_template('album04-songs.html')

@app.route('/album05-songs.html')
def album05songs():
    return render_template('album05-songs.html')

@app.route('/album06-songs.html')
def album06songs():
    return render_template('album06-songs.html')

@app.route('/album07-songs.html')
def album07songs():
    return render_template('album07-songs.html')

@app.route('/album08-songs.html')
def album08songs():
    return render_template('album08-songs.html')

@app.route('/album09-songs.html')
def album09songs():
    return render_template('album09-songs.html')

@app.route('/album10-songs.html')
def album10songs():
    return render_template('album10-songs.html')

@app.route('/album11-songs.html')
def album11songs():
    return render_template('album11-songs.html')

@app.route('/album12-songs.html')
def album12songs():
    return render_template('album12-songs.html')

@app.route('/album13-songs.html')
def album13songs():
    return render_template('album13-songs.html')

@app.route('/album14-songs.html')
def album14songs():
    return render_template('album14-songs.html')

@app.route('/album15-songs.html')
def album15songs():
    return render_template('album15-songs.html')

@app.route('/album16-songs.html')
def album16songs():
    return render_template('album16-songs.html')


@app.route('/album17-songs.html')
def album17songs():
    return render_template('album17-songs.html')

@app.route('/album18-songs.html')
def album18songs():
    return render_template('album18-songs.html')

@app.route('/album19-songs.html')
def album19songs():
    return render_template('album19-songs.html')

@app.route('/album20-songs.html')
def album20songs():
    return render_template('album20-songs.html')

@app.route('/album21-songs.html')
def album21songs():
    return render_template('album21-songs.html')

@app.route('/album22-songs.html')
def album22songs():
    return render_template('album22-songs.html')

@app.route('/album23-songs.html')
def album23songs():
    return render_template('album23-songs.html')

@app.route('/album24-songs.html')
def album24songs():
    return render_template('album24-songs.html')

@app.route('/album25-songs.html')
def album25songs():
    return render_template('album25-songs.html')

@app.route('/album26-songs.html')
def album26songs():
    return render_template('album26-songs.html')

@app.route('/album27-songs.html')
def album27songs():
    return render_template('album27-songs.html')

@app.route('/album28-songs.html')
def album28songs():
    return render_template('album28-songs.html')

@app.route('/album29-songs.html')
def album29songs():
    return render_template('album29-songs.html')

@app.route('/album30-songs.html')
def album30songs():
    return render_template('album30-songs.html')




db = sqlite3.connect('playlist.db', check_same_thread=False)
db.execute('CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, duration TEXT)')

@app.route('/add_to_playlist', methods=['POST'])
def add_to_playlist():
    title = request.form['song_title']
    duration = request.form['duration']
    
    # Check if song already exists in the database
    existing_song = db.execute('SELECT * FROM songs WHERE title = ?', (title,)).fetchone()
    if existing_song:
        return 'Song already exists in the playlist'
    
    # Insert song into the database
    db.execute('INSERT INTO songs (title, duration) VALUES (?, ?)', (title, duration))
    db.commit()
    return 'Success'

@app.route('/playlist.html')
def playlist():
    songs = db.execute('SELECT * FROM songs').fetchall()
    return render_template('playlist.html', songs=songs)

@app.route('/remove_song', methods=['POST','DELETE'])
def remove_song():
    song_title = request.form['song_title']
    duration = request.form['duration']
    
    # Delete song from the playlist in the database
    db.execute('DELETE FROM songs WHERE title = ? AND duration = ?', (song_title, duration)).fetchone()
    db.commit()
    
    # Update playlist page by deleting song
    songs = db.execute('SELECT * FROM songs').fetchall()
    return render_template('playlist.html', songs=songs)





if __name__ == '__main__':
    app.run()

