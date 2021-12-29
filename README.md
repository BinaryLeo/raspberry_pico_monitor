# js_pico-dsport
Output data from raspberry pico temperature sensor in powershell.

<p align="center">
  <a href="#-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-hardware">Hardware</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-how-it-works">How it works</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-how-to-use">How to use</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-license">License</a>
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=8257E5&labelColor=000000">
</p>

## 🧪 technologies

This project was built using the following technologies and features:

- Javascript
- Python
- VS Code
- Powershell with [Oh my posh](https://ohmyposh.dev/)
- [Thonny IDE](https://thonny.org/)  or [Pico-Go VS Code Extension](http://pico-go.net/)

## 💻 hardware

- [Raspberry Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
- A USB micro B lead


## 🚀 how it works

<blockquote>
It consists of two applications, one using python for read the RP2040 temperature sensor. The other in javascript to display data from a serial port.
</blockquote>


- [RP2040](https://www.raspberrypi.com/products/raspberry-pi-pico/) read Local temperature through the built in temperature sensor.
- Read data from serial port using a javascript solution
- Run automatically at Windows Startup. But you can to configure that to other OS.

## 💡 how to use

- Flash the MicroPython firmware.
- Upload your main.py to Raspberry Pico.
- Keep the board connected into your computer.


- Clone this repository
- run:
 <code>npm init -y</code>
 <code>npm install prompt-sync</code>
 <code>npm install -g pkg</code>

The code below will generate an .exe file for windows OS and 2 other files.

 <code>pkg index.js</code>

 Now you have an .exe to show you the local temperature. I've built this project to read the temperature inside my computer.
 More precisely, in summer when our home is very warm.

The next step is optional:

Now we gonna to create a folder to put our .exe file. I've created my folder in C://users/myuser/personalapps/

Open your powershell and paste the code. 
<blockquote> Don't forget to edit the path and the file name</blockquote>

<code>
New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" `
    -Name "Application" `
    -Value "C:\Path\To\MyApplication.exe"
</code>

Press enter and restart your computer. If you followed the instructions, you have now your application running at windows startup. It's simple but usefull! Hope you enjoy it!

## 📄 License

This project was built under MIT. See the file [LICENSE](LICENSE) for more details.

---

Built with 💖 love and burning my 🧠 brain - by Binary Leo 👋🏻 &nbsp;[Find me on linkedin!](https://www.linkedin.com/in/leonardo-moura-92b513209/)