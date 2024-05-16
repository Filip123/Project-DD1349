function fetchCoordinatesForRaceTrack(startTime) {
    console.log("For race track Current time: " + startTime);
    const url = '/get-racetrack-coordinates?raceStart=' + startTime;

    fetch(url)
        .then(response => response.json())
        .then(coordinates => {
            const raceTrack = document.getElementById("raceTrack");
            raceTrackIndividualOffsetX = 100;
            raceTrackIndividualOffsetY = 0;

            const scaleFactor = 24;

            coordinates.forEach((coordinate) => {
                const x = coordinate[0] / scaleFactor;
                const y = coordinate[1] / scaleFactor;

                const newDiv = document.createElement('div');
                newDiv.className = 'coordinateDiv';
                newDiv.style.left = `${(raceTrack.offsetWidth / 2 + x - testDriver.offsetWidth / 2) + 400}px`;
                newDiv.style.bottom = `${(raceTrack.offsetHeight / 2 + y - testDriver.offsetHeight / 2) + 100}px`;

                raceTrack.appendChild(newDiv);
            });
        })
        .catch(error => {
            console.error('Error fetching coordinates:', error);
        });
}
