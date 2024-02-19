// logout.js

window.addEventListener("beforeunload", function (event) {
    // Tarayıcı kapatıldığında logout işlemini gerçekleştirmek için AJAX isteği gönder
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/logout/", false);  // Logout URL'sini doğru şekilde ayarlayın
    xhr.send();
});
