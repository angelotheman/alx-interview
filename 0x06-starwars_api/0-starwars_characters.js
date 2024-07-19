#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
    console.log('Usage: node 0-starwars_characters.js <Movie ID>');
    process.exit(1);
}

// URL for the Star Wars API films endpoint
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error('Error fetching data:', error);
        process.exit(1);
    }

    if (response.statusCode !== 200) {
        console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
        process.exit(1);
    }

    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    // Fetch and display character names
    characters.forEach(charUrl => {
        request(charUrl, (error, response, body) => {
            if (error) {
                console.error('Error fetching character data:', error);
                return;
            }

            if (response.statusCode !== 200) {
                console.error(`Failed to fetch character data. Status code: ${response.statusCode}`);
                return;
            }

            const charData = JSON.parse(body);
            console.log(charData.name);
        });
    });
});
