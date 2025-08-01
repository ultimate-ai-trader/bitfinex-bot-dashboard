
async function loadBalance() {
  try {
    const res = await fetch("/api/balance");
    const data = await res.json();
    document.getElementById("balance").textContent = "LTC: " + data.ltc + " | USD: $" + data.usd;
  } catch (e) {
    document.getElementById("balance").textContent = "Error loading balance.";
  }
}
loadBalance();

function startBot() {
  fetch("/api/start", { method: "POST" });
}
function stopBot() {
  fetch("/api/stop", { method: "POST" });
}
