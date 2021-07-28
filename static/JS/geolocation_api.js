function successFunction(data)
    {
      $('#weather-temperature').val(data.current.temp_f)
      $('#weather-condition').val(data.current.condition.text)
      //$('#date').val(data.location.localtime)
      $('#longitude').val(data.location.lon)
      $('#latitude').val(data.location.lat)

    }
    
    $("#location").on("click", (evt) => {
      evt.preventDefault()

      navigator.geolocation.getCurrentPosition(geolocator,error)

    });

function geolocator(position) {

    const latitude  = position.coords.latitude;
    const longitude = position.coords.longitude;

      $.ajax({
        url: `/geoapi/?latitude=${latitude}&longitude=${longitude}`,
        contentType: 'json',
        success: successFunction,
        method: "GET"
      })
    };
    

  function error() {
    status.textContent = 'Unable to retrieve your location';
  }