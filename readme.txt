
This tool estimates the Signal-to-Noise Ratio (SNR) by using NIST algorithm (https://www.nist.gov/itl/iad/mig/nist-speech-signal-noise-ratio-measurements). Although NIST (National Institute of Standards and Technology) provides a code to estimate SNR, obtaining a binary file from such code is complicated. A binary file (tested in Linux-Ubuntu) is provided.


La presente rutina estima los valores de relación señal-ruido para una serie de audios localizados en una
carpeta. Se utiliza la versión compilada de los códigos, de nombre spqa_2.3+sphere_2.5.tgz, que reposan en 
https://www.nist.gov/itl/iad/mig/tools . Lograr compilar esos códigos fué una tarea notablemente difícil.

En https://www.nist.gov/itl/iad/mig/nist-speech-signal-noise-ratio-measurements se ofrece una corta explicación 
del método utilizado para la estimación del SNR.

El usuario ha de ingresa al archivo de nombre SNR_NIST.py y modificar las siguientes variables:
name_CD_audio : nombre de la carpeta con los audios.
input_folder  : ruta completa donde se localiza la carpeta con los audios.

La rutina fué creada y probada en "Ubuntu 20.04.1 LTS". A modo de salida se genera una tabla de excel con los valores SNR de salida.
