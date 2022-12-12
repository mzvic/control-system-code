import sys, Ice
import Rigol
import pyvisa

class interact(Rigol.Interaction):
    inst = pyvisa.ResourceManager().open_resource(pyvisa.ResourceManager().list_resources()[0])
    
    
    def getCommand(self, command, current=None, inst=inst):
        if command == "quit":
            sys.exit()
        # elif command == ":DISPlay:DATA?":
        #     def grab(filename='rigol.bmp', auto_view=True):
        #         # self.rigol().write(':STOP')
        #         buf = inst().query_binary_values(':DISP:DATA?', datatype='B')
        #         with open(filename, 'wb') as f:
        #             self.verbose_print('Capturing screen to', filename)
        #             f.write(bytearray(buf))
        #     grab()
        else:
            inst.write(command)
            print(command)
            


with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("InteractionAdapter", "default -p 10000")
    object = interact()
    adapter.add(object, communicator.stringToIdentity("Interaction"))
    adapter.activate()
    communicator.waitForShutdown()