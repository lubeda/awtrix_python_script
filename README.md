# **Sorry, i can't support this anymore** because i don't use awtrix anymore!

Take a look at [](https://github.com/lubeda/EsphoMaTrix) or host the awtrix server in a docker container.-



# HowTo
## German

Awtrix-Server installieren z.B. als hass.io [add-on](https://github.com/lubeda/repository) oder [normal](https://awtrix.github.io/AWTRIX2.0-Docs_Beta/#/de-de/host)

Den awtrix-server mit dem selben MQTT-Server wie deinen Home-Assistant verbinden. [Doku](https://awtrix.github.io/AWTRIX2.0-Docs_Beta/#/de-de/settings?id=mqtt)

Im Home-Assistant `python_script:` aktivieren [Doku](https://www.home-assistant.io/integrations/python_script/)

Skripte als `awtrix_notify.py` in das Verz. /config/python_scripts ablegen

Aufgerufen werden kann das Skript dann über Automatisierungen, z.B.:

```
- id: 'a157427619503te0'
  alias: AWTRIX Aussentemp
  description: Bei jeder neuen Messung Aussentemp. auf Matrix anzeigen
  trigger:
  - entity_id: sensor.temperature
    platform: state
  action:
  - data_template:
      text: '{{ states("sensor.temperature")}} C'
      name: "temperature"
      icon: 233
      lifetime: 10
    service: python_script.awtrix_notify
```

Unter Datatemplate können alle Parameter von Awtrix die für "customapp" gültig sind verwendet werden. [Doku für notify](https://awtrix.github.io/AWTRIX2.0-Docs_Beta/#/de-de/api?id=benachrichtigungen)

### Zwei Awtrixe
Die zweite Awtrix muss unter einem anderen Topic angebunden werden. Die erste sollte unter "awtrix" stehen, die zweite unter einem anderen topic, z.B. "awtrix2"

```
- id: 'a157427619503te0'
  alias: AWTRIX Aussentemp
  description: Bei jeder neuen Messung Aussentemp. auf Matrix anzeigen
  trigger:
  - entity_id: sensor.temperature
    platform: state
  action:
  - data_template:
      text: 'Zweite Awtrix {{ states("sensor.temperature")}} C'
      name: "temperature"
      icon: 233
      lifetime: 10
      topix: awtrix2
    service: python_script.awtrix_notify
  - data_template:
      text: 'Erste Awtrix {{ states("sensor.temperature")}} C'
      name: "temperature"
      icon: 233
      lifetime: 10
    service: python_script.awtrix_notify
```
