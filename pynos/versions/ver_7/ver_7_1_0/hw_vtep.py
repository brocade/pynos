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
import pynos.utilities
from pynos.versions.ver_7.ver_7_1_0.yang.brocade_tunnels import brocade_tunnels

class hwvtep():
    """hw_vtep class containing all hw_vtep related methods and
    attributes.
    """

    def __init__(self, callback):
        """
        VCS init function

        Args:
            callback: Callback function that will be called for each action

        Returns:
            VCS Object

        Raises:
            None
        """
        self._callback = callback
        self._brocade_tunnels = brocade_tunnels(callback=pynos.utilities.return_xml)

    def hwvtep_set_overlaygw_name(self,**kwargs):
        """
        Set overlay-gateway name on the switch

        Args:
            name (str): overlay_gateway name
            callback (function): A function executed upon completion of the
                 method.

        Returns:
           Return value of `callback`.

        Raises:
            None
        """
        name = kwargs.pop('name')
        name_args = dict(name=name)
        method_name = 'overlay_gateway_name'
        method_class = self._brocade_tunnels
        gw_attr = getattr(method_class, method_name)
        config = gw_attr(**name_args)
        output = self._callback(config)
        return output

    def hwvtep_set_overlaygw_type(self, **kwargs):
        """
        Set gateway type

        Args:
            name  (str): gateway-name
            type (str): gateway-type
            callback (function): A function executed upon completion of the
                method.

        Returns:
            Return value of `callback`.

        Raises:
            None
        """
        name = kwargs.pop('name')
        type = kwargs.pop('type')
        ip_args = dict(name=name, gw_type=type)
        method_name = 'overlay_gateway_gw_type'
        method_class = self._brocade_tunnels
        gw_attr = getattr(method_class, method_name)
        config = gw_attr(**ip_args)
        output = self._callback(config)
        return output

    def hwvtep_add_rbridgeid(self, **kwargs):
        """
        Add a range of rbridge-ids

        Args:
            name  (str): gateway-name
            vlan (str): rbridge-ids range
            callback (function): A function executed upon completion of the
                 method.

        Returns:
           Return value of `callback`.

        Raises:
            None
        """
        name = kwargs.pop('name')
        id = kwargs.pop('rb_range')
        ip_args = dict(name=name,rb_add=id)
        method_name = 'overlay_gateway_attach_rbridge_id_rb_add'
        method_class = self._brocade_tunnels
        gw_attr = getattr(method_class, method_name)
        config = gw_attr(**ip_args)
        output = self._callback(config)
        return output

    def hwvtep_add_loopback_interface(self, **kwargs):
        """
        Add loopback interface to the overlay-gateway

        Args:
            name  (str): gateway-name
            int_id (int): loopback inteface id
            callback (function): A function executed upon completion of the
                 method.

        Returns:
           Return value of `callback`.

        Raises:
            None
        """
        name = kwargs.pop('name')
        id = kwargs.pop('int_id')
        ip_args = dict(name=name,loopback_id=id)
        method_name = 'overlay_gateway_ip_interface_loopback_loopback_id'
        method_class = self._brocade_tunnels
        gw_attr = getattr(method_class, method_name)
        config = gw_attr(**ip_args)
        output = self._callback(config)
        return output

    def hwvtep_add_ve_interface(self,**kwargs):
        """
               Add virtual ethernet (ve) interface to the overlay-gateway

               Args:
                   name  (str): gateway-name
                   int_id (int): ve id
                   vrrp_id (int): VRPP-E group ID
                   callback (function): A function executed upon completion of the
                        method.

               Returns:
                  Return value of `callback`.

               Raises:
                   None
               """
        name = kwargs.pop('name')
        ve_id = kwargs.pop('ve_id')
        vrrp_id = kwargs.pop('vrrp_id')
        ve_args = dict(name=name, ve_id=ve_id)
        method_name = 'overlay_gateway_ip_interface_ve_ve_id'
        method_class = self._brocade_tunnels
        ve_attr = getattr(method_class, method_name)
        config = ve_attr(**ve_args)
        output = self._callback(config)
        method_name = 'overlay_gateway_ip_interface_ve_vrrp_extended_group'
        vrrp_attr = getattr(method_class, method_name)
        vrrp_args = dict(name=name, vrrp_extended_group=vrrp_id)
        config = vrrp_attr(**vrrp_args)
        output = self._callback(config)

        return output

    def hwvtep_activate_hwvtep(self, **kwargs):
        """
        Activate the hwvtep

        Args:
            name (str): overlay_gateway name
            callback (function): A function executed upon completion of the
                 method.

        Returns:
           Return value of `callback`.

        Raises:
            None
        """
        name = kwargs.pop('name')
        name_args = dict(name=name)
        method_name = 'overlay_gateway_activate'
        method_class = self._brocade_tunnels
        gw_attr = getattr(method_class, method_name)
        config = gw_attr(**name_args)
        output = self._callback(config)
        return output

    def hwvtep_attach_vlan_vid(self, **kwargs):
        """
        Identifies exported VLANs in VXLAN gateway configurations.

        Args:
            name (str): overlay_gateway name
            vlan(str):  vlan_id range
            callback (function): A function executed upon completion of the
                 method.

        Returns:
           Return value of `callback`.

        Raises:
            None
        """
        name = kwargs.pop('name')
        mac = kwargs.pop('mac')
        vlan = kwargs.pop('vlan')
        name_args = dict(name=name,vid=vlan,mac=mac)
        method_name= 'overlay_gateway_attach_vlan_mac'
        method_class = self._brocade_tunnels
        gw_attr = getattr(method_class, method_name)
        config = gw_attr(**name_args)
        output = self._callback(config)
        return output

    def get_overlay_gateway(self):
        """
               Get overlay-gateway name on the switch
               Args:
                   callback (function): A function executed upon completion of the
                    method.

               Returns:
                  Dictionary containing details of VXLAN Overlay Gateway.

               Raises:
                   None
        """
        urn = "urn:brocade.com:mgmt:brocade-tunnels"
        config = ET.Element("config")
        ET.SubElement(config, "overlay-gateway" , xmlns = urn)
        output = self._callback(config, handler='get_config')
        result = {}
        element = ET.fromstring(str(output))
        for overlayGw in element.iter('{%s}overlay-gateway' % urn):
            result['name'] = overlayGw.find('{%s}name' % urn).text
            isactivate = overlayGw.find('{%s}activate' % urn)
            if isactivate is None:
                result['activate'] = False
            else:
                result['activate'] = True

            gwtype = overlayGw.find('{%s}gw-type' % urn)
            if gwtype is None:
                result['gwtype'] = None
            else:
                result['gwtype'] = gwtype.text

            attach = overlayGw.find('{%s}attach' % urn)
            if attach is not None:
                rbridgeId = attach.find('{%s}rbridge-id' % urn)
                if rbridgeId is None:
                    result['attached-rbridgeId'] = None
                else:
                    result['attached-rbridgeId'] = rbridgeId.find('{%s}rb-add' % urn).text
                result['attached-vlan'] = None
                vlans = []
                for vlan in attach.iter('{%s}vlan'%urn):
                    vlans.append(vlan.find('{%s}vid' % urn).text)
                result['attached-vlan'] = vlans

        return result
