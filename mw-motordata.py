
"""test-attitude.py: Main module to test communication with a MultiWii Board by asking attitude."""

__author__ = "Kiran Kumar Lekkala"

__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

from modules.pyMultiwii import MultiWii
from sys import stdout

if __name__ == "__main__":

    board = MultiWii("/dev/ttyUSB0")
    #board = MultiWii("/dev/tty.SLAB_USBtoUART")
    try:
        while True:
            board.getData(MultiWii.MOTOR)
            #print board.attitude #uncomment for regular printing

            # Fancy printing (might not work on windows...)
            message = "angx = {:+f} \t angy = {:+f} \t heading = {:+f} \t elapsed = {:+f} \t".format(float(board.motor['m1']),float(board.motor['m2']),float(board.motor['m3']),float(board.motor['m4']))
            stdout.write("\r%s" % message )
            stdout.flush()
            # End of fancy printing
    except Exception,error:
        print "Error on Main: "+str(error)
