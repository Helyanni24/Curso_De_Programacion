const contactForm = document.getElementById('contact-form');
const contactMessage = document.getElementById('contact-message');

// Reemplaza con tu clave pública
emailjs.init("TU_PUBLIC_KEY");

contactForm.addEventListener("submit", e => {
  e.preventDefault();

  emailjs.sendForm("TU_SERVICE_ID", "TU_TEMPLATE_ID", "#contact-form")
    .then(() => {
      contactMessage.textContent = "✅ Mensaje enviado con éxito.";
      contactForm.reset();
    })
    .catch(() => {
      contactMessage.textContent = "❌ Error al enviar el mensaje.";
    });
});
