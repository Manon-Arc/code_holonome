# html + css autre fichier
# envoyer en back dir
# afficher variable dir en temps réel
# controler vitesse
# front manette

import network
import socket
from deplacement import Move
from motor import Motor


def display_ap_info(ap):
    print("\nLocal IP: {}\nSubnet mask: {}\nIP Gateway: {}\nDNS:{}".format(*ap.ifconfig()))
    print("SSID: {}\nChannel: {}".format(ap.config("essid"), ap.config("channel")))
    print("BSSID: {:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(*ap.config("mac")))


def web_page():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<style>
    html {
        font-family: Helvetica;
    }

    body {
        width: auto;
        height: 100svh;
        overflow: hidden;
    }

    .head {
        color: black;
        padding: 2vh;
        margin-bottom: 5%;
    }

    .page {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .joystick {
        position: relative;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-template-rows: repeat(3, 1fr);
        border-radius: 50%;
        background-color: rgb(212, 212, 212);
        box-shadow: none;
    }

    .button {
        width: calc(30vh/3);
        height: calc(30vh/3);
        display: flex;
        color: black;
        text-decoration: none;
        font-size: 30px;
        cursor: pointer;
        border: none;
        z-index: 10;
        user-select: none;
    }

    .av {
        grid-area: 1 / 2 / 2 / 3;
    }

    .avg {
        grid-area: 1 / 1 / 2 / 2;
    }

    .g {
        grid-area: 2 / 1 / 3 / 2;
    }

    .arg {
        grid-area: 3 / 1 / 4 / 2;
    }

    .ar {
        grid-area: 3 / 2 / 4 / 3;
    }

    .ard {
        grid-area: 3 / 3 / 4 / 4;
    }

    .d {
        grid-area: 2 / 3 / 3 / 4;
    }

    .avd {
        grid-area: 1 / 3 / 2 / 4;
    }

    .center {
        grid-area: 2 / 2 / 3 / 3;
    }

    .cursor {
        position: absolute;
        background-color: rgb(72, 72, 72);
        width: calc(30vh/2.3);
        height: calc(30vh/2.3);
        border-radius: 50%;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
    }

    .slidecontent {
        height: 20px;
        width: 250px;
        padding: 10px;
        margin-bottom: 10%;
        border-radius: 20px;
        box-shadow: -3px 4px 15px 1px #ffffff inset, 3px -1px 15px 1px #8d8d8d inset;
    }

    .slider {
        -webkit-appearance: none;
        width: 250px;
        height: 5px;
        border-radius: 5px;
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        -webkit-transition: .2s;
        transition: opacity .2s;
    }

    .slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 15px;
        height: 15px;
        border-radius: 50%;
        cursor: pointer;
        border-radius: 40%;
        background: #939393;
        border: 2px solid #d4d4d4;
        box-shadow: -4px 4px 3px 2px #ffffff, 2px -1px 4px 3px #8d8d8d;

    }

    .slider::-moz-range-thumb {
        width: 200px;
        height: 15px;
        border-radius: 50%;
        position: absolute;
        cursor: pointer;
        border-radius: 40%;
        background: #efefef;
        border: 2px solid #d4d4d4;
        box-shadow: -4px 4px 3px 2px #ffffff, 2px -1px 4px 3px #8d8d8d;

    }

    .slidecontainer {
        display: flex;
        flex-direction: row;
        height: 150px;
        justify-content: space-between;
        align-items: center;
        position: relative;
    }

    .affichage_vitesse {
        margin-bottom: 50%;
    }
</style>

<body>
    <div class="page">
        <div class="head">
            <h1>Motor control :</h1>
        </div>
        <div class="vitesse">
            <div class="affichage_vitesse">
                <label for="sliderValue">Speed :</label>
                <span id="sliderValue"></span>
                <div class="slidecontent">
                    <input type="range" min="0" max="100" value="0" step="1" class="slider" id="myRange" name="slider"
                        onchange=''>
                    <input type="hidden" name="speed" class="slider_speed" value="">
                </div>
            </div>
        </div>
        <div class="joystick">
            <div class="button av" id="av" onmouseenter="sens('av')"; onclick="sendRequest('POST', '/manette', 'joystick', 'av' )" >
            </div>
            <div class="button avg" onmouseenter="sens('avg')"; onclick="sendRequest('POST', '/manette', 'joystick', 'avg' )" >
            </div>
            <div class="button g" onmouseenter="sens('g')"; onclick="sendRequest('POST', '/manette', 'joystick', 'g' )" >
            </div>
            <div class="button arg" onmouseenter="sens('arg')"; onclick="sendRequest('POST', '/manette', 'joystick', 'arg' )" >
            </div>
            <div class="button ar" onmouseenter="sens('ar')"; onclick="sendRequest('POST', '/manette', 'joystick', 'ar' )" >
            </div>
            <div class="button ard" onmouseenter="sens('ard')"; onclick="sendRequest('POST', '/manette', 'joystick', 'ard' )" >
            </div>
            <div class="button d" onmouseenter="sens('d')"; onclick="sendRequest('POST', '/manette', 'joystick', 'd' )" >
            </div>
            <div class="button avd" onmouseenter="sens('avd')"; onclick="sendRequest('POST', '/manette', 'joystick', 'avd' )" >
            </div>
            <div class="button center" onmouseenter="sens('st')"; onclick="sendRequest('POST', '/manette', 'joystick', 'st' )" >
            </div>
            <div class="cursor">
            </div>
        </div>
    </div>
</body>
<script>
    let direction;
    const sens = (sens) => {
        direction = `${sens}`
        console.log(sens)
        return direction
        // envoyer dir en back
    }
    const lache_clique = (e) => {
        e.style.left = "50%";
        e.style.top = "50%";
    }
    const joystick = document.querySelector(".joystick")
    const necessaire = joystick.scrollWidth;
    document.body.addEventListener('touchmove', (e) => {
        let xP = e.touches[0].clientX
        let yP = e.touches[0].clientY
        let cursor = document.querySelector(".cursor");
        const joystick_pos = document.querySelector(".joystick").getBoundingClientRect();
        cursor.style.left = `${xP - joystick_pos.left}px`;
        cursor.style.top = `${yP - joystick_pos.top}px`;
        const cursor_pos = cursor.getBoundingClientRect();

        if (cursor_pos.top < joystick_pos.top) {
            cursor.style.top = `${cursor.scrollWidth / 2}px`;
        }
        if (cursor_pos.bottom > joystick_pos.bottom) {
            cursor.style.top = `${necessaire - cursor.scrollWidth / 2}px`;
        }
        if (cursor_pos.right > joystick_pos.right) {
            cursor.style.left = `${necessaire - cursor.scrollWidth / 2}px`;
        }
        if (cursor_pos.left < joystick_pos.left) {
            cursor.style.left = `${cursor.scrollWidth / 2}px`;
        }
    }
    )

    document.body.addEventListener('touchend', (e) => {
        let cursor = document.querySelector(".cursor");
        cursor.style.left = `50%`;
        cursor.style.top = `50%`;
    }
    )

</script>
<script>
    const slider = document.getElementById("myRange");
    const output = document.getElementById("sliderValue");
    slider.addEventListener("input", function () {
    const value = slider.value;
    output.innerHTML = value;
    });
</script>
<script>
    function sendRequest(method, type, name, dir) {
    console.log("send")
    // Init un variable de requête
    let xhttp = new XMLHttpRequest();
    let url = "";
    // Donne les paramètres de la requête   ("methode", "action", true|false(Async))
    xhttp.open(method, url, true);
    // Informe que l'envoie correspond à un envoie de form (des données sont envoyées)
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    // Donne les informations "name"="value"&"name2"="value2"   pour récuperer la value c'est comme avec un input from("name")
    xhttp.send(`${name}=${dir}`);
    console.log("send dir")
}
</script>
</html>"""

moteur_1 = Motor(16, 17)
moteur_2 = Motor(18, 5)
moteur_3 = Motor(14, 27)
moteur_4 = Motor(26, 25)
movement = Move(16, 17, 18, 5, 14, 27, 26, 25)

def main():
    my_ap = network.WLAN(network.AP_IF)
    my_ap.active(True)
    my_ap.config(essid='ESP-AP', authmode=network.AUTH_WPA_WPA2_PSK, password='123456789')
    display_ap_info(my_ap)

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind(('', 80))
    my_socket.listen(5)

    while True:
        conn, addr = my_socket.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        print('Content = %s' % str(request))
        request_str = str(request)

        if "joystick=avg" in request_str:
            print("avg")
            movement.mov("avg")

        elif "joystick=avd" in request_str:
            print("avd")
            movement.mov("avd")

        elif "joystick=av" in request_str:
            print("av")
            movement.mov("av")

        elif "joystick=g" in request_str:
            print("g")
            movement.mov("g")

        elif "joystick=arg" in request_str:
            print("arg")
            movement.mov("arg")

        elif "joystick=ard" in request_str:
            print("ard")
            movement.mov("ard")

        elif "joystick=ar" in request_str:
            print("ar")
            movement.mov("ar")

        elif "joystick=d" in request_str:
            print("d")
            movement.mov("d")

        elif "joystick=g" in request_str:
            print("g")
            movement.mov("g")

        elif "joystick=st" in request_str:
            print("stop")
            movement.mov("stop")
        else:
            print('No action')

        response = web_page()
        conn.write("HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
        conn.send(response)
        conn.close()


if __name__ == "__main__":
    main()

