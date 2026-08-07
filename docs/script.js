const button = document.getElementById("button");
const message = document.getElementById("message");

button.addEventListener("click", () => {
    message.textContent = "Thanks for clicking! 🎉";
});