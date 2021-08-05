let seatNumber = document.querySelector("#seat-number");


var intervalSeatId = window.setInterval(function() {

    fetch("/get-seat", {
      method: "POST",
      body: JSON.stringify({ "test": 1 }),
    })
    .then((resp) => resp.json())
    .then(function(data) {
      seatNumber.innerHTML = data.seat_number;
    });
    

}, 10000);