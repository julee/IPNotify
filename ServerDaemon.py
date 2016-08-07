import daemon
import Server

with daemon.DaemonContext():
    while True:
        try:
            Server.main()
        except:
            print('exception occured')
