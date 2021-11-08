work= data.copy()

if work.get("topic","") == "" :
   work["topic"]="awtrix"

hass.services.call('mqtt', 'publish', { "topic": work["topic"]+"/basic", "payload":str(work) }, False)

