# Copyright 2017 Great Software Laboratory Pvt. Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from pynos.versions.ver_7.ver_7_0_0.yang.brocade_interface \
    import brocade_interface as brcd_intf
from pynos.versions.ver_7.ver_7_0_0.yang.brocade_rbridge \
    import brocade_rbridge as brcd_rbridge
import pynos.utilities
from pynos.versions.base.interface import Interface as InterfaceBase
import xml.etree.ElementTree as ET
import logging

class Interface(InterfaceBase):
    """
    The Interface class holds all the actions assocaiated with the Interfaces
    of a NOS device.

    Attributes:
        None
    """
    def __init__(self, callback):
        super(Interface, self).__init__(callback)
        self._interface = brcd_intf(callback=pynos.utilities.return_xml)
        self._rbridge = brcd_rbridge(callback=pynos.utilities.return_xml)

    def port_profile_port(self,inter_type, inter,enable=True):
        """
        Activates the Automatic Migration of Port Profiles (AMPP) port-profile configuration mode on a port.

        Args:
          inter_type: The type of interface you want to configure. Ex.
                tengigabitethernet, gigabitethernet, fortygigabitethernet.
          inter: The ID for the interface you want to configure. Ex. 1/0/1
          enable: (bool) Enables port_profile mdode by default. If set to False
                    disables the port-profile mode.
        Returns:
            True if command completes successfully or False if not.

        Raises:
            None
        """

        config = ET.Element("config")
        interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
        tengigabitethernet = ET.SubElement(interface, inter_type)
        name_key = ET.SubElement(tengigabitethernet, "name")
        name_key.text = inter

        if enable:
            port_profile_port = ET.SubElement(tengigabitethernet, "port-profile-port",
                                          xmlns="urn:brocade.com:mgmt:brocade-port-profile")
        else:
            port_profile_port = ET.SubElement(tengigabitethernet, "port-profile-port",
                                          xmlns="urn:brocade.com:mgmt:brocade-port-profile", operation='delete')
        try:
            if enable:
                self._callback(config)
                return True
            else:
                self._callback(config)
                return True
        except Exception as e:
            logging.error(e)
            return False
