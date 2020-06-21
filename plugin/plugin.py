from __future__ import absolute_import
# for localized messages  	 
from . import _
#################################################################################
#
#    Plugin for Dreambox-Enigma2
#    version:
VERSION = "1.17"
#    Coded by shamann & ims (c)2012 as ClearMem on basic idea by moulikpeta
#	latest modyfication by ims:
#	- ngettext, getMemory, freeMemory, WHERE_PLUGINMENU, Info, translate 
#	- rebuild timers, less code, renamed to CacheFlush
#	- min_free_kbyte, type drop cache, clean dirty cache
#
#    This program is free software; you can redistribute it and/or
#    modify it under the terms of the GNU General Public License
#    as published by the Free Software Foundation; either version 2
#    of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#################################################################################

from Plugins.Plugin import PluginDescriptor
from Components.config import ConfigSubsection, config, ConfigSelection

config.plugins.CacheFlush = ConfigSubsection()
config.plugins.CacheFlush.where = ConfigSelection(default = "0", choices = [("0", _("plugins")), ("1", _("menu-system")), ("2", _("extensions")), ("3", _("event info"))])

def startSetup(menuid, **kwargs):
	if menuid != "system":
		return [ ]
	return [(_("Setup CacheFlush"), main, "CacheFlush", None)]

def sessionAutostart(reason, **kwargs):
	if reason == 0:
		from . import ui
		ui.CacheFlushAuto.startCacheFlush(kwargs["session"])

def main(session,**kwargs):
	from . import ui
	session.open(ui.CacheFlushSetupMenu)

def Plugins(path, **kwargs):
	name = "CacheFlush"
	descr = _("Automatic cache flushing")
	list = [PluginDescriptor(where=[PluginDescriptor.WHERE_SESSIONSTART], fnc=sessionAutostart),]
	if config.plugins.CacheFlush.where.value == "0":
		list.append(PluginDescriptor(name=name, description=descr, where=PluginDescriptor.WHERE_PLUGINMENU, needsRestart = True, icon = 'plugin.png', fnc=main))
	elif config.plugins.CacheFlush.where.value == "1":
		list.append(PluginDescriptor(name=name, description=descr, where=PluginDescriptor.WHERE_MENU, needsRestart = True, fnc=startSetup))
	elif config.plugins.CacheFlush.where.value == "2":
		list.append(PluginDescriptor(name=name, description=descr, where=PluginDescriptor.WHERE_EXTENSIONSMENU, needsRestart = True, fnc=main))
	elif config.plugins.CacheFlush.where.value == "3":
		list.append(PluginDescriptor(name=name, description=descr, where=PluginDescriptor.WHERE_EVENTINFO, needsRestart = True, fnc=main))
	return list

