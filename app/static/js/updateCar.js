let currentInterval; // Declare outside to clear it properly
let isFetching = false; // To track if a fetch request is ongoing
let debounceTimeout; // To handle debouncing

function fetchCoordinates(baseTime, slideValue) {
    console.log(typeof baseTime);
    console.log(typeof '2023-09-17T13:00:00');
    console.log("baseTime: " + baseTime);
    if (isFetching) {
        clearTimeout(debounceTimeout);
        debounceTimeout = setTimeout(() => fetchCoordinates(baseTime, slideValue), 200);
        return;
    }

    isFetching = true;
    let startTime = new Date(baseTime.trim());
    console.log("start time 1: " + startTime);
    startTime.setSeconds(startTime.getSeconds() + parseInt(slideValue) * 10); // Adjusting time based on slider value
    console.log("start time 2: " + startTime);
    let formattedTime = formatDate(startTime);

    console.log("Current time: " + formattedTime);
    const url = '/get-coordinates?currentTime=' + formattedTime + '&currentSession=' + getCurrentSessionID();

    document.getElementById('time').innerHTML = formatDate(startTime);

    clearInterval(currentInterval); // Clear existing interval
    fetch(url)
        .then(response => response.json())
        .then(coordinates => {
            const testDriver = document.getElementById("testDriver");
            const raceTrack = document.getElementById("raceTrack");
            let coordinateIndex = 0;
            const scaleFactor = 24;
            const timeInterval = 100;
            let additionalSeconds = 0;
            currentInterval = setInterval(() => {
                if (coordinateIndex < coordinates.length) {
                    const x = coordinates[coordinateIndex][0] / scaleFactor;
                    const y = coordinates[coordinateIndex][1] / scaleFactor;
                    testDriver.style.left = `${(raceTrack.offsetWidth / 2 + x - testDriver.offsetWidth / 2) + 400}px`;
                    testDriver.style.bottom = `${(raceTrack.offsetHeight / 2 + y - testDriver.offsetHeight / 2) + 100}px`;

                    if (coordinateIndex % 4 === 0) {
                        additionalSeconds+=2;
                        let currentTime = new Date(startTime.getTime());
                        currentTime.setSeconds(currentTime.getSeconds() + additionalSeconds);
                        document.getElementById('time').innerHTML = formatDate(currentTime);
                    }

                    coordinateIndex++;
                } else {
                    clearInterval(currentInterval);
                    let slider = document.getElementById("timeSliderInput");
                    let newValue = parseInt(slider.value) + 1;
                    if (newValue <= slider.max) {
                        slider.value = newValue; // Update slider value
                        fetchCoordinates(baseTime, newValue); // Fetch next set of coordinates automatically if needed
                    }
                }
            }, timeInterval);
            isFetching = false;
        })
        .catch(error => {
            console.error('Error fetching coordinates:', error);
            clearInterval(currentInterval);
            isFetching = false;
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
