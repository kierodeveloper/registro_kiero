

#   Clase Usuarios Rutas



#   Creada por: ...



#   Fecha creacion: ...







#Archivos necesarios para flask







#Se llama el objeto de flask



from flask import jsonify, request



from flask_mail import Message,Mail

from os import urandom

from routes.router import app,resource,response,req,reqpar



#from database.schemas.catalogo import Catalogo



from flask_mail import Mail

from flask_restful import Resource, reqparse



from app.models.m_registro import mRegistro



#from app.services.sregistro import sRegistro



#from broco import mail

mail = Mail(app)



import json



from flask_restful import Resource, reqparse, request



from passlib.hash import pbkdf2_sha256 as sha256



from datetime import date



import hashlib



from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)



#-*- coding: utf-8 -*-



import pyodbc



#import secrets

#from app.controller.crypto import AES_Encryption ODBC Driver 17 for 



conn = pyodbc.connect('DRIVER={SQL Server};SERVER=190.85.232.78;DATABASE=DBKiero_Productos;UID=sa;PWD=S3rv3r1-27!')



today = date.today()



# dd/mm/YY

get_today = today.strftime("%d/%m/%Y")

#Importando el conector odbc para las conexiones con mssql

import pyodbc

#clase para el control de rutas en usuarios 

# from app.services.connect_to_mysql import mysql

from datetime import datetime  

from datetime import timedelta  

import os

import hashlib

import random
import datetime
date_time = []
today = datetime.date.today()
date_time.append(today)



class registro(resource):

    def __init__(self):

        #   Se aniaden los parametros que se van a utilizar

        pass

    

    def post(self):



        data = request.get_json()


        # registrar = sRegistro(usuario_id=usuario_id) # se llaman a los servicios

        

        random_data = os.urandom(128)

        string_random = hashlib.md5(random_data).hexdigest()[:32]

        with conn: 

            query = """select top(1) email from users where email = '{comprobar_email}'""".format(comprobar_email=data['email'])

            crsr = conn.execute(query)

            rows = crsr.fetchone()

            crsr.fast_executemany = True

        if rows is None:

            try:



                name = data['name']

                lastname = data['lastname']

                email = data['email']

                password = sha256.hash(data['password'])

                nickname = name+str(random.randint(60000, 100000))

                source_ip = request.remote_addr

                email_status=0

                status = 1

                token_confirmation_email = string_random


                new_user = [email,password]



                access_token = create_access_token(identity = data['email'])

                refresh_token = create_refresh_token(identity = data['email'])



                with conn:

                    new_user_save = """insert into users (name,lastname,nickname, email,password,source_ip,email_status,status,create_at,token_confirmation_email,email_confirmation_sent_on) 

                    values ('{name}','{lastname}','{nickname}','{email}','{password}','{source_ip}',{email_status},{status},'{date}','{token_confirmation_email}','{email_confirmation_sent_on}')""".format(name=name,lastname=lastname,nickname=nickname,email=email,password=password,source_ip=source_ip,email_status=email_status,status=status,date=get_today,token_confirmation_email=token_confirmation_email,email_confirmation_sent_on=get_today)

                    conn.execute(new_user_save)

                    crsr.fast_executemany = True
                
                try:
                    msg = Message('Pregunta registrada', sender = 'contacto@kiero.co', recipients = ['diana.gutierrez@kiero.co', 'josefmarin1910@gmail.com','danielabakiero@gmail.com'])
                    msg.body = """
                    Nuevo usuario registrado:

                    Nombre: {name} {lastname}
                    email: {email}
                    fecha: {datetime_re}    

                    """.format(name=name,lastname=lastname,email=email,datetime_re=today)
                    mail.send(msg)
                except Exception as unErr:
                    print(unErr)

               





                data_email_confirmation =str(token_confirmation_email) +'~^~'+ str(date_time[0])

                # token_email = AES_Encryption().encrypt(data_email_confirmation)

                buildConfirmationLink = "https://www.kiero.co/confirmation_email.html?{token_email}".format(token_email=token_confirmation_email)



                try:

                    with app.app_context():

                        msg = Message(subject="Correo de confirmación",

                                    sender=app.config.get("MAIL_USERNAME"),

                                    recipients=[email], # use your email for testing

                                    body="""



correo = {email}

Este es el correo de confirmación, copie el siguiente link y peguelo en el buscador de su navegador favorito                   

{url}

                                    """.format(email=email,url=buildConfirmationLink))

                        mail.send(msg)

                except Exception as err:

                    print(err)



                buildJSON = {

                    'message': 'El usuario {} a sido creado'.format(data['email']),

                    'access_token': access_token,

                    'refresh_token': refresh_token

                    }

                __return = response(json.dumps({"status":1,'result':buildJSON }),status=200, mimetype='application/json') 

                __return.headers['Access-Control-Allow-Origin'] = '*'

                __return.headers['Access-Control-Allow-Methods'] = 'POST'

                __return.headers['Allow'] = 'POST'

                return __return

            except Exception as err:

                print(err)

                __return = response({'Error':'Hubo un error interno'},status=400, mimetype='application/json') 

                __return.headers['Access-Control-Allow-Origin'] = '*'

                __return.headers['Access-Control-Allow-Methods'] = 'POST'

                __return.headers['Allow'] = 'POST'

                return __return



        elif rows[0] == data['email']:

            

            return {'status':0 ,'message': 'User {} already exists'.format(data['email'])}

        


