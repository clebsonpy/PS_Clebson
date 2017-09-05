from abc import ABCMeta, abstractmethod
from exceptions import ResourceChangeStateError
from permission import PermissionResource

class ResourceState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print("Status changed")
            self.__class__ = state
        else:
            raise ResourceChangeStateError("Status can not be changed")

class InProcessAllocation(ResourceState):
    name = "In Process Allocation"
    allowed = ["Allocated"]
    permission = PermissionResource().changeState()

class Allocated(ResourceState):
    name = "Allocated"
    allowed = ["In progress"]
    permission = PermissionResource().changeState()

class InProgress(ResourceState):
    name = "In progress"
    allowed = ["Completed"]
    permission = PermissionResource().changeState()

class Completed(ResourceState):
    name = "Completed"
    allowed = ["In Process Allocation"]
    permission = PermissionResource().changeState()