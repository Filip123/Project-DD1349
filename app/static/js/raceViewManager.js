function setCurrentSessionID(sessionID) {
    console.log("Setting current session ID...");
    sessionStorage.setItem('currentSessionID', sessionID); // Store sessionID in sessionStorage
}

function getCurrentSessionID() {
    var currentSessionID = sessionStorage.getItem('currentSessionID'); // Retrieve sessionID from sessionStorage
    return currentSessionID;
}
