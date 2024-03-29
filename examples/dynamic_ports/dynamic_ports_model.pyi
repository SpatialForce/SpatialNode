#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

from PySide6 import QtCore

import SpatialNode as sNode
from examples.dynamic_ports.port_add_remove_widget import PortAddRemoveWidget

class DynamicPortsModel(sNode.AbstractGraphModel):
    class NodeGeometryData:
        size: QtCore.QSize
        posL: QtCore.QPointF

    class NodePortCount:
        inPort: int = 0
        outPort: int = 0

    def __init__(self):
        self._nodeIds: set[sNode.NodeId] = None
        self._connectivity: set[sNode.ConnectionId] = None
        self._nodeGeometryData: dict[sNode.NodeId, sNode.NodeGeometryData] = None
        self._nodePortCounts: dict[sNode.NodeId, DynamicPortsModel.NodePortCount] = None
        self._nodeWidgets: dict[sNode.NodeId, PortAddRemoveWidget] = None
        self._nextNodeId: int = None

    def _widget(self, nodeId: sNode.NodeId) -> PortAddRemoveWidget: ...
    @override
    def allNodeIds(self): ...
    @override
    def allConnectionIds(self, nodeId): ...
    @override
    def connections(self, nodeId, portType, index): ...
    @override
    def connectionExists(self, connectionId): ...
    @override
    def addNode(self, nodeType=""): ...
    @override
    def connectionPossible(self, connectionId): ...
    @override
    def addConnection(self, connectionId): ...
    @override
    def nodeExists(self, nodeId): ...
    @override
    def nodeData(self, nodeId, role): ...
    @override
    def setNodeData(self, nodeId, role, value): ...
    @override
    def portData(self, nodeId, portType, index, role): ...
    @override
    def setPortData(self, nodeId, portType, index, value, role=sNode.PortRole.Data): ...
    @override
    def deleteConnection(self, connectionId): ...
    @override
    def deleteNode(self, nodeId): ...
    @override
    def saveNode(self, nodeId): ...
    def save(self): ...
    @override
    def loadNode(self, nodeJson): ...
    def load(self, jsonDocument: sNode.QJsonObject): ...
    def addPort(
        self, nodeId: sNode.NodeId, portType: sNode.PortType, portIndex: sNode.PortIndex
    ): ...
    def removePort(
        self, nodeId: sNode.NodeId, portType: sNode.PortType, first: sNode.PortIndex
    ): ...
    @override
    def newNodeId(self): ...
