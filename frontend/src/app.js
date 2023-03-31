function Create() {
    let long_url = document.getElementById("Long_URL").value;
    let user_id = document.getElementById("User_Id").value;
    CreateShortUrl(long_url, user_id);
}

async function CreateShortUrl(long_url, user_id) {
    const response = await fetch(`/api/create_url/`, {
        method: 'POST',
        redirect: 'follow',
        headers: {"Accept": "application/json", "content-type": "application/json"},
        body: JSON.stringify({
            original_url: long_url,
            creator_id: user_id
        })
    });
    if (response.ok) {
        const link = await response.json();
        // localStorage.setItem('secret_access_token', link.secret_access_token)
        location.href = 'http://'+link.secret_access_token_full;
    }
    else {
        const error = await response.json();
        console.log(error.message);
    }
}