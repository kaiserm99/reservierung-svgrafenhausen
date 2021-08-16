
function confirmTicket(id) {
  fetch("/confirm-ticket", {
    method: "POST",
    body: JSON.stringify({ "ticket-id": id }),
  })
  .then((resp) => document.location.reload(true));
}


function deleteTicket(id) {
  fetch("/delete-ticket", {
    method: "POST",
    body: JSON.stringify({ "ticket-id": id }),
  })
  .then((resp) => document.location.reload(true));
}

function undoTicket(id) {
  fetch("/undo-ticket", {
    method: "POST",
    body: JSON.stringify({ "ticket-id": id }),
  })
  .then((resp) => document.location.reload(true));
}

function sendEmail(user_id) {
  fetch("/send-email", {
    method: "POST",
    body: JSON.stringify({ "user-id": user_id }),
  })
  .then((resp) => window.location.href = "/admin");
}