function onSignIn(googleUser) {
    var id_token = googleUser.getAuthResponse().id_token;
    var token = document.createElement("id_token");
    id.setAttribute("value", id_token);
    console.log(token);
    document.getElementById("loginForm").submit();
}

function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
    });
}
