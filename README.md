# Hand Recognition and System Volume Control

Este é um sistema em Python que utiliza a biblioteca `mediapipe` para o reconhecimento de mãos e o controle do volume do sistema com gestos. O programa captura o vídeo da webcam, identifica a mão e ajusta o volume do sistema com base nos movimentos da mão.

## Pré-requisitos
- Python 3.x
- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)
- Pycaw (`pip install pycaw`)

Certifique-se de configurar a webcam corretamente e ajustar a variável `video` para a porta da sua webcam.

## Como Usar
1. Execute o script `main.py`.
2. Leve sua mão em frente à webcam.
3. Posicione sua mão em forma de pinça, então aproxime e afaste o dedo indicador do dedão.
4. O ajuste de volume será refletido no sistema operacional.
5. Enquanto a mão estiver totalmente aberta o sistema nao realiza o ajuste de volume

## Funcionalidades
- Reconhecimento de mãos usando a biblioteca Mediapipe.
- Controle de volume dinâmico com gestos.
- Suporte para sistemas Windows e macOS.

## Notas
- Este sistema foi testado em sistemas operacionais Windows e macOS.
- No macOS, utiliza-se o comando `osascript` para ajustar o volume.
- Certifique-se de ter permissões adequadas para controlar o volume do sistema.
- O desempenho pode variar dependendo da qualidade da câmera e das condições de iluminação.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para melhorar o código ou adicionar funcionalidades.


