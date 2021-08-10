
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