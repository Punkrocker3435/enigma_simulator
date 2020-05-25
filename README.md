# Enigma Machine Simulator
This is a console simulation of the Enigma Machine used by the Germans in WWII.
It was entirely written in Python.
It simulates the Enigma I version used by the Wehrmacht (German Army).

# Features
1. Encryption / decryption of messages.
2. Fully functional plugboard that supports up to 13 connections. (Minimum 1 connection)
3. A set of 5 different rotors to choose from with the original internal wiring from WWII times.
4. The reflector is also wired as one of the originals.
5. Favourites list for both keys and text snippets. You can only add entries.
6. There is a neat random key generator that you can use.
7. "Animated" machine setting plays when you have finished entering the data.
8. Encrypted text is formatted into 4 letter words separated by spaces to resemble actual messages from WWII.

## How to use the Simulator
### How to set a key
First of all, you have to set the plugboard connections. This program supports from 1 connection to 13 connections. Connections are always 1 to 1. That means:
- Letters cannot be connected to themselves.
- It is not possible to have one letter connected to two letters or more.

Enter the number of desired connections and you'll be prompted to choose all letters on the left side of the connection, that is, if you imagine letters connected by a cable with two plugs, you are expected to plug only one end of the connection.
Once the letters on the left end are done, you are now asked to enter the letters on the right side, that is, to close the connections.
For example, if you want to connect F to Z and G to Q, you will enter F and G first, and then G and Q.

After the plugbloard is done, you are expected to put the rotors in place. You will have a total of 5 rotors, numbered from 1 to 5, from which you have to pick 3 to put into the machine. They will be ordered as FAST, MEDIUM, and SLOW.

IMPORTANT: You only have ONE copy of every rotor, so you cannot repeat the numbers.

Finally, you have to turn the rotors you chose into their initial positions (from A to Z) and that controls into which letter contact will the signal from the plugboard go to when entering the rotors. You are supposed to enter three letters in the order "Fast Medium Slow" to set the rotors up.
