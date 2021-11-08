work= data.copy()

if work.get("lifetime",0) == 0 :
   work["lifetime"]=2

if work.get("repeat",0) == 0 :
   work["repeat"]=3

if work.get("name","") == "" :
   work["name"]="homeassistant"

if work.get("topic","") == "" :
   work["topic"]="awtrix"

if work.get("moveIcon","") == "" :
   work["moveIcon"]=True
#work["force"]=True
work["repeatIcon"]=True

hass.services.call('mqtt', 'publish', { "topic": work["topic"]+"/temporaryapp", "payload":str(work) }, False)

