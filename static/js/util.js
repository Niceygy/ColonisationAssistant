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

/**
 * Gets the sharecode from the server, and copies it
 */
function get_sharecode(values, id) {
  fetch("/sharecode", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ values: values, id: id, window: window.location.origin }),
  })
    .then((response) => response.text())
    .then((text) => {
      // const shareUrl = `${window.location.origin}/userdata/get?id=${text}`;
      copyText(text);
      alert("Please open the share url yourself, so if you press save again it updates the same sharecode (not makes a new one)")
    });
}


function redirect(url) {
  window.location.href = url
}