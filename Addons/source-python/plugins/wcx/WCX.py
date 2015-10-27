
from cvars.public import PublicConVar
from plugins.info import PluginInfo

info = PluginInfo()
info.name = "War3 Extended"
info.author = "necavi"
info.version = "0.1"
info.basename = "wcx"
info.variable = info.basename + "_version"
info.convar = PublicConVar(info.variable, info.version, 0, info.name + " Version")