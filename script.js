function convertToExcel() {
    const pdfInput = document.getElementById('pdfInput');
    const file = pdfInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('pdfFile', file);

        fetch('/convert', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Conversion successful! Download link: ' + data.downloadLink);
            } else {
                alert('Conversion failed. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again later.');
        });
    } else {
        alert('Please select a PDF file.');
    }
}
