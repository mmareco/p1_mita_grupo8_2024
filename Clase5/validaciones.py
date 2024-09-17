import re

def validar_correo(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron, correo):
        return True
    return False

def validar_telefono(telefono):
    patron = r'^\+54\s9\s\d{2}\s\d{4}-\d{4}$|^0\d{2}\s\d{4}-\d{4}$'
    if re.match(patron, telefono):
        return True
    return False

def validar_codigo_postal(codigo_postal):
    patron = r'^\d{4}$|^[A-Z]\d{4}[A-Z]{3}$'
    if re.match(patron, codigo_postal):
        return True
    return False

def validar_fecha(fecha):
    patron = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(patron, fecha):
        anio, mes, dia = map(int, fecha.split('-'))
        if 1 <= mes <= 12 and 1 <= dia <= 31:
            if mes == 2 and dia > 29:
                return False
            if mes in {4, 6, 9, 11} and dia > 30:
                return False
            return True
    return False

def validar_datos(datos):
    errores = []
    
    if not validar_correo(datos.get('correo', '')):
        errores.append("El correo electrónico ingresado no es válido.")
    
    if not validar_telefono(datos.get('telefono', '')):
        errores.append("El número de teléfono ingresado no es válido.")
    
    if not validar_codigo_postal(datos.get('codigo_postal', '')):
        errores.append("El código postal ingresado no es válido.")
    
    if not validar_fecha(datos.get('fecha', '')):
        errores.append("La fecha ingresada no es válida.")
    
    if errores:
        return False, errores
    return True, []
