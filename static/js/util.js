function copyText(text) {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard
      .writeText(text)
      .then(function () {
        alert("Copied " + text);
      })
      .catch(function (err) {
        console.error("Could not copy text: ", err);
      });
  } else {
    // Fallback method
    let textarea = document.createElement("textarea");
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    try {
      document.execCommand("copy");
      alert("Copied " + text);
    } catch (err) {
      console.error("Fallback: Oops, unable to copy", err);
    }
    document.body.removeChild(textarea);
  }
}

function get_sharecode() {
  fetch("{{ url_for('generate_sharecode') }}")
    .then((response) => response.text())
    .then((text) => copyText(text));
}


function redirect(url) {
  window.location.href = url
}