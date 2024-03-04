#  Copyright (c) 2024 Feng Yang
#
#  I am making my contributions/submissions to this project solely in my
#  personal capacity and am not conveying any rights to any intellectual
#  property of any third parties.

from typing import override

from PySide6 import QtWidgets

from SpatialNode.abstract_graph_model import AbstractGraphModel
from SpatialNode.basic_graphics_scene import BasicGraphicsScene
from SpatialNode.connection_graphics_object import ConnectionGraphicsObject
from SpatialNode.definitions import NodeId
from SpatialNode.node_state import NodeState

class NodeGraphicsObject(QtWidgets.QGraphicsObject):
    def __init__(self, scene: BasicGraphicsScene, node: NodeId):
        self._nodeId: NodeId = None
        self._graphModel: AbstractGraphModel = None
        self._nodeState: NodeState = None
        self._proxyWidget: QtWidgets.QGraphicsProxyWidget = None
        ...

    @property
    def graphModel(self) -> AbstractGraphModel: ...
    def nodeScene(self) -> BasicGraphicsScene: ...
    def nodeId(self) -> NodeId: ...
    @property
    def nodeState(self) -> NodeState: ...
    @override
    def boundingRect(self): ...
    def setGeometryChanged(self) -> None: ...
    def moveConnections(self) -> None: ...
    def reactToConnection(self, cgo: ConnectionGraphicsObject) -> None: ...
    @override
    def paint(self, painter, option, widget=...): ...
    @override
    def itemChange(self, change, value): ...
    @override
    def mousePressEvent(self, event): ...
    @override
    def mouseMoveEvent(self, event): ...
    @override
    def mouseReleaseEvent(self, event): ...
    @override
    def hoverEnterEvent(self, event): ...
    @override
    def hoverLeaveEvent(self, event): ...
    @override
    def hoverMoveEvent(self, event): ...
    @override
    def mouseDoubleClickEvent(self, event): ...
    @override
    def contextMenuEvent(self, event): ...
    def _embedQWidget(self) -> None: ...
    def _setLockedState(self) -> None: ...
