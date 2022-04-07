# js_pico-dsport
Reading built in Temperature sensor values of Raspberry Pico  with PowerShell.

<p align="center">
  <a href="#-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-hardware">Hardware</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-how-it-works">How it works</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-javascript-version">Javascript version</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-python-version">Python version</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-license">License</a>
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=008080&labelColor=000000">
</p>

![node](https://user-images.githubusercontent.com/72607039/162097491-43e5f036-2071-4bd5-aa1c-fa1fd1e89f51.gif)
![python](https://user-images.githubusercontent.com/72607039/149645124-790f4602-bda2-4075-a67f-dd645fe0f65b.gif)

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
It consists of two applications, one using python for read the RP2040 temperature sensor. The other in (javascript) or (python) to display data from a serial port.
</blockquote>


- [RP2040](https://www.raspberrypi.com/products/raspberry-pi-pico/) read Local temperature through the built in temperature sensor.
- Read data from serial port using a .py or .js solution
- Run automatically at Windows Startup. But you can to configure that to other OS.

![img](https://github.com/BinaryLeo/js_pico-dsport/blob/main/Resources/Pico-R3-SDK11-Pinout.svg)

## 💡 how to use

- Flash the MicroPython firmware.
- Upload your main.py to Raspberry Pico.
- Keep the board connected into your computer.

- Clone this repository

<mark style="background-color:#008080" >Choose between two paths: JS or Python</mark> 


## 📁 javascript version
- run
 <code>npm init -y</code>
 <code>npm install prompt-sync</code>
 <code>npm install -g pkg</code>
 
The code below will generate an .exe file for windows OS and 2 other files.

 <code>pkg index.js</code>

## 🐍 python version
- run
<code>pip install pyinstaller</code>

The command below will create a /dist directory in your program folder that contains the standalone executable file.

<code>pyinstaller --onefile --icon="exe_resources\Appicon.ico" index.py</code>

 
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
