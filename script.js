async function analyzeMedia() {
    const fileInput = document.getElementById('mediaUpload');
    const btn = document.getElementById('analyzeBtn');
    const outputPanel = document.getElementById('outputPanel');
    const resultImage = document.getElementById('resultImage');
    const scriptText = document.getElementById('scriptText');

    if (fileInput.files.length === 0) {
        alert("Provide media input first.");
        return;
    }

    btn.innerText = "Processing Data...";
    btn.style.backgroundColor = "#d29922";

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        const response = await fetch("http://127.0.0.1:8000/analyze-media/", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (data.status === "success") {
            resultImage.src = "data:image/jpeg;base64," + data.image_base64;
            scriptText.innerText = data.audio_script;
            outputPanel.style.display = "block";

            if (data.audio_base64) {
                const audio = new Audio("data:audio/mp3;base64," + data.audio_base64);
                audio.play();
            } else {
                console.log("ElevenLabs bypassed. Engaging native browser voice.");
                const synth = window.speechSynthesis;
                const alertVoice = new SpeechSynthesisUtterance(data.audio_script);
                
                alertVoice.rate = 1.1; 
                alertVoice.pitch = 0.8; 
                
                synth.speak(alertVoice);
            }
        } else {
            alert("Analysis Failed.");
        }
    } catch (error) {
        alert("Connection to API lost.");
    } finally {
        btn.innerText = "Execute Analysis";
        btn.style.backgroundColor = "#238636";
    }
}