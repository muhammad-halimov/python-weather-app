async function weather_js()
{
    var place = document.getElementById('city').value.toUpperCase();
    var result = await eel.get_weather(place)();

    document.getElementById('info').innerHTML = result;
}