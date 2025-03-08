
// Images selon le sentiment
document.addEventListener("DOMContentLoaded", function () {
    const resultElement = document.getElementById("sentiment-result");
    const imageElement = document.getElementById("sentiment-image");

    if (resultElement) {
        const resultText = resultElement.textContent.trim();

        let imagePath = "";
        if (resultText.includes("Positif")) {
            imagePath = "/static/positif.png";
        } else if (resultText.includes("Neutre")) {
            imagePath = "/static/neutre.png";
        } else if (resultText.includes("Négatif")) {
            imagePath = "/static/negatif.png";
        }

        if (imagePath) {
            imageElement.src = imagePath;
            imageElement.style.display = "block";
        }
    }

    // Onglets de sentiment
    const tabs = document.querySelectorAll(".nav-link");
    tabs.forEach(tab => {
        tab.addEventListener("click", function () {
            tabs.forEach(t => t.classList.remove("active"));
            this.classList.add("active");
        });
    });
});
