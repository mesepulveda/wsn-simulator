"""Everything related with the simulation of a node."""


class _Node:
    """Defines attributes and methods needed in both sink and sensing nodes."""

    def __init__(self, address, name=None):
        self.address = address
        if name:
            self.name = name
        else:
            self.name = str(address)
        self.neighbours = set()

    def __repr__(self):
        return '{0}, {1}'.format(self.address, self.name)

    def __str__(self):
        return '{0}, {1}'.format(self.address, self.name)


class SensingNode(_Node):
    """Defines attributes and methods of a regular sensing (not sink) node."""

    def __init__(self, address, name=None):
        super().__init__(address, name)

    def get_next_hop_node(self):
        """Returns the node to route data."""
        pass


class SinkNode(_Node):
    """Defines attributes and methods specific for a sink node."""

    def __init__(self, address, name=None):
        super().__init__(address, name)
        pass


class _SimulationNode(_Node):
    """Extends Node class in order to simulate."""

    def __init__(self, address, name=None):
        super().__init__(address, name)

    def clean_simulation(self):
        """Clears logs of simulations."""
        # todo: implement it
        pass


class SimulationSensingNode(SensingNode, _SimulationNode):
    """Extends SensingNode and SimulationNode class in order to simulate."""

    def __init__(self, address, name=None):
        super().__init__(address, name)

    def clean_simulation(self):
        """Clears logs of simulations."""
        # todo: implement it
        super().clean_simulation()
        pass


class SimulationSinkNode(SinkNode, _SimulationNode):
    """Extends SinkNode and SimulationNode class in order to simulate."""

    def __init__(self, address, name=None):
        super().__init__(address, name)

    def clean_simulation(self):
        """Clears logs of simulations."""
        # todo: implement it
        super().clean_simulation()
        pass


def convert_to_simulation_nodes(nodes):
    """Returns simulation nodes from regular nodes."""
    simulation_nodes = []
    for node in nodes:
        address = node.address
        name = node.name
        if isinstance(node, SensingNode):
            simulation_node = SimulationSensingNode(address, name)
        elif isinstance(node, SinkNode):
            simulation_node = SimulationSinkNode(address, name)
        else:
            raise AttributeError('Class of node is not correct')
        simulation_nodes.append(simulation_node)
    return simulation_nodes


def get_equivalent_simulation_node(nodes, simulation_nodes):
    """Returns the equivalent simulation node of one or many nodes."""
    # If it is only one object
    if isinstance(nodes, (SensingNode, SinkNode)):
        return _get_equivalent_node(nodes, simulation_nodes)
    # If it is a list of objects
    equivalent_simulation_nodes = []
    for node in nodes:
        equivalent_node = _get_equivalent_node(node, simulation_nodes)
        equivalent_simulation_nodes.append(equivalent_node)
    return equivalent_simulation_nodes


def _get_equivalent_node(node, simulation_nodes):
    """Returns the equivalent simulation node of one node."""
    for simulation_node in simulation_nodes:
        if node.address == simulation_node.address:
            return simulation_node
