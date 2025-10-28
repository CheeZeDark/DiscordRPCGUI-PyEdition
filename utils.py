import pypresence as discordrpc
import threading as thread
import GUI as gui
import time
def NewThread(new_thread):
    thr = thread.Thread(target=new_thread)
    return thr.run()
def GetPresence(clientid):
    drpc_pres = discordrpc.Presence(clientid)
    return drpc_pres

def ConnectRPC(statestr, descr, smalltxt, largetxt, name_rpc, smallimg, largeimg):
    starttime = time.time()
    presence = GetPresence(gui.GetValue("CID"))
    presence.connect()
    presence.update(state=statestr, start=starttime, details=descr, name=name_rpc, large_text=largetxt, small_text=smalltxt, small_image=smallimg, large_image=largeimg)