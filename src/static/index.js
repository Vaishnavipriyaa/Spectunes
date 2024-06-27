window.onload = function() {
			var navLinks = document.querySelectorAll('nav a');

			// Add event listeners to each navigation link
			navLinks.forEach(function(link) {
				link.addEventListener('mouseover', function() {
					this.style.color = 'red';
				});

				link.addEventListener('mouseout', function() {
					this.style.color = '';
				});
			});
		};



const form = document.querySelector('form');
const searchInput = document.querySelector('#search');
const durationInput = document.querySelector('#duration');
const explicitInput = document.querySelector('#explicit');
const resultsDiv = document.querySelector('#results');
const clearFilterButton = document.querySelector('#clear-filter');

clearFilterButton.addEventListener('click', () => {
  durationInput.value = '';
  explicitInput.value = 'any';
});

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const searchTerm = searchInput.value;
  const duration = durationInput.value;
  const explicit = explicitInput.value;
  const response = await fetch(`https://itunes.apple.com/search?term=${searchTerm}&entity=song`);
  const data = await response.json();
  resultsDiv.innerHTML = '';
  if (data.results.length === 0) {
    resultsDiv.textContent = 'No results found.';
  } else {
    let resultsCount = 0;
    data.results.forEach((result) => {
      if ((!duration || result.trackTimeMillis <= duration * 60 * 1000) && resultsCount < 10) {
        if (explicit === 'any' || (result.trackExplicitness === 'explicit' && explicit === 'explicit') || ((result.trackExplicitness === 'notExplicit' || result.trackExplicitness === 'cleaned') && explicit === 'cleaned')) {
          const resultDiv = document.createElement('div');
          resultDiv.classList.add('result');
          const trackName = document.createElement('h2');
          trackName.textContent = result.trackName;
          resultDiv.appendChild(trackName);
          const artistName = document.createElement('p');
          artistName.textContent = `Artist: ${result.artistName}`;
          resultDiv.appendChild(artistName);
          const albumPoster = document.createElement('img');
          albumPoster.src = result.artworkUrl100;
          resultDiv.appendChild(albumPoster);
          const audioElement = document.createElement('audio');
          audioElement.controls = true;
          const audioSource = document.createElement('source');
          audioSource.src = result.previewUrl;
          audioSource.type = 'audio/mpeg';
          audioElement.appendChild(audioSource);
          resultDiv.appendChild(audioElement);
          const durationBar = document.createElement('div');
          durationBar.classList.add('duration-bar');
          durationBar.style.width = `${(result.trackTimeMillis / (duration * 60 * 1000)) * 100}%`;
          resultDiv.appendChild(durationBar);
          resultsDiv.appendChild(resultDiv);
          resultsCount++;
        }
      }
    });

    if (resultsCount === 0) {
      resultsDiv.textContent = 'No results found.';
    }
  }
});



const text = "SEARCH PAGE!"; // Text to be typed out
let index = 0; // Index of the current character being typed out

function typeEffect() {
  document.querySelector("h1").textContent += text[index]; // Add the next character to the h1 tag
  index++; // Increment the index
  if (index === text.length) clearInterval(timer); // Stop the timer when all characters have been typed out
}

const timer = setInterval(typeEffect, 100); // Call the typeEffect function every 100 milliseconds

// Center the h1 element
const container = document.querySelector('.container');
container.style.textAlign = 'center';

var navLinks = document.querySelectorAll('nav a');
// Add event listeners to each navigation link



			

