

<div align="center">
Raspberry Pico Monitor </br>  
Read and display the built in Temperature sensor values of Raspberry Pico.
  
  <a href="#-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-hardware">Hardware</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-how-it-works">How it works</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-gui-application">GUI application</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-command-line-application">Command-Line Application</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-license">License</a>

  
  [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://github.com/BinaryLeo/js_pico-dsport/blob/main/LICENSE)
  ![GitHub last commit](https://img.shields.io/github/last-commit/BinaryLeo/js_pico-dsport?style=flat-square)
  ![GitHub top language](https://img.shields.io/github/languages/top/BinaryLeo/js_pico-dsport?style=flat-square)
</div>

Windows OS - Powershell running the JS application
![node](https://user-images.githubusercontent.com/72607039/162097491-43e5f036-2071-4bd5-aa1c-fa1fd1e89f51.gif)

Windows OS - VS code integrated terminal running the Python application
![python](https://user-images.githubusercontent.com/72607039/149645124-790f4602-bda2-4075-a67f-dd645fe0f65b.gif)</br>


Linux (Pop OS) GUI application</br>
![gui](https://raw.githubusercontent.com/BinaryLeo/raspberry_pico_monitor/main/Resources/gui_app.gif)


## 🧪 technologies

This project was built using the following technologies and features:

Command line application - programming languages:
- Javascript 
- Python

GUI Application:
- Python
- PyQT5

Softwares:
- [Thonny IDE](https://thonny.org/) to upload the config file (Main.py)
- VS Code

## 💻 hardware

- [Raspberry Pico RP2040](https://www.raspberrypi.com/products/raspberry-pi-pico/)
- A USB micro B lead


## 🚀 how it works

<blockquote>
It consists of two applications: Main.py using to read the RP2040 temperature sensor and the other one in (javascript) or (python) to display data from a serial port.
</blockquote>


- [RP2040](https://www.raspberrypi.com/products/raspberry-pi-pico/) read Local temperature through the built in temperature sensor.
- Display data from serial port using a .py or .js solution (Command-line app)
- Display data from serial port - GUI Application
- Run automatically at Windows Startup.

![img](https://github.com/BinaryLeo/js_pico-dsport/blob/main/Resources/Pico-R3-SDK11-Pinout.svg)

## 💡 how to use

- Flash the MicroPython firmware.
- Upload your Main.py to Raspberry Pico.
- Keep the board connected into your computer.

- Clone this repository

<mark style="background-color:#008080" >Choose from the options below</mark> 
## 💻 gui application

in development

## 💻 command line application

🐍 Python
- install the dependencies
<code>pip install pyinstaller</code>
<code>pip install pyserial</code>

The command below will create a /dist directory in your program folder that contains the standalone executable file.

<code>pyinstaller --onefile --icon="exe_resources\Appicon.ico" index.py</code>

📁 javascript command line application
- install the dependencies
- run 
 <code>npm i</code>
 <code>npm install prompt-sync</code>
 <code>npm install -g pkg</code>
 
The code below will generate an .exe file for windows OS and 2 other files.

 <code>pkg index.js</code>

 
<blockquote>
 --onefile / -F : Create a one-file bundled executable.<br/>
 --icon / -i : set an icon to the executable file.

</blockquote>
 Now you have an .exe to show you the local temperature. I've built this project to read the temperature inside my computer.
 More precisely, in summer when our home is very warm.
 
 
 
 ![img](https://github.com/BinaryLeo/js_pico-dsport/blob/main/Resources/pico_inside.jpg)
 
 <br/>

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
