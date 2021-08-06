let seatNumber = document.querySelector("#seat-number");
let switchRegister = document.querySelector("#switch-register");
let switchLogin = document.querySelector("#switch-login");
let formLogin = document.querySelector("#form-login")


// Function which updates the number of free seats, if the user needs to long to insert the data and something has changed
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

// If pressed => display login page
switchRegister.addEventListener('click', () => {
  formLogin.classList.add("active");
});

// If pressed => display register page
switchLogin.addEventListener('click', () => {
  formLogin.classList.remove("active");
});