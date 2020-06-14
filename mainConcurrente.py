import asyncio
import http3
import json
import random
"""async def arduino():
	nombre = ["S1","S2","S3","S4","S5"]
	estado = ["left","rigth","center"]
	r1 = random.randint(0, 4)
	r2 = random.randint(0, 2)
	nombre_send = nombre[r1]
	estado_send = estado[r2]
	json_send = {"nombre": nombre_send, "estado": estado_send}
	json_listo = json.loads(json_send)
	return (json_listo)
"""
async def main():
	client = http3.AsyncClient()
	for i in range(50): #50 peticiones
		datos = {"nombre":"nombre_dispositivo","estado":"posición"}
		r = await client.post('http://127.0.0.1:8000/framework', json=datos)
		print(r,i)
asyncio.run(main())

"""
>>> data = {'integer': 123, 'boolean': True, 'list': ['a', 'b', 'c']}
>>> r = httpx.post("https://httpbin.org/post", json=data)
>>> print(r.text)
{
  ...
  "json": {
    "boolean": true,
    "integer": 123,
    "list": [
      "a",
      "b",
      "c"
    ]
  },
  ...
}

#for(i<50){
#nombre=1
#estado="derecha"
#datos=client.post({"name":name, "estado":estado})
#name=name+1
#estado=random_string()
#}
#import requests

#response = requests.post('https://httpbin.org/post', json={'id': 1, 'name': 'Jessa'})

#print("Status code: ", response.status_code)
#print("Printing Entire Post Request")
#print(response.json())
"""
