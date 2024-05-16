
document.addEventListener('DOMContentLoaded', (event) => {
    getCurrentStartTime()
        .then(baseTime => {
            fetchCoordinatesForRaceTrack(baseTime)
        })
        .catch(error => {
            console.error('Error getting start time:', error);
        });
});

