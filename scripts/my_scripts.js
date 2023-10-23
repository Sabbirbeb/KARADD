var urlParams;
(window.onpopstate = function () {
    var match,
        pl     = /\+/g,  // Regex for replacing addition symbol with a space
        search = /([^&=]+)=?([^&]*)/g,
        decode = function (s) { return decodeURIComponent(s.replace(pl, " ")); },
        query  = window.location.search.substring(1);

    urlParams = {};
    while (match = search.exec(query))
    urlParams[decode(match[1])] = decode(match[2]);
})();

function myFunction(q = 0) {
    //window.alert((q).toString())
    const a = urlParams['q']
    if (a) {
        document.getElementById("demo").innerHTML = a * a;
    }
    else {
        document.getElementById("demo").innerHTML = myFunction.name;
    }
}

function onlyLettersAndNumbers(str) {
    return /^[A-Za-z0-9]*$/.test(str);
}

function reset() {
    document.getElementById("demo").innerHTML = reset.name;
}

function get_from_input() {
    fname = document.getElementById('fname').value
    lname = document.getElementById('lname').value
    if (onlyLettersAndNumbers(fname)){
        fname = 'Input your fname. It must contain only RU letters!'
    }
    if (onlyLettersAndNumbers(lname)){
        lname = 'Input your lname. It must contain only RU letters!'
    }
    document.getElementById("fname_out").innerHTML = fname
    document.getElementById("lname_out").innerHTML = lname
}

function link_shorter_input(){
    inputUrl = document.getElementById('urlToShorten').value
    apiKey   = '/set_link?link=' + inputUrl
    if (inputUrl) {
        window.location.replace(apiKey);
    }
    else {
        alert ('Please enter URL for shortening!')
    }
}