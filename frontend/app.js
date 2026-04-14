async function uploadResume() {
  const fileInput = document.getElementById("resumeFile");
  const file = fileInput.files[0];

  if (!file) {
    alert("Please upload a file");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("https://YOUR_API_GATEWAY_URL/analyze", {
    method: "POST",
    body: formData
  });

  const data = await response.json();
  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
}
