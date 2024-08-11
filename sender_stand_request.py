import configuration
import requests
import data



def get_docs():
    return requests.get(configuration.URL_SERVICE+configuration.DOC_PATH)

response1=get_docs()
print(response1.status_code)


def get_logs():
    return requests.get(configuration.URL_SERVICE+configuration.LOG_MAIN_PATH)

response2=get_logs()
print(response2.status_code)
print(response2.headers)


def get_logs():
    return requests.get(configuration.URL_SERVICE+configuration.LOG_MAIN_PATH,params={"count":20})

response3=get_logs()
print(response3.status_code)
print(response3.headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response4 = get_users_table()
print(response4.status_code)


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_USER_PATH,json=body,headers=data.headers)

response5=post_new_user(data.user_body)
print(response5.status_code)
print(response5.json())

def post_products_kits(products_id):
    return requests.post(configuration.URL_SERVICE+configuration.PRODUCTS_KITS_PATH,json=products_id,headers=data.headers)

response6 = post_products_kits(data.product_ids);
print(response6.status_code)
print(response6.json())



def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)
print(response.headers)
'''

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count": 20})

response = get_logs()
print(response.status_code)
print(response.headers)
'''
'''
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
    '''
'''
response = get_users_table()
print(response.status_code)

ejm post luego lo aplicooo
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
'''

'''
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


response = post_new_user(data.user_body)
print(response.status_code)'''

'''
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())
def post_products_kits(products_ids):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, # Concatenación de URL base y ruta.
                         json=products_ids, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.


response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json()) # Muestra del resultado en la consola
'''
