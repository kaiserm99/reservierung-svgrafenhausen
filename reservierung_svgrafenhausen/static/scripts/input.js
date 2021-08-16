let input = document.querySelector("#input-number");
let dec = document.querySelector("#decrement");
let inc = document.querySelector("#increment");
let mainPrice = document.querySelector("#main-price");

let ticketMain = document.querySelector("#main-tickets");

const PRICE = 14;

(function() {
 
  window.inputNumber = function(el) {
  
    var min = el.getAttribute("min") || false;
    var max = el.getAttribute("max") || false;

    el.addEventListener('keypress', (e) => {
      
      if (e.keyCode < 48 || e.keyCode > 57) {
        e.returnValue = false;
        return;
      }
      
      var c = String.fromCharCode(e.which);
      var value = parseInt(el.value + c);

      if ( value > max) {
        el.value = max;
        e.returnValue = false;
        value = max;
      }

      if (value < ticketMain.childElementCount) {
        while (value != ticketMain.childElementCount) {
          ticketMain.removeChild(ticketMain.lastChild);
        }
      }

      if (value > ticketMain.childElementCount) {
        while (value != ticketMain.childElementCount) {
          ticketMain.appendChild(getTicketElement());
        }
      }

      mainPrice.innerHTML = ticketMain.childElementCount * 14;
    });

    el.addEventListener('keydown', (e) => {
      var value = el.value.substring(0, el.value.length - 1);

      if ((e.keyCode != 8 && e.keyCode != 46)) {
        return;
      }

      if (value == "") {
        value = 0;
      } else {
        value = parseInt(el.value.substring(0, el.value.length - 1));
      }
      

      while (value != ticketMain.childElementCount) {
        ticketMain.removeChild(ticketMain.lastChild);
      }
      
      mainPrice.innerHTML = ticketMain.childElementCount * 14;
    });

    dec.addEventListener('click', () => {
      var value = el.value;
      value--;
      if (!min || value >= min) {
        el.value = value;
        ticketMain.removeChild(ticketMain.lastChild);
      }

      mainPrice.innerHTML = ticketMain.childElementCount * 14;
    });

    inc.addEventListener('click', () => {
      var value = el.value;
      value++;
      if (!max || value <= max) {
        el.value = value++;
        ticketMain.appendChild(getTicketElement());
      }

      mainPrice.innerHTML = ticketMain.childElementCount * 14;
    });
  }
})();

inputNumber(input);


function getTicketElement() {
  let div = document.createElement('div');
  div.classList.add('ticket');

  let span1 = document.createElement('span');
  span1.innerHTML = "Ticket " + (ticketMain.childElementCount + 1) + " (14€)";

  div.appendChild(span1);

  let innerDiv = document.createElement('div');

  let span2 = document.createElement('span');
  span2.innerHTML = "&#128993;";

  let span3 = document.createElement('span');
  span3.innerHTML = " Nicht bestätigt";

  innerDiv.appendChild(span2);
  innerDiv.appendChild(span3);

  div.appendChild(innerDiv);

  return div;
}



function submitTicketCount() {
  fetch("/submit-tickets", {
    method: "POST",
    body: JSON.stringify({ "ticket-count": ticketMain.childElementCount }),
  })
  .then((resp) => window.location.href = "/reservierung");
}



// &#128994; --> Grün

// &#128308; --> Rot