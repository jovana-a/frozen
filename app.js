function showSummary() {
    const customerName = document.getElementById('customerName').value;
    const sauce = document.getElementById('sauce').value;
    const toppings = Array.from(document.querySelectorAll('input[name="toppings"]:checked')).map(el => el.value);

    if (toppings.length > 3) {
        alert("Du kannst nur bis zu 3 Toppings auswählen.");
        return;
    }

    const summary = `
        <h2>Dein Frozen Joghurt</h2>
        <p><strong>Name:</strong> ${customerName}</p>
        <p><strong>Soße:</strong> ${sauce}</p>
        <p><strong>Toppings:</strong> ${toppings.join(', ')}</p>
    `;

    document.getElementById('summary').innerHTML = summary;
    document.getElementById('printButton').style.display = 'block';
    document.getElementById('previewButton').style.display = 'block';
}

function sendToPrint() {
    const url = generateUrlScheme();
    window.open(url, '_blank');
}

function previewLink() {
    const url = generateUrlScheme();
    document.getElementById('urlSchemeText').textContent = url;
    document.getElementById('urlScheme').style.display = 'block';
}

function generateUrlScheme() {
    const customerName = document.getElementById('customerName').value;
    const sauce = document.getElementById('sauce').value;
    const toppings = Array.from(document.querySelectorAll('input[name="toppings"]:checked')).map(el => el.value).join(',');

    return `brotherwebprint://print?filename=joghurt.lbx&50x70.bin&text_name=${encodeURIComponent(customerName)}&text_sauce=${encodeURIComponent(sauce)}&text_toppings=${encodeURIComponent(toppings)}`;
}

// Limit the selection of toppings to a maximum of 3
document.querySelectorAll('input[name="toppings"]').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const checkedToppings = document.querySelectorAll('input[name="toppings"]:checked');
        if (checkedToppings.length > 3) {
            this.checked = false;
            alert("Du kannst nur bis zu 3 Toppings auswählen.");
        }
    });
});
