# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_network_interface_show
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test):
    setup_scenario(test)
    # STEP NOT FOUND: /VirtualNetworks/put/Create virtual network
    # STEP NOT FOUND: /Subnets/put/Create subnet
    # STEP NOT FOUND: /PublicIPAddresses/put/Create public IP address defaults
    # STEP NOT FOUND: /NetworkInterfaces/put/Create network interface
    step_network_interface_show(test, checks=[])
    # STEP NOT FOUND: /NetworkInterfaces/get/List virtual machine scale set network interface ip configurations
    step_network_interface_show(test, checks=[])
    # STEP NOT FOUND: /NetworkInterfaces/get/List virtual machine scale set vm network interfaces
    # STEP NOT FOUND: /NetworkInterfaces/get/List virtual machine scale set network interfaces
    # STEP NOT FOUND: /NetworkInterfaces/get/Get network interface
    # STEP NOT FOUND: /NetworkInterfaces/get/List network interfaces in resource group
    # STEP NOT FOUND: /NetworkInterfaces/get/List all network interfaces
    # STEP NOT FOUND: /NetworkInterfaces/post/List network interface effective network security groups
    # STEP NOT FOUND: /NetworkInterfaces/post/Show network interface effective route tables
    # STEP NOT FOUND: /NetworkInterfaces/patch/Update network interface tags
    # STEP NOT FOUND: /NetworkInterfaces/delete/Delete network interface
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class NetworkinterfacesScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(NetworkinterfacesScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myApplicationGateway': 'appgw',
            'myCustomIpPrefix': 'test-customipprefix',
            'myInboundNatRule': self.create_random_name(prefix='natRule1.1'[:5], length=10),
            'myNetworkInterface': 'nic1',
            'myDefaultSecurityRule': 'AllowVnetInBound',
            'myNetworkWatcher': 'nw1',
            'myPublicIpAddress': 'pub1',
            'myVirtualNetwork': 'vnetName',
            'mySubnet': 'subnet1',
            'myVirtualNetworkGatewayConnection': 'vpngw',
            'myVpnSiteLink': 'vpnSiteLink1',
            'myVpnConnection': 'vpnConnection1',
            'myP2sVpnGateway': 'p2svpngateway',
            'myVirtualNetworkGateway': 'vpngateway',
        })

    @ResourceGroupPreparer(name_prefix='clitestnetwork_rg1'[:7], key='rg', parameter_name='rg')
    def test_networkinterfaces_Scenario(self, rg):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
