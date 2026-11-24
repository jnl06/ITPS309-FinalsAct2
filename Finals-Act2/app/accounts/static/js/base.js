// Show / Hide password
document.querySelectorAll(".toggle-pw").forEach((btn) => {
  btn.addEventListener("click", () => {
    const input = document.getElementById(btn.dataset.target);
    const show = input.type === "password";
    input.type = show ? "text" : "password";
    btn.textContent = show ? "Hide" : "Show";
  });
});

// Password strength meter (signup only)
const pw = document.getElementById("id_password1");
const meter = document.getElementById("strength");
const label = document.getElementById("strength-label");

if (pw && meter) {
  const names = ["", "Weak", "Medium", "Strong"];

  pw.addEventListener("input", () => {
    const v = pw.value;
    let score = 0;
    if (v.length >= 8) score++;
    if (/[A-Z]/.test(v) && /[a-z]/.test(v)) score++;
    if (/\d/.test(v) && /[^A-Za-z0-9]/.test(v)) score++;
    if (!v) score = 0;
    meter.dataset.level = score;
    label.textContent = names[score];
  });
}