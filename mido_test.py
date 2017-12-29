import mido

from time import sleep

print(mido.get_input_names())

print('\n\n')

def openInputContains(substring):
    for port in mido.get_input_names():
        if substring in port:
            return mido.open_input(port)
    raise Exception("Couldn't find a port that contains '" + substring + "'" )
    
def openOutputContains(substring):
    for port in mido.get_output_names():
        if substring in port:
            return mido.open_output(port)
    raise Exception("Couldn't find a port that contains '" + substring + "'" )


input_in = openInputContains('APC Key 25')

input_out = openOutputContains('Python APC')

output_in = openInputContains('Python APC')
output_out = openOutputContains('APC Key 25')

while True:
    msg = input_in.poll()
    if msg:
        print('Input')
        print(msg)
        print(msg.bytes())
        input_out.send(msg)
        
    msg = output_in.poll()
    if msg:
        print('Output')
        print(msg)
        print(msg.bytes())
        output_out.send(msg)

    sleep(0.001)
