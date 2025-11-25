const tabs = document.querySelectorAll('.nav-tab');
const panels = document.querySelectorAll('.tab-panel');
const converterForm = document.getElementById('converter-form');
const result = document.getElementById('conversion-result');

function setActiveTab(targetId) {
  tabs.forEach((tab) => tab.classList.toggle('active', tab.dataset.target === targetId));
  panels.forEach((panel) => {
    panel.hidden = panel.id !== targetId;
  });
  window.location.hash = targetId;
}

tabs.forEach((tab) => {
  tab.addEventListener('click', (event) => {
    event.preventDefault();
    setActiveTab(tab.dataset.target);
  });
});

const initial = window.location.hash?.replace('#', '') || 'overview';
setActiveTab(initial);

if (converterForm) {
  converterForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const amount = event.target.amount.value;
    const from = event.target.from.value;
    const to = event.target.to.value;

    result.textContent = 'Converting...';
    try {
      const response = await fetch(
        `https://api.exchangerate.host/convert?from=${encodeURIComponent(from)}&to=${encodeURIComponent(to)}&amount=${encodeURIComponent(amount)}`
      );
      const data = await response.json();
      if (!response.ok || !data.result) {
        throw new Error('Unable to fetch rate');
      }
      result.textContent = `${amount} ${from} ≈ ${data.result.toFixed(4)} ${to}`;
    } catch (error) {
      console.error(error);
      result.textContent = 'Could not convert right now. Please try again shortly.';
    }
  });
}

const googlePlaceholder = 'YOUR_GOOGLE_CLIENT_ID';
const googleIdContainer = document.getElementById('g_id_onload');
if (googleIdContainer && googleIdContainer.dataset.client_id === googlePlaceholder) {
  const notice = document.createElement('p');
  notice.className = 'notice';
  notice.textContent = 'Replace YOUR_GOOGLE_CLIENT_ID with your Google OAuth client ID to enable one-tap sign-up.';
  googleIdContainer.insertAdjacentElement('afterend', notice);
}
