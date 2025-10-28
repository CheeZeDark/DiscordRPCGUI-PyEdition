import dearpygui.dearpygui as dpg
import sys
import utils

def GetValue(tagname : str):
    return dpg.get_value(tagname)
def Call_RPCConnect():
    return utils.NewThread(lambda: utils.ConnectRPC(statestr=GetValue("staterpc"), descr=GetValue("descr_rpc"), smalltxt=GetValue("smallimage_rpc"), largetxt=GetValue("largeimage_rpc"), name_rpc=GetValue("namerpc"), largeimg=GetValue("largeimage_rpc"), smallimg=GetValue("smallimage_rpc")))
def MainGUI():
    dpg.create_context()
    with dpg.window(label="DiscordRPC", tag="window_drpc"):
        dpg.add_text("Hello, this is my first Python Project for Discord RPC \nSo Enjoy to use this!!!")
        dpg.add_input_text(label="Client ID", tag="CID")
        dpg.add_input_text(label="Name of RPC", tag="namerpc")
        dpg.add_input_text(label="State", tag="staterpc")
        dpg.add_input_text(label="Small Image", tag="smallimage_rpc")
        dpg.add_input_text(label="Large Image", tag="largeimage_rpc")
        dpg.add_input_text(label="Description of Your RPC(Rich Presence)", tag="descr_rpc", width=140, height=140)
        dpg.add_input_text(label="Large Text of RPC", tag="largetxt")
        dpg.add_input_text(label="Small Text of RPC", tag="smalltxt")
        dpg.add_button(label="Connect", callback=Call_RPCConnect)
        dpg.add_button(label="Close RPC", callback=lambda: utils.GetPresence(GetValue("CID")).close())
    dpg.set_primary_window("window_drpc", True)
    dpg.create_viewport(title='Discord RPC', width=750, height=750)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()