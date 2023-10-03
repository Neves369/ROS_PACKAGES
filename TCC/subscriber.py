#!/usr/bin/env python3
import rospy
from std_msg.msg import Int32
from gtts import gTTS
from playsound import playsound

def callback(data):

    nivel = str(data.data)
    mensagem = "Nível de fumaça " + nivel

    aux = int(data.data)
    print(mensagem)

    if(aux >= 350):
        alerta = "Atenção, foi detectado um elevado nível de gás inflamável!"
        s = gTTS(alerta, lang='pt')
        s.save('sample.mp3')
        playsound('sample.mp3')


def listener():

    #inicia o nó
    rospy.init_node('Ouvindo', anonymous=True)

    s = gTTS('Iniciando', lang='pt')
    s.save('sample.mp3')
    playsound('sample.mp3')

    rospy.Subscriber('smoke', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()