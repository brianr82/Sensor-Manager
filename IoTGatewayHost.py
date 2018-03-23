from IoTNode import *


class IoTGatewayHost(IoTNode):
    def __init__(self):

        self.maxNumberOfVirtualIoTGatewaysSupported = 10
        self.virtualIoTGatewayList = []

    def addVirtualGateway(self,new_iotgateway):
        self.virtualIoTGatewayList.append(new_iotgateway)

    def removeVirtualGateway(self,virtual_IoTGateway):
        self.virtualIoTGatewayList.remove(virtual_IoTGateway)

    def hasFreeVirtualGateway(self):

        for virtual_gateway in self.virtualIoTGatewayList:
            if virtual_gateway.checkIfRoomtoAddDevice ():
                return True
        else:
            return False


    def getNextFreeVirtualGateway(self):
        if self.hasFreeVirtualGateway():
            #1. traverse virtualIoTGatewayList []
            for virtual_gateway in self.virtualIoTGatewayList:
                if virtual_gateway.checkIfRoomtoAddDevice():
                    usable_gateway = virtual_gateway
                    return usable_gateway
            #2. if virtual