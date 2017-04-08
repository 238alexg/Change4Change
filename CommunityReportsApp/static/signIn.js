function onSignIn(googleUser) {
    form = document.getElementById("loginForm");
    var id_token = googleUser.getAuthResponse().id_token;
    var id = document.createElement("id_token");
    id.setAttribute("value", id_token);
    form.appendChild(id);
    console.log(id);
    form.submit();
}

function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
    });
}
