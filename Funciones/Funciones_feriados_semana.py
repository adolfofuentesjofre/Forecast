# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import holidays
from datetime import timedelta
import calendar
import datetime 
calendar.setfirstweekday(calendar.MONDAY)

#%%

def Feriado(f):
    """
    Función que determina si una fecha es feriado o no

    Parameters
    ----------
    f : Timestamp
        Fecha que se quiere analizar

    Returns
    -------
    A : bool
        Si f es feriado retortna True, si no lo es retorna False

    """
    A = f in holidays.Chile()
    return A

def Diaantesdeferiado(f):
    """
    Función que determina si una fecha es el día anterior a un feriado.

    Parameters
    ----------
    f : Timestamp
         Fecha que se quiere analizar

    Returns
    -------
    int
        Si la fecha corresponde al día anterior de un feriado retorna 1, caso contrario,
        retorna 0.

    """
    if  (f + timedelta(days=1) in holidays.Chile()) & (f not in holidays.Chile()):
        return 1
    else:
        return 0



def Label (dt):
    """
    Función que indica si la fecha se encuentra en la semana inicial, intermedia o final del  mes

    Parameters
    ----------
    df : Datetime
        Fecha que se quiere evaluar

    Returns
    -------
    n_week: int
        Número de la semana en el mes

    """
    # Calcula el número de la semana
    mth = calendar.monthcalendar(dt.year, dt.month)
    for i, wk in enumerate(mth):
        print(i,wk)
        if dt.day in wk:
            n_week = i + 1
            

    # Etiqueta al número de la semana
    max_week = calendar.month(dt.year, dt.month).count('\n') - 2
    if n_week == 1:
        semana = 'Primera'
    elif n_week == max_week:
        semana = 'Ultima'
    else:
        semana = 'Intermedia'
    return semana


def semana_del_mes(data):
    """
    Función que indica si las fechas de un dataframe se encuentra en la semana inicial, intermedia o 
    final del  mes

    Parameters
    ----------
    data : DataFrame
        Columna con datetimes.

    Returns
    -------
    columna: Dataframe
        Dataframe con la etiqueta de la semana en el mes de cada fecha

    """
  
    columna = [Label(x) for x in data]
    return columna
