function successFunction(data)
    {
      $('#weather').val(data.current.condition.text)
      // console.log(data.current.condition.text);

    }
    
    $("#location").on("click", (evt) => {
      evt.preventDefault()

    navigator.geolocation.getCurrentPosition(geolocator,error)

    });

function geolocator(position) {

    const latitude  = position.coords.latitude;
    const longitude = position.coords.longitude;

      $.ajax({
        url: `https://api.weatherapi.com/v1/current.json?key=WEATHER_KEY&q=${latitude},${longitude}`,
        contentType: 'json',
        success: successFunction,
        method: "GET"
      })
    };
    

  function error() {
    status.textContent = 'Unable to retrieve your location';
  }