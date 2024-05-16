function setCurrentSessionID(sessionID) {
    console.log("Setting current session ID...");
    sessionStorage.setItem('currentSessionID', sessionID); // Store sessionID in sessionStorage
}

function getCurrentSessionID() {
    var currentSessionID = sessionStorage.getItem('currentSessionID'); // Retrieve sessionID from sessionStorage
    return currentSessionID;
}

function getCurrentCountryName() {
    const url = '/get-country?sessionKey=' + getCurrentSessionID();

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(countryName => {
            //Set countryName element to the current country name
            document.getElementById('countryName').textContent = countryName;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

document.addEventListener('DOMContentLoaded', function () {
    // Get a reference to the button with the name "start"
    const startButton = document.querySelector('button[name="start"]');
    if (startButton) {
        // Set the data-formatted-time attribute for the button
        getCurrentStartTime()
            .then(baseTime => {
                startButton.setAttribute('data-formatted-time', baseTime);
                // Add event listener to handle click event for the button
                startButton.addEventListener('click', function () {
                    fetchCoordinates(baseTime, 0);
                });
            })
            .catch(error => {
                console.error('Error getting start time:', error);
            });
    }
});


// Function to handle the onchange event of the range input
function handleTimeSliderChange() {
    // Get the value of the range input
    const sliderValue = document.getElementById('timeSliderInput').value;
    // Call fetchCoordinates with the slider value
    fetchCoordinates('2023-09-17T13:00:00', sliderValue);
}

function getCurrentStartTime() {
    const url = '/get-startTime?sessionKey=' + getCurrentSessionID();
    return fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(startTime => {
            console.log(startTime);
            console.log(typeof startTime);
            return startTime;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            throw error; // Rethrow the error to propagate it further
        });
}