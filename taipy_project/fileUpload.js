function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const selectedFile = fileInput.files[0];

    if (selectedFile) {
        const formData = new FormData();
        formData.append("file", selectedFile);

        fetch("/upload", {
            method: "POST",
            body: formData
        })
            .then(response => response.text())
            .then(data => {
                console.log("Server response:", data);
            })
            .catch(error => {
                console.error("Error:", error);
            });
    }
}
