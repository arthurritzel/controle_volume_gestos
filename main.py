import math
import cv2
import mediapipe as mp
import osascript
import platform


# Inicializa a captura de vídeo
# ---------SELECIONE A PORTA DA SUA WEBCAM----------
video = cv2.VideoCapture(1)

# Inicializa o módulo Hands
hands = mp.solutions.hands
Hands = hands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# Verifica o sistema operacional
sistema = platform.system()

while True:
    # Lendo webcam
    sucesso, img = video.read()
    frame_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Processa o video com o modelo Hands
    resultados = Hands.process(frame_rgb)
    pontos_mao = resultados.multi_hand_landmarks
    h, w, _ = img.shape

    pontos = []
    if pontos_mao:
        for pontos_referencia in pontos_mao:
            mpDraw.draw_landmarks(img, pontos_referencia, hands.HAND_CONNECTIONS)

            for id, coordenada in enumerate(pontos_referencia.landmark):
                cx, cy = int(coordenada.x * w), int(coordenada.y * h)
                cv2.putText(img, str(id), (cx, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                pontos.append((cx, cy))

            # Calcula distâncias das retas
            distancia_pausa = math.sqrt(pow((pontos[20][0] - pontos[0][0]), 2) + pow((pontos[20][1] - pontos[0][1]), 2))

            distancia = math.sqrt(pow((pontos[8][0] - pontos[4][0]), 2) + pow((pontos[8][1] - pontos[4][1]), 2))

            # Calcula a porcentagem com base na distância
            if distancia <= 70:
                porcentagem = 0
            elif distancia >= 500:
                porcentagem = 100
            else:
                porcentagem = ((distancia - 70) / (500 - 70)) * 100

            # Calcula o ponto médio da linha de volume
            ponto_medio_0 = int((pontos[8][0] + pontos[4][0]) / 2)
            ponto_medio_1 = int((pontos[8][1] + pontos[4][1]) / 2)

            # Ajusta o volume ou pausa o ajuste de volume caso o dedinho esteja abaixado
            if distancia_pausa < 220:
                # Desenha uma linha entre pontos para o volume
                cv2.line(img, (pontos[8][0], pontos[8][1]), (pontos[4][0], pontos[4][1]), (0,255,127), 3)
                # Escreve a porcentagem na tela
                cv2.putText(img, str(int(porcentagem)) + "%", (ponto_medio_0, ponto_medio_1), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,127), 2)

                if sistema == "Windows":
                    from ctypes import cast, POINTER
                    from comtypes import CLSCTX_ALL
                    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

                    try:
                        # Obtém o controlador de volume do dispositivo de reprodução padrão
                        devices = AudioUtilities.GetSpeakers()
                        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                        volume = cast(interface, POINTER(IAudioEndpointVolume))
                        volume.SetMasterVolumeLevelScalar(int(porcentagem) / 100, None)
                    except Exception as e:
                        print("Erro ao ajustar o volume:", e)

                elif sistema == "Darwin":  # "Darwin" é o sistema base do macOS

                    osascript.osascript("set volume output volume " + str(int(porcentagem)))
                else:
                    print("Sistema operacional não reconhecido.")
            else:
                cv2.rectangle(img, (80, 10), (200, 110), (255, 0, 0), -1)
                cv2.putText(img, "X", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5)

    cv2.imshow('Imagem', img)
    cv2.waitKey(1)


# Libera os recursos ao final
video.release()
cv2.destroyAllWindows()
