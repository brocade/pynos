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

import logging
import re
import xml.etree.ElementTree as ET
from ipaddress import ip_interface
import pynos.utilities
from ipaddress import ip_interface
from pynos.versions.ver_7.ver_7_1_0.yang.brocade_tunnels import brocade_tunnels

class Nsx():
    """NSX class containing all NSX related methods and
    attributes.
    """
    def __init__(self,callback):
        """
        NSX init function

        Args:
            callback: Callback function that will be called for each action

        Returns:
            NSX Object

        Raises:
            None
        """
        self._callback = callback
        self._brocade_tunnels = brocade_tunnels (callback=pynos.utilities.return_xml)

    def nsx_controller_name(self,**kwargs):
        """
        Get/Set nsx controller name

        Args:
            name: (str) :   Name of the nsx controller
            get (bool) : Get nsx controller config(True,False)
            callback (function): A function executed upon completion of the
                 method.

        Returns:
           Return value of `callback`.

        Raises:
            None
        """
        name = kwargs.pop('name')
        name_args = dict(name=name)
        method_name = 'nsx_controller_name'
        method_class = self._brocade_tunnels
        nsxcontroller_attr = getattr(method_class, method_name)
        config = nsxcontroller_attr(**name_args)

        if kwargs.pop('get',False):
            output  = self._callback(config,handler='get_config')
        else:
            output = self._callback(config)
        return output

    def set_nsxcontroller_ip(self, **kwargs):
        """
        Set nsx-controller IP

        Args:
            IP (str): IPV4 address.
            callback (function): A function executed upon completion of the
                 method.

        Returns:
           Return value of `callback`.

        Raises:
            None
        """
        name = kwargs.pop('name')
        ip_addr = str((kwargs.pop('ip_addr',None)))
        nsxipaddress = ip_interface(unicode(ip_addr))
        if nsxipaddress.version != 4:
            raise ValueError('NSX Controller ip must be IPV4')

        ip_args = dict(name=name,address=ip_addr)
        method_name = 'nsx_controller_connection_addr_address'
        method_class = self._brocade_tunnels
        nsxcontroller_attr = getattr(method_class, method_name)
        config = nsxcontroller_attr(**ip_args)
        output = self._callback(config)
        return output

    def activate_nsxcontroller(self, **kwargs):
        """
        Activate NSX Controller

        Args:
            name (str): nsxcontroller name
            callback (function): A function executed upon completion of the
                 method.

        Returns:
           Return value of `callback`.

        Raises:
            None
        """
        name = kwargs.pop('name')
        name_args = dict(name=name)
        method_name = 'nsx_controller_activate'
        method_class = self._brocade_tunnels
        nsxcontroller_attr = getattr(method_class, method_name)
        config = nsxcontroller_attr(**name_args)
        output = self._callback(config)
        return output

    def set_nsxcontroller_port(self, **kwargs):
        """
        Set Nsx Controller pot on the switch

        Args:
            port (int): 1 to 65535.
            callback (function): A function executed upon completion of the
                 method.

        Returns:
           Return value of `callback`.

        Raises:
            None
        """
        name = kwargs.pop('name')
        port = str(kwargs.pop('port'))
        port_args = dict(name=name, port=port)
        method_name = 'nsx_controller_connection_addr_port'
        method_class = self._brocade_tunnels
        nsxcontroller_attr = getattr(method_class, method_name)
        config = nsxcontroller_attr(**port_args)
        output = self._callback(config)
        return output

    def get_nsx_controller(self):
        """
        Get/Set nsx controller name

        Args:
            name: (str) :   Name of the nsx-controller
            callback (function): A function executed upon completion of the
                method.

            Returns: Return dictionary containing nsx-controller information.
                Returns blank dict if no nsx-controller is configured.

            Raises: None
        """
        urn = "urn:brocade.com:mgmt:brocade-tunnels"
        config = ET.Element("config")
        ET.SubElement(config, "nsx-controller", xmlns = urn)
        output = self._callback(config, handler='get_config')
        result = {}
        element = ET.fromstring(str(output))
        for controller in element.iter('{%s}nsx-controller'%urn):
            result['name'] = controller.find('{%s}name'%urn).text
            isactivate = controller.find('{%s}activate'%urn)
            if isactivate is None:
                result['activate'] = False
            else:
                result['activate'] = True
            connection = controller.find('{%s}connection-addr'%urn)
            if connection is None:
                result['port'] =  None
                result ['address'] = None
            else :
                result['port'] = connection.find('{%s}port'%urn).text
                address = connection.find('{%s}address'%urn)
                if address is None:
                    result ['address'] = None
                else :
                    result['address'] = address.text

        return result
