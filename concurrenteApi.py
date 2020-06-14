from sanic import Sanic
from sanic.response import json
import PyMongo
#from sanic_mongo import Mongo
import datetime

app = Sanic("MoradoConcurrente")

#conf para la conexión con la BD
#nombre de la bd
#app.config['MONGO_DBNAME'] = 'datosard'
#dirección,puerto,bd
#app.config['MONGO_URI'] = 'mongodb:127.0.0.1:27017/datosard'

#mongo = pymongo.app
mongo_uri = "mongodb://{host}:{port}/{database}".format(
	database='datosard',
	port=27017,
	host='localhost'
)
#opcion1
#mongo = Mongo(mongo_uri)
#db = mongo(app)

#opcion2
Mongo.SetConfig(app,test=mongo_uri)
Mongo(app)

#Leer los datos de la bd opcion 1
"""
@app.route('/leer', methods=['GET'])
async def leer_datos():
	framework = mongo.db.framework 
	output = []
	for q in framework.find():
		output.append({'hora' : q['hora'], 'estado' : q['estado']})
	return json({'result' : output})
"""
#Leer los datos de la bd opcion 2
@app.get('/leer')
async def get(request):
	docs = await app.mongo['datosard'].datosard_col.find().to_list()
	for doc in docs:
		doc['id'] = str(doc['_id'])
		#del doc['_id']
	return json(docs)


#INFO QUE PUEDE ESCALAR A INSERTAR 
@app.route('/framework', methods=['POST'])
async def metodoConcurrente(request):
	#En esta parte se recaban los datos del arduino 
	nombre = request.json['nombre']
	estado = request.json['estado']
	#en esta parte se determina la hora
	chora = datetime.datetime.now()
	hora = chora.strftime('%H:%M:%S.%f')
	output = {'nombre' : nombre, 'estado' : estado, 'hora':hora}
	#hasta aqui no debería haber problema
	object_id = await db("coleccion").save(doc)
	return json({'object_id': str(object_id)})
	print(type(app.mongo['datosard']))
	object_id = await app.mongo['datosard']["dispositivos"].save(doc)
	return json({'object_id': str(object_id)})
	return json(output)
	#desplegado de info(en este punto se puede decir que la wea funciona sin necesidad de entrar en bd)

#Leer datos por nombre de dispositivo(incluido en json arduino)(cuestionable)

#PUEDE NO SER NECESARIO
"""
@app.route('/framework/<nombre>', methods=['GET'])
async def get_one_framework(nombre):
	framework = mongo.db.framework

	q = framework.find_one({'nombre' : nombre})

	if q:
		output = {'nombre' : q['nombre'], 'estado' : q['estado'], 'hora':q['hora']}
	else:
		output = 'No results found'

	return json({'result' : output})


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)



#Leer los datos de la bd
@app.route('/leer', methods=['GET'])
async def leer_datos():
    framework = mongo.db.framework 

    output = []

    for q in framework.find():
        output.append({'hora' : q['hora'], 'estado' : q['estado']})

    return jsonify({'result' : output})
"""
