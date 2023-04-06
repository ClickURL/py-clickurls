const secret_access_token = GetTokenFromHeader();
const locations = window.location.origin;

async function EditUrl() {
    // const token = localStorage.getItem('secret_access_token');
    const response = await fetch(`/api/edit/${secret_access_token}`, {
        method: 'GET',
        headers: {"Accept": "application/json"}
    });
    if (response.ok) {
        const result = await response.json();
        AddItem(locations + "/" + result.short_url);
        AddItem(locations + "/edit/" + result.secret_access_token);
    }
    else {
        const error = await response.json();
        console.log(error.message);
    }
}

function AddItem(item) {
    const div_url = document.createElement('div');
    div_url.setAttribute('id', 'table_row');
    const ref_url = document.createElement('a');
    ref_url.append(item);
    ref_url.setAttribute('href', item);
    div_url.append(ref_url);
    const copy_button = document.createElement('button');
    copy_button.append("Copy");
    copy_button.addEventListener("click" , () => {
        navigator.clipboard.writeText(item);
    });
    div_url.appendChild(copy_button);
    document.getElementById('table').append(div_url);
}

function GetTokenFromHeader() {
    const req = new XMLHttpRequest();
    req.open('GET', document.location, false);
    req.send(null);
    const headers = req.getResponseHeader("secret_access_token");
    return headers;
}

function PlotStats() {
    const request_stats = locations + "/api/v1/" + secret_access_token + "/stats.json";
    d3.json(request_stats, function(err, rows){
    function get_date(rows_in){
        let results = [];
        rows_in.views_stats.forEach(function(row) {
        results.push(row.day_views)
        })
        if (results.length == 0) {
            results = [new Date().toISOString().slice(0, 10)];
        }
        return results;
    };
    function get_views(rows_in){
        let results = [];
        rows_in.views_stats.forEach(function(row) {
        results.push(row.count_views)
        });
        if (results.length == 0) {
            results = [0];
        }
        return results;
    };
    const trace = {
        type: "scatter",
        mode: "lines+markers",
        name: 'Stats',
        x: get_date(rows),
        y: get_views(rows),
        fill: 'tozeroy',
        fillcolor: 'rgba(0, 0, 0, 0.15)',
        line: {
            shape: 'spline',
            width: 3,
            color: 'rgba(61, 215, 207, 1)'
        }
    }
    const data = [trace];
    const layout = {
        title: 'Stats',
        titlefont: {
            color: 'white'
        },
        xaxis: {
            type: 'date',
            autotick: false,
            showgrid: false,
            tickfont: {
                color: 'white'
            },
            linecolor: 'black',
            linewidth: 2,
        },
        yaxis: {
            type: 'linear',
            tickfont: {
                color: 'white'
            },
            linecolor: 'black',
            linewidth: 2,
            gridcolor: 'black',
            gridwidth: 1,
            showline: false,
        },
        paper_bgcolor: 'rgba(255, 255, 255, 0)',
        plot_bgcolor: 'rgba(255, 255, 255, 0)'
    };

    const config = {displaylogo: false, responsive: true};

    Plotly.newPlot('stats', data, layout, config);
    })
}

let update_button = document.getElementById('update_button');

update_button.addEventListener('click', function() {
    PlotStats();
});

EditUrl();
PlotStats();