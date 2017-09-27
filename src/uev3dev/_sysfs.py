"""Internal module for interacting with sysfs"""

import os


class Attribute():
    """A sysfs attribute"""
    def __init__(self, path, attr, mode):
        full_path = path + '/' + attr
        self.attr = open(full_path, mode)

    def read(self):
        """Reads the attribute value

        :return: the value read
        :rtype: str
        """
        self.attr.seek(0)
        return self.attr.read().strip()

    def write(self, value):
        """Writes the attribute value

        :param str value: The value to write
        """
        self.attr.write(value)


class IntAttribute(Attribute):
    """A sysfs attribute that has an integer value"""
    def __init__(self, path, attr, mode):
        super(IntAttribute, self).__init__(path, attr, mode)

    def read(self):
        """Reads the attribute value

        :return: the value read
        :rtype: int
        """
        return int(super(IntAttribute, self).read())

    def write(self, value):
        """Writes the attribute value

        :param int value: The value to write
        """
        super(IntAttribute, self).write(str(value))


class ListAttribute(Attribute):
    """A sysfs attribute that has a space-separated list of values"""
    def __init__(self, path, attr, mode):
        super(ListAttribute, self).__init__(path, attr, mode)

    def read(self):
        """Reads the attribute value

        Returns:
            A list of strings
        """
        return super(ListAttribute, self).read().split(' ')

    def write(self, value):
        """Raises ``RuntimeError``
        """
        raise RuntimeError('Writing to ListAttribute is not supported')


def find_node(subsystem, address, driver):
    """Find a sysfs device node.

    :param str subsystem: The name of the subsystem.
    :param str address: A value to match to the ``address`` attribute.
    :param str driver: A value to match to the ``driver_name`` attribute.
    :return str: The path to the device or None if a match was not found.
    """
    path = '/sys/class/' + subsystem
    for node in os.listdir(path):
        node = path + '/' + node
        addr = Attribute(node, 'address', 'r').read()
        if address != addr:
            continue
        drv = Attribute(node, 'driver_name', 'r').read()
        if driver != driver:
            continue
        return node
