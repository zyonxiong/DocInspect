<script></script>

function geoFindMe() {
  
  const status = document.querySelector('#status');
  const mapLink = document.querySelector('#map-link');

  function success(position) {

    const latitude  = position.coords.latitude;
    const longitude = position.coords.longitude;

    $("#form").on("click", () => {

      $.ajax({
        url: `https://api.weatherapi.com/v1/current.json?key=WEATHER_KEY/q={latitude}{longitude}`,
        contentType: 'json',
        success: successFunction,
        method: "GET"
      })

      const form = {
        longitude: $("#longitude").val(),
        latitude: $("#latitude").val(),
  
      };

    });

    
    status.textContent = '';
    mapLink.href = `https://www.openstreetmap.org/#map=18/${latitude}/${longitude}`;
     mapLink.textContent = `Latitude: ${latitude} °, Longitude: ${longitude} °`;
  }

  function error() {
    status.textContent = 'Unable to retrieve your location';
  }

  navigator.geolocation.getCurrentPosition(success,error)

}

document.querySelector('#location').addEventListener('click', geoFindMe);