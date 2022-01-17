#!/usr/bin/python
# -*- coding: utf-8 -*-
# azurevmhelper.py
# It has methods for managing Azure Virtual Machines.

import sys
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient

RESOURCE_GROUP_NAME    = 'AzureExamples'              # Name of the resource group
AZURE_REGION           = 'westeurope'                 # Azure Region location
AVAILABILITY_SET_NAME  = 'myExampleAvailabilitySet'   # Name of the availability set
VNET_NAME              = 'myExampleVNet'              # Name of the virtual network
VNET_ADDRESS_SPACE     = '10.0.0.0/16'                # Address space
SUBNET_NAME            = 'myExampleSubnet'            # Name of the subnet
SUBNET_ADDRESS_SPACE   = '10.0.0.0/24'                # Subnet address space
PUBLIC_IP_NAME         = 'myExamplePublicIP'          # Name of the Public IP
IP_CONFIG_NAME         = 'myExampleIPConfig'          # Name of the IP Config
NETWORK_INTERFACE_NAME = 'myExampleNIC'               # Name of the network interface
AVAILABILITY_SET_NAME  = 'myExampleAvailabilitySet'   # Name of the availability set
VM_NAME                = 'myExampleVM'                # VM name
IMAGE_PUBLISHER        = 'Canonical'                  # Image publisher
IMAGE_OFFER            = 'UbuntuServer'               # Image offer
IMAGE_SKU              = '16.04.0-LTS'                # Image sku
VM_TYPE                = 'Standard_DS1_v2'            # VM size type
VM_USER_NAME           = "user111"                    # User name for VM
VM_PASSWORD            = "Mypass232>"                 # Password for VM

# GLOBAL VARIABLE: resource_client
# GLOBAL VARIABLE: network_client
# GLOBAL VARIABLE: compute_client


def init_resources():
    """
    Init resources
    """
    global resource_client
    global network_client
    global compute_client  

    # Acquire the Azure Subscription Id
    try:
        azure_subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    except KeyError:
        print('Error: Enviroment variable "AZURE_SUBSCRIPTION_ID" does not exist')
        sys.exit(1)

    # Acquire a credential object using CLI-based authentication
    credential = DefaultAzureCredential()

    # Obtain the management object for resources
    resource_client = ResourceManagementClient(credential, azure_subscription_id)

    # Obtain the management object for networks
    network_client = NetworkManagementClient(credential, azure_subscription_id)
    
    # Obtain the management object for virtual machines
    compute_client = ComputeManagementClient(credential, azure_subscription_id)

    # Provision the resource group
    resource_group_result = create_resource_group(resource_client)

    return resource_group_result


def delete_resources():
    """
    Delete resources
    """
    global resource_client

    # Delete the Resource Group
    delete_resource_group(resource_client)
    return


def create_resource_group(resource_client):
    """
    Create the resource group
    """
    print('\nCreating Resource Group ...')
    resource_group_params = { 'location': AZURE_REGION }
    rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME,
                                                                   resource_group_params
                                                                )
    print(f'Provisioned resource group "{rg_result.name}" in the "{rg_result.location}" region')

    return rg_result


def delete_resource_group(resource_client):
    """
    Delete the resource group
    """
    print('\nDeleting Resource Group ..')
    poller = resource_client.resource_groups.begin_delete(RESOURCE_GROUP_NAME)
    rg_result = poller.result()
    print('Deleted')
    return rg_result


def create_availability_set(compute_client):
    """
    Create the Availability Set
    """
    print('Creating Availability set ...')
    avset_params = {
        'location': AZURE_REGION,
        'sku': { 'name': 'Aligned' },
        'platform_fault_domain_count': 3
    }
    availability_set_result = compute_client.availability_sets.create_or_update(
                                  RESOURCE_GROUP_NAME,
                                  AVAILABILITY_SET_NAME,
                                  avset_params
                                )
    print('Provisioned availability set')

    return availability_set_result


def create_vnet(network_client):
    """
    Create the Vnet
    """
    print('Creating Vnet ...')
    vnet_params = {
        'location': AZURE_REGION,
        'address_space': {
            'address_prefixes': [VNET_ADDRESS_SPACE]
        }
    }
    poller = network_client.virtual_networks.begin_create_or_update(
                          RESOURCE_GROUP_NAME,
                          VNET_NAME,
                          vnet_params
                          )
    vnet_result = poller.result()
    print(f'Provisioned virtual network "{vnet_result.name}" with address prefixes "{vnet_result.address_space.address_prefixes}"')

    return vnet_result


