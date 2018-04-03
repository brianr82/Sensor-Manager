from IoTNode import *
from IoTDevice import *


class IoTProducerHost(IoTNode):
    def __init__(self, NodeType,NodeName,NodeDockerRemoteClient,NodeIPAddress,NodeDockerPort,*boundNode):
        IoTNode.__init__(self, NodeType,NodeName,NodeDockerRemoteClient,NodeIPAddress,NodeDockerPort,*boundNode)
        self.virtualIoTDeviceList = []
        self.max_allowed_iot_devices_on_this_host = 10
        self.IoTDeviceCounter = 0

    def addVirtualIoTDevice(self,new_iot_device_to_add,BoundIoTVirtualGateway):
        assert isinstance(new_iot_device_to_add,IoTDevice)
        self.virtualIoTDeviceList.append(new_iot_device_to_add)
        BoundIoTVirtualGateway.add_iot_device(new_iot_device_to_add)

        #increment everytime we add, counter will be used to give each new device a unique id
        self.IoTDeviceCounter  = self.IoTDeviceCounter +1

        print new_iot_device_to_add.IoTDeviceName + ' added'


    def removeVirtualIoTDevice(self,existing_iot_device_to_delete,BoundIoTVirtualGateway):
        assert isinstance (existing_iot_device_to_delete, IoTDevice)
        self.virtualIoTDeviceList.remove(existing_iot_device_to_delete)
        BoundIoTVirtualGateway.remove_iot_device (existing_iot_device_to_delete)
        print existing_iot_device_to_delete.IoTDeviceName + ' removed'
