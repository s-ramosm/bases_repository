from rest_framework.views import APIView
from rest_framework.response import Response
from .connection import connection



cursor = connection.cursor()




class TiposDocumento(APIView):

    def get(self, request, *args, **kwargs):


        cursor = connection.cursor()
        cursor.execute("SELECT * FROM \"Tipo de Documento\"")
        tipos_documento = cursor.fetchall()
        tipos_documento = [
            {
                "id" : documento[0],
                "documento" : documento[1]
            }
            for documento in tipos_documento
        ]
        cursor.close()
        return Response(tipos_documento)


class GuardarUsuario(APIView):

    def post(self, request, *args, **kwargs):
        usuario = request.data.get("usuario")
        id_tipo_documento = request.data.get("id_tipo_documento")
        nombre = request.data.get("nombre")
        apellido = request.data.get("apellido")
        fecha_nacimiento = request.data.get("fecha_nacimiento")
        numero_documento = request.data.get("numero_documento")
        
        cursor = connection.cursor()
        cursor.execute(" SELECT COUNT(*) FROM \"Candidato\" WHERE \"Usuario\" = '{}'".format(usuario))
        count = cursor.fetchone()[0]
        if count > 0:
            cursor.close()
            return Response({"status": "error", "message": "El usuario ya existe"})
        
        sql = "INSERT INTO \"Candidato\" (\"Usuario\", \"Id Tipo de Documento\", \"Nombre\", \"Apellido\", \"Fecha de Nacimiento\", \"NumeroDocumento\") VALUES ('{}', '{}', '{}', '{}', TO_DATE('{}', 'YYYY-MM-DD'), {})".format(usuario, id_tipo_documento, nombre, apellido, fecha_nacimiento, numero_documento)

        print(sql)
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        
        return Response({"status": "complete"})



# class update(APIView):

#     def post(self,request,*args,**kwargs):
       
#         id = request.data.get("id")
#         nombre = request.data.get("nombre")
#         apellido = request.data.get("apellido")
#         correo = request.data.get("correo")
#         data = cursor.execute("update empleado set apellidoEmpleado='{}', correoEmpleado ='{}', nombreEmpleado='{}' where idEmpleado='{}'".format(apellido,correo,nombre,id))
        
#         connection.commit()
#         return Response( {"status" : "complete"} )

# class registerEmployee (APIView):

#     def get(self,request,*args,**kwargs):
       
        
#         data = cursor.execute("select * from TIPODOCUMENTO").fetchall()
#         tipos = [ {"id" : x[0],  "desc" :  x[1]} for x in data]
        

#         return Response( tipos )


#     def post(self,request, *args, **kwargs):

#         documento = request.data.get("documento")
#         tipoDocumento = request.data.get("tipoDocumento")
#         documento = request.data.get("documento")
#         cargo = request.data.get("cargo")
#         nombre = request.data.get("nombre")
#         apellido = request.data.get("apellido")
#         correo = request.data.get("correo")
#         fecha_Nacimiento = request.data.get("fecha")

#         query = """INSERT INTO EMPLEADO 
#             (idTipoDocumento, idEmpleado, apellidoEmpleado, correoEmpleado,idCargo, nombreEmpleado, fechaNacimientoEmp) 
#             VALUES ('{}', '{}', '{}', '{}', '{}', '{}', TO_DATE('{}', 'yyyy-mm-dd'))""".format(
             
#             tipoDocumento,
#             documento,
#             apellido, 
#             correo, 
#             cargo, 
#             nombre, 
#             fecha_Nacimiento)

#         cursor.execute(query)
#         connection.commit()

#         return Response({"status" : "complete"})


# class registerEmployee (APIView):

#     def get(self,request,*args,**kwargs):
       
        
#         data = cursor.execute("select * from TIPODOCUMENTO").fetchall()
#         tipos = [ {"id" : x[0],  "desc" :  x[1]} for x in data]
        
#         data = cursor.execute("select * from CARGO").fetchall()
#         cargos = [ {"id" : x[0],  "desc" :  x[1]} for x in data]

#         data = cursor.execute("select * from EMPLEADO").fetchall()
#         empleados = [ {"id" : x[0],  "nombre" :  x[3], "apellido" :  x[4], "correo" :  x[5]} for x in data]

#         return Response( {"tipos" : tipos, "cargos" : cargos, "empleados": empleados} )

#     def post(self,request, *args, **kwargs):

#         documento = request.data.get("documento")
#         tipoDocumento = request.data.get("tipoDocumento")
#         documento = request.data.get("documento")
#         cargo = request.data.get("cargo")
#         nombre = request.data.get("nombre")
#         apellido = request.data.get("apellido")
#         correo = request.data.get("correo")
#         fecha_Nacimiento = request.data.get("fecha")

#         query = """INSERT INTO EMPLEADO 
#             (idTipoDocumento, idEmpleado, apellidoEmpleado, correoEmpleado,idCargo, nombreEmpleado, fechaNacimientoEmp) 
#             VALUES ('{}', '{}', '{}', '{}', '{}', '{}', TO_DATE('{}', 'yyyy-mm-dd'))""".format(
             
#             tipoDocumento,
#             documento,
#             apellido, 
#             correo, 
#             cargo, 
#             nombre, 
#             fecha_Nacimiento)

#         cursor.execute(query)
#         connection.commit()

#         return Response({"status" : "complete"})


# class registrerAU(APIView):
    
#     def post(self,request, *args, **kwargs):

#         id = request.data.get("id", "")
        
#         SQL = """select E.NOMEMPLEADO,ES.NOMESPACIO from EMPLEADO E, EMPLEADO_CARGO EC, CARGO C , ESPACIO ES
#                 where E.codEmpleado = EC.codEmpleado and C.idCargo = EC.idCargo and ES.codEspacio = EC.codEspacio 
#                 and E.codEmpleado = '{}' and C.idCargo = '1'
#                 """.format(id)

#         data = cursor.execute(SQL).fetchall()


#         return Response(data)

# class asisDocente(APIView):

#     def post(self,request,*args,**kwargs):
        
#         nombre  = request.data.get("nombre", "")
#         apellido  = request.data.get("apellido", "")

#         SQL = """select E.NOMEMPLEADO,ES.NOMESPACIO from EMPLEADO E, EMPLEADO_CARGO EC, CARGO C , ESPACIO ES
#                 where E.codEmpleado = EC.codEmpleado and C.idCargo = EC.idCargo and ES.codEspacio = EC.codEspacio 
#                 and lower(E.nomEmpleado) = '{}' and lower(E.apellEmpleado) = '{}' and C.idCargo = '2'""".format(
#                     nombre.lower(),
#                     apellido.lower()
#                 )



#         docente = cursor.execute(SQL).fetchone()

#         SQL = """ select *  from TIPOELEMENTO TE, ESTADO E, ELEMENDEPORTIVO ED 
#         where  TE.idTipoElemento = ED.idTipoElemento and E.idEstado = ED.idEstado """

#         return Response({"docente" : docente})


