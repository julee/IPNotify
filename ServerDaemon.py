import daemon
import Server

with daemon.DaemonContext():
    Server.main()
