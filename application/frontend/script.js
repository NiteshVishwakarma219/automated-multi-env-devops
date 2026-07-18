async function loadData(){

    const response = await fetch("http://127.0.0.1:9000/health");

    const data = await response.json();

    document.getElementById("environment").innerHTML = data.environment;

    document.getElementById("version").innerHTML = data.version;

    document.getElementById("status").innerHTML = data.status;

    document.getElementById("time").innerHTML = data.time;

}

loadData();