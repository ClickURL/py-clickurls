const locations = window.location.origin;

function Create() {
    let long_url = document.getElementById("Long_URL").value;
    let user_id = document.getElementById("input_user_id").value;
    CreateShortUrl(long_url, user_id);
}

async function CreateShortUrl(long_url, user_id) {
    try {
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
            const result = await response.json();
            location.href = locations + "/edit/" + result.secret_access_token;
        }
        else{
            let error = await response.json();
            throw error;
        }
    } catch (error) {
        handle_error(error);
    }
        
}

const submit_button = document.getElementById("input_user_id");
submit_button.addEventListener("keyup", (event) => {
    if (event.key === "Enter")
    {
        document.getElementById("submit_user_id").click();
    }
});

function handle_error(error) {
    let error_container = document.getElementById('error-container');
    error_container.style.visibility = 'visible';
    let error_message = document.createElement('div');
    error_message.setAttribute('id', 'error-message');
    error_message.innerText = `${error.detail}`;
    error_container.appendChild(error_message);
    error_container.addEventListener('click', function () {
        error_message.remove();
        error_container.style.visibility = 'hidden';
    })
}