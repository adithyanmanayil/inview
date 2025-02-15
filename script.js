document.addEventListener("DOMContentLoaded", function() {
    const dropArea = document.getElementById("dropArea");
    const fileInput = document.getElementById("fileInput");
    const fileNameDisplay = document.getElementById("fileName");
    const browseBtn = document.getElementById("browseBtn");

    // Open file dialog when clicking "Browse"
    browseBtn.addEventListener("click", () => fileInput.click());

    // Handle file selection
    fileInput.addEventListener("change", function(event) {
        handleFiles(event.target.files);
    });

    // Drag over effect
    dropArea.addEventListener("dragover", function(event) {
        event.preventDefault();
        dropArea.classList.add("drag-over");
    });

    // Drag leave effect
    dropArea.addEventListener("dragleave", function() {
        dropArea.classList.remove("drag-over");
    });

    // Handle file drop
    dropArea.addEventListener("drop", function(event) {
        event.preventDefault();
        dropArea.classList.remove("drag-over");
        handleFiles(event.dataTransfer.files);
    });

    // Function to handle selected files
    function handleFiles(files) {
        if (files.length > 0) {
            fileNameDisplay.textContent = "Selected File: " + files[0].name;
        }
    }
});
