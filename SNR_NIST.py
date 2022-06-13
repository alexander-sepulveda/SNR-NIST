#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:31:36 2021

@author: alexander
"""

# con este programa se estima el valor SNR (Relación Señal-Ruido) de señales de voz. 
# Para ello utiliza el software proveído por la misma NIST en su página web.
# El código fué bajado y compilado en un ejecutable, para luego ser invocado por
# el presente programa de python. El parámetro de entrada corresponde a la ruta completa
# donde se encuentra el conjunto de archivos a analizar; y, como salida, se entrega
# un archivo en formato excel con los respectivos valores SNR para cada archivo de audio.
# Se asume que los archivos de audio están en formato *.wav a XX KHz.

# librerías a cargar:
import os
import numpy as np
import time
import soundfile as sf           # soundfile permite leer una buena cantidad de formatos de audio.
import sox                       # (Sound eXchange) herramienta multiplataforma para trabajar con archivos de audio. 



def Calcula_SNR_NIST_sin_Diarization(file_name):
    from subprocess import check_output
    
    senal, samplerate = sf.read(file_name)
    mu = np.sum(senal)/len(senal);
    senal = senal - mu;                         # remueve el valor medio de la senal.
    file_name_ = 'tempo_file.wav'
    sf.write(file_name_, senal, samplerate)     # lleva a formato *.wav.
    file_name_out    = 'temp_snr.sph'
    time.sleep(0.2)   # Delays for 0.2 seconds.
    tfm = sox.Transformer();
    tfm.convert(samplerate=None, n_channels=None, bitdepth=16);
    tfm.build(file_name_, file_name_out);       # lleva el audio a formato sphere (NIST), pero con la misma rata de muestreo original.
    
    result = check_output(["./stnr", "-c", "temp_snr.sph"], encoding="utf-8")   # corre archivo ejecutable para cálculo del SNR.
    SNR_str = result[(len(result)-9):(len(result)-4)]     # lee el resultado.
    SNR_str.strip()
    try:
        SNR = float(SNR_str)
    except ValueError:
        print("Oops!  No es un número válido.")
        SNR = -100
        print(result)
        return SNR
    return SNR


# ============== THE MAIN FUNCTION ===========================================================
def main():                                # -- create the main function -------------------
    from xlwt import Workbook
    
    # ------  información a ingresar por el usuario.
    name_CD_audio = 'pedazos'              # nombre del folder de los audios     
    input_folder = '/home/alexander/Desktop/Audios/trabajando/'+name_CD_audio+'/'   # ubicación del anterior folder.
    # -----------------------------
    
    temp_wav = os.getcwd();                # obtiene la ubicación actual del folder (folder de trabajo) 
    temp_wav = temp_wav+'/uno.wav'         # archivo temporal de trabajo requerido.
 
    output_folder = input_folder + "resultados/"      # donde van a quedar los archivos generados.
    if not os.path.exists(output_folder):
           os.mkdir(output_folder)
    
    name_output_file = output_folder + 'valores_SNR.xls';  # nombre del archivo de salida
    
    # Crea la plantilla excel, para luego guardar los resultados generales.
    my_wb  = Workbook()                         # a Workbook is created 
    sheet1 = my_wb.add_sheet('SNR')     # add_sheet is used to create sheet.
    sheet1.write(0, 0, 'archivo') 
    sheet1.write(0, 1, 'SNR [dB]') 
    
    # inicia a recorrer los archivos .wav dentro del folder.
    k = 0
    for the_file in os.listdir(input_folder):
        file_name_in = input_folder + the_file;
        if file_name_in.endswith(".wav"): 
            print(file_name_in)
            SNR = Calcula_SNR_NIST_sin_Diarization(file_name_in)       # calcula el SNR del audio total.
            print(SNR)
            k = k + 1
            sheet1.write(k, 0, the_file)         # almacena el nombre del registro de audio.  
            sheet1.write(k, 1, SNR)              # almacena valor SNR para cada k registro.
    
    my_wb.save(name_output_file)
           
# ----------------------------
main()

