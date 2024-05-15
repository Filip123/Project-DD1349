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