def create_subnet(network_client):
    """
    Create the Subnet
    """
    print('Creating Subnet ...')
    subnet_params = {
        'address_prefix': SUBNET_ADDRESS_SPACE
    }
    poller = network_client.subnets.begin_create_or_update(
                        RESOURCE_GROUP_NAME,
                        VNET_NAME,
                        SUBNET_NAME,
                        subnet_params
                      )
    subnet_result = poller.result()
    print(f'Provisioned virtual subnet "{subnet_result.name}" with address prefix "{subnet_result.address_prefix}"')

    return subnet_result


def create_public_ip_address(network_client):
    """
    Create the Public IP Address
    """
    print('Creating Public IP ...')
    public_ip_addess_params = {
        'location': AZURE_REGION,
        "sku": { "name": "Standard" },
        "public_ip_allocation_method": "Static",
        "public_ip_address_version" : "IPV4"
    }
    poller = network_client.public_ip_addresses.begin_create_or_update(
                        RESOURCE_GROUP_NAME,
                        PUBLIC_IP_NAME,
                        public_ip_addess_params
                      )
    ip_address_result = poller.result()
    print(f'Provisioned public IP address "{ip_address_result.name}" with address "{ip_address_result.ip_address}"')

    return ip_address_result


def create_nic(network_client):
    """
    Create the NIC
    """
    print('Creating NIC ...')
    subnet_info = network_client.subnets.get(
                      RESOURCE_GROUP_NAME, 
                      VNET_NAME, 
                      SUBNET_NAME
                    )
    publicIPAddress = network_client.public_ip_addresses.get(
                        RESOURCE_GROUP_NAME,
                        PUBLIC_IP_NAME
                      )
    nic_params = {
        'location': AZURE_REGION,
        'ip_configurations': [{
              'name': IP_CONFIG_NAME,
              'subnet': {
                    'id': subnet_info.id
              },
              'public_ip_address': publicIPAddress,
        }]
    }
    poller = network_client.network_interfaces.begin_create_or_update(
                          RESOURCE_GROUP_NAME,
                          NETWORK_INTERFACE_NAME,
                          nic_params
                      )
    nic_result = poller.result()
    print(f'Provisioned network interface client "{nic_result.name}"')

    return nic_result


def create_vm(network_client, compute_client):  
    """
    Create the VM
    """
    print('Creating VM ...')
    nic = network_client.network_interfaces.get(
                        RESOURCE_GROUP_NAME, 
                        NETWORK_INTERFACE_NAME
                    )
    avset = compute_client.availability_sets.get(
                        RESOURCE_GROUP_NAME,
                        AVAILABILITY_SET_NAME
                    )
    vm_parameters = {
        'location': AZURE_REGION,
        'storage_profile': {
            'image_reference': {
                'publisher': IMAGE_PUBLISHER,
                'offer': IMAGE_OFFER,
                'sku': IMAGE_SKU,
                'version': 'latest'
            }
        },
        'hardware_profile': {
            'vm_size': VM_TYPE
        },
        'os_profile': {
            'computer_name': VM_NAME,
            'admin_username': VM_USER_NAME,
            'admin_password': VM_PASSWORD
        },
        'network_profile': {
            'network_interfaces': [{
                'id': nic.id
            }]
        },
        'availability_set': {
            'id': avset.id
        }
    }
    poller = compute_client.virtual_machines.begin_create_or_update(
                          RESOURCE_GROUP_NAME, 
                          VM_NAME, 
                          vm_parameters
                        )
    vm_result = poller.result()
    print(f'Provisioned virtual machine "{vm_result.name}"')

    return vm_result


def list_vms():
    """
    List all Azure VMs
    """
    global compute_client

    print('\nList VMs in resource group:')
    for vm in compute_client.virtual_machines.list(RESOURCE_GROUP_NAME):
        print("\tVM: {}".format(vm.name))
        virtual_machine = compute_client.virtual_machines.get(
                            RESOURCE_GROUP_NAME, vm.name, expand='instanceView')
        for stat in virtual_machine.instance_view.statuses:
            print("\t    code: ", stat.code)
            print("\t    displayStatus: ", stat.display_status)
    
    return


def run_vm():
    """
    Run an Azure VM
    """
    global compute_client
    global network_client

    print('\nCreating VM and resources ...')    
    create_availability_set(compute_client)
    create_vnet(network_client)
    create_public_ip_address(network_client)
    create_subnet(network_client)
    create_nic(network_client)
    create_vm(network_client, compute_client)
    print('\nVM and resources created')
    return


