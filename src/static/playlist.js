let playlist = [];

function addToPlaylist(song_name, duration) {
  // check if the song already exists in the playlist
  const songIndex = playlist.findIndex(song => song.song_name === song_name && song.duration === duration);
  if (songIndex === -1) {
    // generate a unique id for the new song
    const id = Math.random().toString(36).substr(2, 9);
    // add the song to the playlist
    playlist.push({ id, song_name, duration });
    // save the updated playlist to local storage
    savePlaylist();
    // display the updated playlist on the page
    displayPlaylist();
  } else {
    alert('This song is already in the playlist!');
  }
}

function getPlaylist() {
  // get the playlist from local storage
  const storedPlaylist = localStorage.getItem('playlist');
  console.log(storedPlaylist); // add this line to check the value of storedPlaylist
  if (storedPlaylist) {
    // parse the stored playlist JSON string into an array
    playlist = JSON.parse(storedPlaylist);
  }
  // display the playlist on the page
  displayPlaylist();
}


function savePlaylist() {
  // save the current playlist to local storage
  localStorage.setItem('playlist', JSON.stringify(playlist));
}

function removeFromPlaylist(id) {
  // find the index of the song with the given id
  const songIndex = playlist.findIndex(song => song.id === id);
  if (songIndex !== -1) {
    // remove the song from the playlist
    playlist.splice(songIndex, 1);
    // save the updated playlist to local storage
    savePlaylist();
    // display the updated playlist on the page
    displayPlaylist();
  }
}

function displayPlaylist() {
  const playlistContainer = document.querySelector('#playlist');
  // clear the existing playlist display
  playlistContainer.innerHTML = '';
  // create a new playlist display
  playlist.forEach(song => {
    const songElement = document.createElement('div');
    songElement.innerHTML = `${song.title} - ${song.duration}`;
    // create a remove button for the song
    const removeButton = document.createElement('button');
    removeButton.innerHTML = 'Remove';
    removeButton.addEventListener('click', () => removeFromPlaylist(song.id));
    // add the remove button to the song element
    songElement.appendChild(removeButton);
    // add the song element to the playlist container
    playlistContainer.appendChild(songElement);
  });
}

// initialize the playlist display on page load
window.addEventListener('load', () => {
  getPlaylist();
});

