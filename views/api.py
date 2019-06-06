from functools import wraps
import json
from cassandra.cqlengine import connection
from flask import Blueprint, Response, request, make_response, jsonify
import flask
# from models.user import Person
from models.usuarios import Usuarios
from models.medico import Medico
from models.persona import Persona
from models.turnos import Turnos
import util

__author__ = 'hangvirus'

api = Blueprint("api", __name__)

connection.setup(['192.168.0.120'], "cqlengine", protocol_version=3)


def json_api(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        result = f(*args, **kwargs)  # Call Function
        json_result = util.to_json(result)
        return Response(response=json_result,
                        status=200,
                        mimetype="application/json")

    return decorated_function


@api.route('/', defaults={"path": ""})
@api.route('/<path:path>')
def index(path=None):
    return "Hello World hehe"


#Esto es para registrar, no deberia de estar validado para crearse un usuario
@api.route("/agregar_usuario", methods=["POST"])
@json_api
def add_usuario():
    # print('Request data:', json.dumps(request.data))
    #data = flask.request.data #este da error
    print(request.form['id'])

    #print(data)
    user = Usuarios.create(id=request.form["id"], nombre=request.form["nombre"], password=request.form["password"], estado=request.form["estado"])
    #user = Usuarios.create(id=4, nombre='prueba', password='qwerty', estado=True)
    # print(user)
    user.save()
    return 'ok'




#DESDE AQUI HAY QUE VALIDAR AL USUARIO PARA ENTRAR A ESTOS PATHS
@api.route("/ver_usuario")
@json_api
def get_all_usuario():
    users = Usuarios.objects().all()
    return [user.get_data() for user in users]
#
# #
# @api.route("/agregar_medico", methods=["POST"])
# @json_api
# def add_medico():
#     data = json.loads(flask.request.data)
#     medico = Medico.create(nombre_doc=data["nombre_doc"], cin=data["cin"], horario=data['horario'],
#                            estado_doc=['estado_doc'], especialidad=['especialidad'])
#     medico.save()
#     return medico.get_data()
#
# @api.route("/ver_medico")
# @json_api
# def get_all_medico():
#     medicos = Medico.objects().all()
#     return [medico.get_data() for medico in medicos]
# #
# @api.route("/agregar_persona", methods=["POST"])
# @json_api
# def add_medico():
#     data = json.loads(flask.request.data)
#     persona = Persona.create(nombre_pers=data["nombre_pers"], ci=data["ci"], fecha_nac=data['fecha_nac'],
#                            sexo=['sexo'], telefono=['telefono'], estado_pers=['estado_pers'])
#     persona.save()
#     return persona.get_data()
#
# @api.route("/ver_persona")
# @json_api
# def get_all_persona():
#     personas = Persona.objects().all()
#     return [persona.get_data() for persona in personas]
# #
# @api.route("/agregar_turnos", methods=["POST"])
# @json_api
# def add_turnos():
#     data = json.loads(flask.request.data)
#     turno = Turnos.create(nro_turno=data["nro_turno"], fecha=data["fecha"], hora=data['hora'],
#                            medico=['medico'], persona=['persona'], estado_turnos=['estado_turnos'])
#     turno.save()
#     return turno.get_data()
#
# @api.route("/ver_turnos")
# @json_api
# def get_all_persona():
#     turnos = Turnos.objects().all()
#     return [turno.get_data() for turno in turnos]



######################################################################################################

# @api.route("/add", methods=["POST"])
# @json_api
# def add_person():
#     data = json.loads(flask.request.data)
#     person = Person.create(first_name=data["first_name"], last_name=data["last_name"])
#     person.save()
#     return person.get_data()
#
#
#
# @api.route("/get-all")
# @json_api
# def get_all():
#     persons = Person.objects().all()
#     return [person.get_data() for person in persons]

