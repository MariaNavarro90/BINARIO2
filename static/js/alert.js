document.addEventListener('DOMContentLoaded', function() {
    if (typeof messages !== 'undefined' && messages.length > 0) {
        messages.forEach(function(message) {
            Swal.fire({
                icon: 'success',
                title: '¡Éxito!',
                text: message,
            });
        });
    }
});