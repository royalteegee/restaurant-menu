document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        var flashMessages = document.querySelectorAll('.messages .alert');
        flashMessages.forEach(function(flashMessage) {
            flashMessage.style.display = 'none';
        });
    }, 1000); // 5000 milliseconds = 5 seconds
});
