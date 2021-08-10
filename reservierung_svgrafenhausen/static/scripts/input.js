let input = document.querySelector("#input-number");
let dec = document.querySelector("#decrement");
let inc = document.querySelector("#increment");

let ticketMain = document.querySelector("#main-tickets");

(function() {
 
  window.inputNumber = function(el) {
  
    var min = el.getAttribute("min") || false;
    var max = el.getAttribute("max") || false;

    dec.addEventListener('click', () => {
      var value = el.value;
      value--;
      if(!min || value >= min) {
        el.value = value;
        ticketMain.removeChild(ticketMain.lastChild);
      }
    });

    inc.addEventListener('click', () => {
      var value = el.value;
      value++;
      if(!max || value <= max) {
        el.value = value++;
        ticketMain.appendChild(getTicketElement());
      }
    });
  }
})();

inputNumber(input);


function getTicketElement() {
  let div = document.createElement('div');
  div.classList.add('ticket');

  let span1 = document.createElement('span');
  span1.innerHTML = "Ticket " + (ticketMain.childElementCount + 1);

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