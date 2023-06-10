import eel

eel.init('web')

@eel.expose
def get_weather(place):
    from pyowm import OWM
    owm = OWM('527138375508c55a18a2f50a849441aa')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    status = w.detailed_status
    winds = w.wind()['speed']

    return f"В городе {place.upper()} сейчас {round(temp)} градусов, скорость ветра {winds} м/c."

eel.start('main.htm', size = (640, 700))