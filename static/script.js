document.getElementById("analyzeBtn").addEventListener("click", analyzePage);

async function analyzePage() {

    const url = document.getElementById("urlInput").value;

    const button = document.getElementById("analyzeBtn");

    button.disabled = true;
    button.textContent = "Analyzing...";

    const response = await fetch("/analyze", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            url: url
        })

    });

    const data = await response.json();

    // Update Cards

    document.getElementById("status").textContent = data.status;

    document.getElementById("time").textContent = data.response_time;

    document.getElementById("h1").textContent = data.h1_count;

    document.getElementById("words").textContent = data.word_count;

    document.getElementById("title").textContent = data.title;

    document.getElementById("description").textContent = data.description;

    button.disabled = false;
    button.textContent = "Analyze";

}