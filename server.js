const express = require('express');
const fs = require('fs');
const app = express();
const PORT = 3000;

// Route to get random song lyrics
app.get('/random-lyrics', (req, res) => {
  fs.readFile('lyrics.json', 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ error: 'Error reading the file' });
    }

    const jsonData = JSON.parse(data);
    const songs = jsonData.songs;

    // Get random song
    const randomSong = songs[Math.floor(Math.random() * songs.length)];

    res.json(randomSong);
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
