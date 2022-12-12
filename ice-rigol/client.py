import sys, Ice
import Rigol
import pyvisa



with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("Interaction:default -p 10000")
    interaction = Rigol.InteractionPrx.checkedCast(base)
    if not interaction:
        raise RuntimeError("Invalid proxy")
    inst = pyvisa.ResourceManager().open_resource(pyvisa.ResourceManager().list_resources()[0])
    while True:
        command = input("Enter command: ")
        interaction.getCommand(command)
    
    