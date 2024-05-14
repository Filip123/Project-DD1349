let currentInterval; // Declare outside to clear it properly

function fetchCoordinates(currentTime) {
    console.log("Current time: " + currentTime);
    const url = '/get-coordinates?currentTime=' + currentTime;
    let currentDateTime = new Date(currentTime); // Declare as local
    clearInterval(currentInterval); // Clear existing interval
    fetch(url)
        .then(response => response.json())
        .then(coordinates => {
            const test = document.getElementById("testDriver");
            raceTrackIndividualOffsetX = 100;
            raceTrackIndividualOffsetY = 0;

            let coordinateIndex = 0;
            const scaleFactor = 30;
            const timeInterval = 100;

            raceTrack = document.getElementById("raceTrack")

            const trackWidth = raceTrack.offsetWidth;
            const trackHeight = raceTrack.offsetHeight;

            currentInterval = setInterval(() => {
                if (coordinateIndex < coordinates.length) {
                    const x = coordinates[coordinateIndex][0] / scaleFactor;
                    const y = coordinates[coordinateIndex][1] / scaleFactor;

                    test.style.left = (raceTrackIndividualOffsetX + (trackWidth / 2 + x - test.offsetWidth / 2)) + 250 + 'px';
                    test.style.bottom = (raceTrackIndividualOffsetY + (trackHeight / 2 + y - test.offsetHeight / 2)) + 100 + 'px';


                    coordinateIndex++;

                } else {
                    clearInterval(currentInterval); // Stop the interval when coordinates are exhausted
                    currentDateTime.setSeconds(currentDateTime.getSeconds() + 10);
                    fetchCoordinates(formatDate(currentDateTime)); // Call recursively with new time
                }
            }, timeInterval);
        })
        .catch(error => {
            console.error('Error fetching coordinates:', error);
            clearInterval(currentInterval); // Clear on error
        });

}
function formatDate(date) {
    // Utility function to format date to string
    return date.getFullYear() + '-' +
        ('0' + (date.getMonth() + 1)).slice(-2) + '-' +
        ('0' + date.getDate()).slice(-2) + 'T' +
        ('0' + date.getHours()).slice(-2) + ':' +
        ('0' + date.getMinutes()).slice(-2) + ':' +
        ('0' + date.getSeconds()).slice(-2);
}