def list_vm():
    """
    List an Azure VM
    """
    global compute_client

    try:
        vm = compute_client.virtual_machines.get(RESOURCE_GROUP_NAME, VM_NAME, expand='instanceView')
        print("hardwareProfile")
        print("   vmSize: ", vm.hardware_profile.vm_size)
        print("\nstorageProfile")
        print("  imageReference")
        print("    publisher: ", vm.storage_profile.image_reference.publisher)
        print("    offer: ", vm.storage_profile.image_reference.offer)
        print("    sku: ", vm.storage_profile.image_reference.sku)
        print("    version: ", vm.storage_profile.image_reference.version)
        print("  osDisk")
        print("    osType: ", vm.storage_profile.os_disk.os_type)
        print("    name: ", vm.storage_profile.os_disk.name)
        print("    createOption: ", vm.storage_profile.os_disk.create_option)
        print("    caching: ", vm.storage_profile.os_disk.caching)
        print("\nosProfile")
        print("  computerName: ", vm.os_profile.computer_name)
        print("  adminUsername: ", vm.os_profile.admin_username)
        print("  disablePasswordAuthentication: ", vm.os_profile.linux_configuration.disable_password_authentication)
        print("  ssh: ", vm.os_profile.linux_configuration.ssh)
        print("\nnetworkProfile")
        for nic in vm.network_profile.network_interfaces:
            print("  networkInterface id: ", nic.id)
        print("\nvmAgent")
        print("  vmAgentVersion", vm.instance_view.vm_agent.vm_agent_version)
        print("    statuses")
        for stat in vm.instance_view.vm_agent.statuses:
            print("    code: ", stat.code)
            print("    displayStatus: ", stat.display_status)
            print("    message: ", stat.message)
            print("    time: ", stat.time)
        print("\ndisks")
        for disk in vm.instance_view.disks:
            print("  name: ", disk.name)
            print("  statuses")
            for stat in disk.statuses:
                print("    code: ", stat.code)
                print("    displayStatus: ", stat.display_status)
                print("    time: ", stat.time)
        print("\nVM general status")
        print("  provisioningStatus: ", vm.provisioning_state)
        print("  id: ", vm.id)
        print("  name: ", vm.name)
        print("  type: ", vm.type)
        print("  location: ", vm.location)
        print("\nVM instance status")
        for stat in vm.instance_view.statuses:
            print("  code: ", stat.code)
            print("  displayStatus: ", stat.display_status)

    except Exception as e:
        print("\nError:")
        print(e)

    return


def start_vm():
    """
    Start an Azure VM
    """
    global compute_client

    try:
        print('\nStarting VM ...')
        async_vm_start = compute_client.virtual_machines.begin_start(RESOURCE_GROUP_NAME, VM_NAME)
        async_vm_start.wait()
        print('\nVM started')

    except Exception as e:
        print("\nError:")
        print(e)

    return


def stop_vm():
    """
    Stop an Azure VM
    """
    global compute_client

    try:
        print('\nStopping VM ...')
        async_vm_stop = compute_client.virtual_machines.begin_power_off(RESOURCE_GROUP_NAME, VM_NAME)
        async_vm_stop.wait()
        print('\nVM stopped')

    except Exception as e:
        print("\nError:")
        print(e)

    return


def restart_vm():
    """
    Restart an Azure VM
    """
    global compute_client

    try:
        print('\nRestarting VM ...')
        async_vm_restart = compute_client.virtual_machines.begin_restart(RESOURCE_GROUP_NAME, VM_NAME)
        async_vm_restart.wait()
        print('\nVM restarted')

    except Exception as e:
        print("\nError:")
        print(e)

    return


def delete_vm():
    """
    Deallocate & Delete an Azure VM
    """
    global compute_client

    try:
        print('\nDeallocating VM ...')
        # Shuts down the virtual machine and releases the compute resources
        async_vm_deallocate = compute_client.virtual_machines.begin_deallocate(RESOURCE_GROUP_NAME, VM_NAME)
        async_vm_deallocate.wait()
        print('\nVM deallocated')
        
        print('\nDeleting VM ...')
        # Delete the virtual machin
        async_vm_delete = compute_client.virtual_machines.begin_delete(RESOURCE_GROUP_NAME, VM_NAME)
        async_vm_delete.wait()
        print('\nVM deleted')

    except Exception as e:
        print("\nError:")
        print(e)

    return
