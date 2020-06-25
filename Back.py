import json, requests 
from dateutil.relativedelta import relativedelta

def request(concept): 
    
    """""
    concept es un string que nos da el path final de la url a la que queremos consultar
    headers es una constante la cuál contiene nuestra key para acceder a la API del BCR
    más info: https://estadisticasbcra.com/api/documentacion
    response es la variable donde dumpeamos el json con la informacion que queremos
    """""
    url = "https://api.estadisticasbcra.com/"+concept
    headers = {"Authorization": "BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjM5Mjc4MTgsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJsZWNoZXMxMjM3QGdtYWlsLmNvbSJ9.Nc5r_7CfW4F8iye6CbM4sgiLe6nh4UMf_rHt1Vp84aclgn0cbmQdW3XbFZe2cTqR-3fIPo0EH1eEBdd3Sa0V0w"}
    response = json.loads(requests.get(url, headers=headers ).text)
    
    return response

def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return round((abs(current - previous) / previous) * 100.0, 2)
    except ZeroDivisionError:
        return float('inf')
    
def busqueda_ultimo(file):
    dict_v = dict()
    ultimo=file.index(file[-1])
    dict_v['ultimo']=file[ultimo]
    dict_v['var_diario']=[file[ultimo-1]["v"],file[ultimo-1]["d"], get_change(file[ultimo]["v"], file[ultimo-1]["v"])]
    dict_v['var_mensual']=[file[ultimo-30]["v"],file[ultimo-30]["d"], get_change(file[ultimo]["v"], file[ultimo-30]["v"])]
    dict_v['var_anual']=[file[ultimo-360]["v"],file[ultimo-360]["d"], get_change(file[ultimo]["v"], file[ultimo-360]["v"])]
    return dict_v

def historicos(file):
    valor = []
    valor.append(min(file, key=lambda x:x['v']))
    valor.append(max(file, key=lambda x:x['v']))
    return valor        

def lista_por_rango(file, rango):

    if rango == "diario":
        valor = file[-20:]
    elif rango == "mensual":
        ultima = file[-1]
        valor = [ultima]
        x=30
        for i in range(11):    
            valor.append(file[file.index(file[-1])-x])
            x+=30
    elif rango == "anual":
        ultima = file[-1]
        valor = [ultima]
        x=300
        for i in range(11):
            valor.append(file[file.index(file[-1])-x])
            x+=300
    new_valor = [tuple(dic.values()) for dic in valor]
    return list(reversed(new_valor))

def dic_keys_auxiliares():
    stat_label_combo_dict = dict()
    stat_label_combo_dict["Base monetaria"]="base"
    stat_label_combo_dict["Base monetaria dividida USD"]="base_usd"
    stat_label_combo_dict["Reservas internacionales"]="reservas"
    stat_label_combo_dict["Base monetaria dividida reservas internacionales"]="base_div_res"
    stat_label_combo_dict["Cotización del USD"]="usd"
    stat_label_combo_dict["Cotización del USD Oficial"]="usd_of"
    stat_label_combo_dict["Porcentaje de variación entre la cotización del USD y el USD oficial"]="usd_of_minorista"
    stat_label_combo_dict["Circulación monetaria"]="circulacion_monetaria"
    stat_label_combo_dict["Billetes y monedas"]="billetes_y_monedas"
    stat_label_combo_dict["Efectivo en entidades financieras"]="efectivo_en_ent_fin"
    stat_label_combo_dict["Depositos de entidades financieras en cuenta del BCRA"]="depositos_cuenta_ent_fin"
    stat_label_combo_dict["Depósitos"]="depositos"
    stat_label_combo_dict["Cuentas corrientes"]="cuentas_corrientes"
    stat_label_combo_dict["Plazos fijos"]="plazo_fijo"
    stat_label_combo_dict["Prestamos"]="prestamos"
    stat_label_combo_dict["Tasa préstamos personales"]="tasa_prestamos_personales"
    stat_label_combo_dict["Tasa adelantos cuenta corriente"]="tasa_adelantos_cuenta_corriente"
    stat_label_combo_dict["Porcentaje de prestamos en relación a depósito"]="porc_prestamos_vs_depositos"
    stat_label_combo_dict["LEBACs"]="lebac"
    stat_label_combo_dict["LELIQs"]="leliq"
    stat_label_combo_dict["LEBACs en USD"]="lebac_usd"
    stat_label_combo_dict["LELIQs en USD"]="leliq_usd"
    stat_label_combo_dict["Tasa de LELIQs"]="tasa_leliq"
    stat_label_combo_dict["M2 privado variación mensual"]="m2_privado_variacion_mensual"
    stat_label_combo_dict["CER"]="cer"
    stat_label_combo_dict["UVA"]="uva"
    stat_label_combo_dict["UVI"]="uvi"
    stat_label_combo_dict["Tasa BADLAR"]="tasa_badlar"
    stat_label_combo_dict["Tasa BAIBAR"]="tasa_baibar"
    stat_label_combo_dict["Tasa TM20"]="tasa_tm20"
    stat_label_combo_dict["Tasa pase activas a 1 día"]="tasa_pase_activas_1_dia"
    stat_label_combo_dict["Tasa pase pasivas a 1 día"]="tasa_pase_pasivas_1_dia"
    stat_label_combo_dict["Zona de no intervención cambiaria límite inferior"]="zona_de_no_intervencion_cambiaria_limite_inferior"
    stat_label_combo_dict["Zona de no intervención cambiaria límite superior"]="zona_de_no_intervencion_cambiaria_limite_superior"
    stat_label_combo_dict["Inflación mensual oficial"]="inflacion_mensual_oficial"
    stat_label_combo_dict["Inflación interanual oficial"]="inflacion_interanual_oficial"
    stat_label_combo_dict["Inflación esperada oficial"]="inflacion_esperada_oficial"
    stat_label_combo_dict["Diferencia entre inflación interanual oficial y esperada"]="dif_inflacion_esperada_vs_interanual"
    stat_label_combo_dict["Variación base monetaria interanual"]="var_base_monetaria_interanual"
    stat_label_combo_dict["Variación USD interanual"]="var_usd_interanual"
    stat_label_combo_dict["Variación USD (Oficial) interanual"]="var_usd_oficial_interanual"
    stat_label_combo_dict["Variación MERVAL interanual"]="var_merval_interanual"
    stat_label_combo_dict["Variación anual del dólar"]="var_usd_anual"
    stat_label_combo_dict["Variación anual del dólar oficial"]="var_usd_of_anual"
    stat_label_combo_dict["Variación anual del MERVAL"]="var_merval_anual"
    stat_label_combo_dict["MERVAL"]="merval"
    stat_label_combo_dict["MERVAL dividido cotización del USD"]="merval_usd"
    return stat_label_combo_dict
