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
        return results;
    };
    function get_views(rows_in){
        let results = [];
        rows_in.views_stats.forEach(function(row) {
        results.push(row.count_views)
        })
        return results;
    };
    const trace = {
        type: "scatter",
        mode: "lines",
        name: 'Stats',
        x: get_date(rows),
        y: get_views(rows),
        line: {color: '#17BECF'}
    }
    const data = [trace];
    const layout = {
        title: 'Stats',
        xaxis: {
            autorange: true,
            range: ['2023-03-01', '2032-03-31'],
            rangeselector: {buttons: [
                {
                    count: 1,
                    label: '1d',
                    step: 'day',
                    stepmode: 'backward'
                },
                {
                    count: 6,
                    label: '6d',
                    step: 'day',
                    stepmode: 'backward'
                },
                {
                    step: 'all'
                }
            ]},
            rangeslider: {range: ['2023-03-01', '2023-03-31']},
            type: 'date'
        },
        yaxis: {
            autorange: true,
            type: 'linear'
        }
    };

    Plotly.newPlot('stats', data, layout);
    })
}

let update_button = document.getElementById('UpdateStats');

update_button.addEventListener('click', function() {
    PlotStats();
});

EditUrl();
PlotStats();