const form = document.getElementById('predict-form');
const submitBtn = document.getElementById('submit-btn');
const statusBox = document.getElementById('status');
const cooldownMs = 2000; // short cooldown between submits
let coolingDown = false;

const setStatus = (message, type = 'info') => {
  statusBox.className = `alert alert-${type} mt-3`;
  statusBox.textContent = message;
  statusBox.classList.remove('d-none');
};

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  if (coolingDown) {
    return;
  }

  const message = document.getElementById('message').value.trim();
  if (!message) {
    setStatus('Please enter some text before submitting.', 'warning');
    return;
  }

  coolingDown = true;
  submitBtn.disabled = true;
  setStatus('Submitting...', 'info');

  try {
    const response = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error(`Server responded with ${response.status}`);
    }

    const result = await response.json();
    setStatus(`Prediction: ${result?.label ?? 'unknown'}`, 'success');
  } catch (err) {
    setStatus('There was a problem submitting your request. Please try again.', 'danger');
    console.error(err);
  } finally {
    setTimeout(() => {
      coolingDown = false;
      submitBtn.disabled = false;
    }, cooldownMs);
  }
});
