async function EditUrl() {
    // const token = localStorage.getItem('secret_access_token');
    const secret_access_token = GetTokenFromHeader();
    const response = await fetch(`/api/edit/${secret_access_token}`, {
        method: 'GET',
        headers: {"Accept": "application/json"}
    });
    if (response.ok) {
        const result = await response.json();
        const location = window.location.origin
        const row_short_url = document.createElement('div');
        const row_token_url = document.createElement('div');
        row_short_url.append(location + "/" + result.short_url);
        row_token_url.append(location + "/edit/" + result.secret_access_token);
        document.getElementById('table').append(row_short_url);
        document.getElementById('table').append(row_token_url);
    }
    else {
        const error = await response.json();
        console.log(error.message);
    }
}

function GetTokenFromHeader() {
    const req = new XMLHttpRequest();
    req.open('GET', document.location, false);
    req.send(null);
    const headers = req.getResponseHeader("secret_access_token");
    return headers;
}
EditUrl();
