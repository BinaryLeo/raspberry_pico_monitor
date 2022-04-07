// Import dependencies
const SerialPort = require('serialport')
const Readline = require('@serialport/parser-readline')
const prompt = require('prompt-sync')({ sigint: true })

let comPort = [] // An empty list to receive our available COM Ports
SerialPort.list() //Promise to return the serial port info
  .then((ports) => {
    comPort = ports.map(function (port) {
      return port.path
    })
    console.table(ports)
    console.log('Available ports: ', comPort)
    runme()
  })
  .catch((err) => console.warn(err, 'e'))

function runme() {
  const sp = prompt('Type a COM port from the list above: ').toUpperCase()
  if (comPort.includes(sp)) {
    // validate with available ports
    let br = '115200' // Default value
    const port = new SerialPort(sp, {
      baudRate: parseInt(br), // Serial takes two parameters: serial device and baudrate
    })
    // The Serial port parser
    const parser = new Readline()
    port.pipe(parser)
    // Read the data from the serial port
    parser.on('data', (line) => console.log('Current temperature: ', line))
  } //
  else {
    console.log('Try again ..')
    runme()
  }
}