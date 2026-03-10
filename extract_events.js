const fs = require('fs');

// Mock siteData to avoid importing everything if possible, or just require the file
// But data.js is probably a browser script (const siteData = ...)
// So we can just read it as text and extract the JSON.

const dataText = fs.readFileSync('data.js', 'utf8');
const start = dataText.indexOf('events: [');
const end = dataText.indexOf('],', start) + 1;
const eventsString = dataText.substring(start + 'events: '.length, end);

// Cleanup the string to be valid JSON (it might have trailing commas or use unquoted keys)
// Instead of complex cleanup, let's just eval it in a safe-ish way since it's our own data.
try {
    const events = eval(eventsString);
    fs.writeFileSync('events_seed.json', JSON.stringify(events, null, 2));
    console.log('Successfully extracted events to events_seed.json');
} catch (e) {
    console.error('Failed to parse events:', e);
}
