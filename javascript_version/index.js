// Import dependencies
const SerialPort = require("serialport");
const Readline = require("@serialport/parser-readline");

const prompt = require("prompt-sync")({sigint:true});

const sp = prompt("Type a COM port: "); // Allows the user to inform the Port and Bad Rate
const br = prompt("Type the Baud Rate: ");
function runme(){
// Defining the serial port
const port = new SerialPort(sp, {
    baudRate:  parseInt(br)
});

// The Serial port parser
const parser = new Readline();
port.pipe(parser);

// Read the data from the serial port
parser.on("data", (line) => console.log('Current temperature: ', line));
}
runme();