#!/usr/bin/python
# -*- coding: utf-8 -*-
# azurevmhelper.py
# It has methods for managing Azure Virtual Machines.

import sys
from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption

RESOURCE_GROUP_NAME    = 'AzureExamples'              # Name of the resource group
AZURE_REGION           = 'westeurope'                 # Azure Region location
AVAILABILITY_SET_NAME  = "myExampleAvailabilitySet"   # Name of the availability set
SUBNET_NAME            = "myExampleSubnet"            # Name of the subnet
VIRTUAL_NETWORK_NAME   = "myExampleVN"                # Name of the virtual network
ADDRESS_SPACE          = "10.0.0.0/16"                # Address space
SUBNET_ADDRESS_SPACE   = "10.0.0.0/24"                # Subnet address space
PUBLIC_IP_NAME         = "myExamplePublicIP"          # Name of the Public IP
IP_CONFIG_NAME         = "myExampleIPConfig"          # Name of the IP Config
NETWORK_INTERFACE_NAME = "myExampleNIC"               # Name of the network interface
VM_NAME                = 'myExampleVM'                # VM name
IMAGE_PUBLISHER        = 'Canonical'                  # Image publisher
IMAGE_OFFER            = 'UbuntuServer'               # Image offer
IMAGE_SKU              = '16.04.0-LTS'                # Image sku
VM_TYPE                = 'Basic_A4'                   # VM size type
VM_USER_NAME           = "user111"                    # User name for VM
VM_PASSWORD            = "Mypass232>"                 # Password for VM

# GLOBAL VARIABLE: resource_group_client
# GLOBAL VARIABLE: compute_client
# GLOBAL VARIABLE: network_client


def init_resources():
  """
  Init resources
  """
  global resource_group_client
  global compute_client
  global network_client

  # Get clients with file based authentication
  resource_group_client = get_client_from_auth_file(ResourceManagementClient)
  compute_client = get_client_from_auth_file(ComputeManagementClient)
  network_client = get_client_from_auth_file(NetworkManagementClient)
  # Create the Resource Group
  resource_group_result = create_resource_group(resource_group_client)
  return resource_group_result


def delete_resources():
  """
  Delete resources
  """
  global resource_group_client

  # Delete the Resource Group
  delete_resource_group(resource_group_client)
  return


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

  print('Availability set ...')
  creation_result = create_availability_set(compute_client)
  print('Vnet ...')
  creation_result = create_vnet(network_client)
  print('Public IP ...')
  creation_result = create_public_ip_address(network_client)
  print('Subnet ...')
  creation_result = create_subnet(network_client)
  print('NIC ...')
  creation_result = create_nic(network_client)
  print('VM ...')
  creation_result = create_vm(network_client, compute_client)
  print('Created')
  return creation_result


def list_vm():
  """
  List an Azure VM
  """
  global compute_client

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
  print("    osType: ", vm.storage_profile.os_disk.os_type.value)
  print("    name: ", vm.storage_profile.os_disk.name)
  print("    createOption: ", vm.storage_profile.os_disk.create_option)
  print("    caching: ", vm.storage_profile.os_disk.caching.value)
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

  return


def start_vm():
  """
  Start an Azure VM
  """
  global compute_client

  print('\nStarting VM ...')
  compute_client.virtual_machines.start(RESOURCE_GROUP_NAME, VM_NAME)
  return


def stop_vm():
  """
  Stop an Azure VM
  """
  global compute_client

  print('\nStopping VM ...')
  compute_client.virtual_machines.power_off(RESOURCE_GROUP_NAME, VM_NAME)
  return


def restart_vm():
  """
  Restart an Azure VM
  """
  global compute_client

  print('\nRestarting VM ...')
  compute_client.virtual_machines.restart(RESOURCE_GROUP_NAME, VM_NAME)
  return


def delete_vm():
  """
  Delete/Deallocate an Azure VM
  """
  global compute_client

  print('\nDeleting/Deallocating VM ...')
  compute_client.virtual_machines.deallocate(RESOURCE_GROUP_NAME, VM_NAME)
  compute_client.virtual_machines.delete(RESOURCE_GROUP_NAME, VM_NAME)
  return


def create_resource_group(resource_group_client):
  """
  Create the resource group
  """
  print('\nCreating Resource Group ...')
  resource_group_params = { 'location':AZURE_REGION }
  resource_group_result = resource_group_client.resource_groups.create_or_update(
      RESOURCE_GROUP_NAME, 
      resource_group_params
  )
  return resource_group_result


def delete_resource_group(resource_group_client):
  """
  Delete the resource group
  """
  print('\nDeleting Resource Group ..')
  resource_group_client.resource_groups.delete(RESOURCE_GROUP_NAME)


def create_availability_set(compute_client):
  """
  Create the Availability Set
  """
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

  return availability_set_result


def create_vnet(network_client):
  """
  Create the Vnet
  """
  vnet_params = {
    'location': AZURE_REGION,
    'address_space': {
      'address_prefixes': [ADDRESS_SPACE]
    }
  }
  creation_result = network_client.virtual_networks.create_or_update(
    RESOURCE_GROUP_NAME,
    VIRTUAL_NETWORK_NAME,
    vnet_params
  )
  return creation_result.result()


def create_public_ip_address(network_client):
  """
  Create the Public IP Address
  """
  public_ip_addess_params = {
    'location': AZURE_REGION,
    'public_ip_allocation_method': 'Dynamic'
  }
  creation_result = network_client.public_ip_addresses.create_or_update(
    RESOURCE_GROUP_NAME,
    PUBLIC_IP_NAME,
    public_ip_addess_params
  )

  return creation_result.result()


def create_subnet(network_client):
  """
  Create the Subnet
  """
  subnet_params = {
    'address_prefix': SUBNET_ADDRESS_SPACE
  }
  creation_result = network_client.subnets.create_or_update(
    RESOURCE_GROUP_NAME,
    VIRTUAL_NETWORK_NAME,
    SUBNET_NAME,
    subnet_params
  )

  return creation_result.result()


def create_nic(network_client):
  """
  Create the NIC
  """
  subnet_info = network_client.subnets.get(
    RESOURCE_GROUP_NAME, 
    VIRTUAL_NETWORK_NAME, 
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
      'public_ip_address': publicIPAddress,
      'subnet': {
        'id': subnet_info.id
      }
    }]
  }
  creation_result = network_client.network_interfaces.create_or_update(
    RESOURCE_GROUP_NAME,
    NETWORK_INTERFACE_NAME,
    nic_params
  )

  return creation_result.result()


def create_vm(network_client, compute_client):  
  """
  Create the VM
  """
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
    'os_profile': {
      'computer_name': VM_NAME,
      'admin_username': VM_USER_NAME,
      'admin_password': VM_PASSWORD
    },
    'hardware_profile': {
      'vm_size': VM_TYPE
    },
    'storage_profile': {
      'image_reference': {
        'publisher': IMAGE_PUBLISHER,
        'offer': IMAGE_OFFER,
        'sku': IMAGE_SKU,
        'version': 'latest'
      }
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
  creation_result = compute_client.virtual_machines.create_or_update(
    RESOURCE_GROUP_NAME, 
    VM_NAME, 
    vm_parameters
  )

  return creation_result.result()
