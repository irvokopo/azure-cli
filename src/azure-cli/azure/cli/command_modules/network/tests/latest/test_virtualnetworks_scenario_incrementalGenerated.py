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
from .example_steps import step_virtual_network_list_usage
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
    # STEP NOT FOUND: /VirtualNetworks/put/Create virtual network with service endpoints and service endpoint policy
    # STEP NOT FOUND: /VirtualNetworks/put/Create virtual network with subnet containing address prefixes
    # STEP NOT FOUND: /VirtualNetworks/put/Create virtual network with Bgp Communities
    # STEP NOT FOUND: /VirtualNetworks/put/Create virtual network
    # STEP NOT FOUND: /VirtualNetworks/put/Create virtual network with service endpoints
    # STEP NOT FOUND: /VirtualNetworks/put/Create virtual network with subnet
    # STEP NOT FOUND: /VirtualNetworks/put/Create virtual network with delegated subnets
    # STEP NOT FOUND: /VirtualNetworks/get/Check IP address availability
    step_virtual_network_list_usage(test, checks=[])
    # STEP NOT FOUND: /VirtualNetworks/get/Get virtual network
    # STEP NOT FOUND: /VirtualNetworks/get/Get virtual network with service association links
    # STEP NOT FOUND: /VirtualNetworks/get/Get virtual network with a delegated subnet
    # STEP NOT FOUND: /VirtualNetworks/get/List virtual networks in resource group
    # STEP NOT FOUND: /VirtualNetworks/get/List all virtual networks
    # STEP NOT FOUND: /VirtualNetworks/patch/Update virtual network tags
    # STEP NOT FOUND: /VirtualNetworks/delete/Delete virtual network
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class VirtualnetworksScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(VirtualnetworksScenarioTest, self).__init__(*args, **kwargs)
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
    def test_virtualnetworks_Scenario(self, rg):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
