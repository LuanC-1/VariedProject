import pywhatkit

try:

    pywhatkit.sendwhatmsg("+5511933308762",
                          "Olá eu sou robo,Teste2",
                          18, 36)
    print("Successfully Sent!")

except:

    print("An Unexpected Error!")
