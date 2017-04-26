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
from pynos.versions.ver_7.ver_7_1_0.yang.brocade_vswitch import brocade_vswitch



class Vcenter():
    """Vcenter class containing all Vcenter related methods and
    attributes.
    """
    def __init__(self,callback):
        """
        Vcenter init function

        Args:
            callback: Callback function that will be called for each action

        Returns:
            Vcenter Object

        Raises:
            None
        """
        self._callback = callback
        self._brocade_vswitch = brocade_vswitch (callback=pynos.utilities.return_xml)

    def add_vcenter(self,**kwargs):
        """
        Add vCenter on the switch

        Args:
            id(str) : Name of an established vCenter
            url (bool) : vCenter URL
            username (str): Username of the vCenter
            password (str): Password of the vCenter
            callback (function): A function executed upon completion of the
                 method.

        Returns:
           Return value of `callback`.

        Raises:
            None
        """

        config = ET.Element("config")
        vcenter = ET.SubElement(config, "vcenter", xmlns="urn:brocade.com:mgmt:brocade-vswitch")
        id = ET.SubElement(vcenter, "id")
        id.text = kwargs.pop('id')

        credentials = ET.SubElement(vcenter, "credentials")
        url = ET.SubElement(credentials, "url")
        url.text = kwargs.pop('url')

        username = ET.SubElement(credentials, "username")
        username.text = kwargs.pop('username')

        password = ET.SubElement(credentials, "password")
        password.text = kwargs.pop('password')


        try:
            self._callback(config)
            return True

        except Exception as error:
            logging.error(error)
            return False

    def activate_vcenter(self,**kwargs):
        """
        Activate vCenter on the switch

        Args:
            name: (str) : Name of an established vCenter
            activate (bool) : Activates the vCenter if activate=True else deactivates it
            callback (function): A function executed upon completion of the
                 method.

        Returns:
           Return value of `callback`.

        Raises:
            None
        """
        name = kwargs.pop('name')
        activate = kwargs.pop('activate', True)
        vcenter_args = dict(id = name)

        method_class = self._brocade_vswitch
        if activate:
            method_name = 'vcenter_activate'
            vcenter_attr = getattr(method_class, method_name)
            config = vcenter_attr(**vcenter_args)
            output = self._callback(config)
            print output
            return output
        else:
            pass
            #need to add code for vcenter deactivation.

    def get_vcenter(self, **kwargs):
        """
        Get vCenter hosts on the switch

        Args:

            callback (function): A function executed upon completion of the
                 method.

        Returns:
           Returns a list of vcenters

        Raises:
            None
        """

        config = ET.Element("config")
        urn = "urn:brocade.com:mgmt:brocade-vswitch"
        ET.SubElement(config, "vcenter", xmlns=urn)

        output = self._callback(config,handler='get_config')
        result = []
        element = ET.fromstring(str(output))

        for vcenter in element.iter('{%s}vcenter'%urn):
             vc ={}
             vc['name'] = vcenter.find('{%s}id' % urn).text
             vc['url'] = (vcenter.find('{%s}credentials' % urn)).find('{%s}url' % urn).text
             isactive = vcenter.find('{%s}activate' %urn)
             if isactive is None:
                 vc['isactive'] = False
             else:
                vc['isactive'] = True

             result.append(vc)
        return result

