"""
created by Nikolay V. Ulyanov (ulianownv@mail.ru)
http://www.smcsystem.ru
"""
import datetime
from __builtin__ import long, unicode
from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import List, Dict, Optional


class ModuleException(Exception):
    """main exception"""

    def __init__(self, text):
        super(ModuleException, self).__init__(text)
        self.txt = text


# class ActionType(Enum):
#     __order__ = 'START EXECUTE UPDATE STOP'
#     START = 0
#     EXECUTE = 1
#     UPDATE = 2
#     STOP = 3
ActionType = Enum('START', 'EXECUTE', 'UPDATE', 'STOP')
ActionType.START.value = 0
ActionType.EXECUTE.value = 1
ActionType.UPDATE.value = 2
ActionType.STOP.value = 3

# class CommandType(Enum):
#     __order__ = 'START EXECUTE UPDATE STOP'
#     START = 0
#     EXECUTE = 1
#     UPDATE = 2
#     STOP = 3
CommandType = Enum('START', 'EXECUTE', 'UPDATE', 'STOP')
CommandType.START.value = 0
CommandType.EXECUTE.value = 1
CommandType.UPDATE.value = 2
CommandType.STOP.value = 3

# class MessageType(Enum):
#     PROCESS_STATE_CHANGE = 1
#
#     ACTION_START = 4
#     ACTION_STOP = 6
#     ACTION_ERROR = 7
#
#     CONFIGURATION_CONTROL_CONFIGURATION_SETTING_UPDATE = 108
#     CONFIGURATION_CONTROL_CONFIGURATION_VARIABLE_UPDATE = 109
#     CONFIGURATION_CONTROL_CONFIGURATION_VARIABLE_REMOVE = 110
#     CONFIGURATION_CONTROL_CONFIGURATION_CREATE = 111
#     CONFIGURATION_CONTROL_CONFIGURATION_UPDATE = 112
#     CONFIGURATION_CONTROL_CONFIGURATION_REMOVE = 113
#     CONFIGURATION_CONTROL_EXECUTION_CONTEXT_CREATE = 114
#     CONFIGURATION_CONTROL_EXECUTION_CONTEXT_UPDATE = 115
#     CONFIGURATION_CONTROL_EXECUTION_CONTEXT_REMOVE = 116
#     CONFIGURATION_CONTROL_SOURCE_CONTEXT_CREATE = 117
#     CONFIGURATION_CONTROL_SOURCE_CONTEXT_UPDATE = 118
#     CONFIGURATION_CONTROL_SOURCE_CONTEXT_REMOVE = 119
#     CONFIGURATION_CONTROL_CONTAINER_CREATE = 120
#     CONFIGURATION_CONTROL_CONTAINER_REMOVE = 121
#
#     FLOW_CONTROL_EXECUTE_NOW_START = 220
#     FLOW_CONTROL_EXECUTE_NOW_EXECUTE = 221
#     FLOW_CONTROL_EXECUTE_NOW_UPDATE = 222
#     FLOW_CONTROL_EXECUTE_NOW_STOP = 223
#     FLOW_CONTROL_EXECUTE_PARALLEL_START = 224
#     FLOW_CONTROL_EXECUTE_PARALLEL_EXECUTE = 225
#     FLOW_CONTROL_EXECUTE_PARALLEL_UPDATE = 226
#     FLOW_CONTROL_EXECUTE_PARALLEL_STOP = 227
#     FLOW_CONTROL_EXECUTE_PARALLEL_WAITING_TACTS = 228
#
#     ERROR = 1000
#     DATA = 1001
#     LOG = 1002
MessageType = Enum('PROCESS_STATE_CHANGE', 'ACTION_START', 'ACTION_STOP', 'ACTION_ERROR'
                   , 'CONFIGURATION_CONTROL_CONFIGURATION_SETTING_UPDATE', 'CONFIGURATION_CONTROL_CONFIGURATION_VARIABLE_UPDATE'
                   , 'CONFIGURATION_CONTROL_CONFIGURATION_VARIABLE_REMOVE', 'CONFIGURATION_CONTROL_CONFIGURATION_CREATE'
                   , 'CONFIGURATION_CONTROL_CONFIGURATION_UPDATE', 'CONFIGURATION_CONTROL_CONFIGURATION_REMOVE'
                   , 'CONFIGURATION_CONTROL_EXECUTION_CONTEXT_CREATE', 'CONFIGURATION_CONTROL_EXECUTION_CONTEXT_UPDATE'
                   , 'CONFIGURATION_CONTROL_EXECUTION_CONTEXT_REMOVE', 'CONFIGURATION_CONTROL_SOURCE_CONTEXT_CREATE'
                   , 'CONFIGURATION_CONTROL_SOURCE_CONTEXT_UPDATE', 'CONFIGURATION_CONTROL_SOURCE_CONTEXT_REMOVE'
                   , 'CONFIGURATION_CONTROL_CONTAINER_CREATE', 'CONFIGURATION_CONTROL_CONTAINER_REMOVE'
                   , 'FLOW_CONTROL_EXECUTE_NOW_START', 'FLOW_CONTROL_EXECUTE_NOW_EXECUTE'
                   , 'FLOW_CONTROL_EXECUTE_NOW_UPDATE', 'FLOW_CONTROL_EXECUTE_NOW_STOP'
                   , 'FLOW_CONTROL_EXECUTE_PARALLEL_START', 'FLOW_CONTROL_EXECUTE_PARALLEL_EXECUTE'
                   , 'FLOW_CONTROL_EXECUTE_PARALLEL_UPDATE', 'FLOW_CONTROL_EXECUTE_PARALLEL_STOP'
                   , 'FLOW_CONTROL_EXECUTE_PARALLEL_WAITING_TACTS'
                   , 'ERROR', 'DATA', 'LOG'
                   )
MessageType.PROCESS_STATE_CHANGE.value = 1
MessageType.ACTION_START.value = 4
MessageType.ACTION_STOP.value = 6
MessageType.ACTION_ERROR.value = 7
MessageType.CONFIGURATION_CONTROL_CONFIGURATION_SETTING_UPDATE.value = 108
MessageType.CONFIGURATION_CONTROL_CONFIGURATION_VARIABLE_UPDATE.value = 109
MessageType.CONFIGURATION_CONTROL_CONFIGURATION_VARIABLE_REMOVE.value = 110
MessageType.CONFIGURATION_CONTROL_CONFIGURATION_CREATE.value = 111
MessageType.CONFIGURATION_CONTROL_CONFIGURATION_UPDATE.value = 112
MessageType.CONFIGURATION_CONTROL_CONFIGURATION_REMOVE.value = 113
MessageType.CONFIGURATION_CONTROL_EXECUTION_CONTEXT_CREATE.value = 114
MessageType.CONFIGURATION_CONTROL_EXECUTION_CONTEXT_UPDATE.value = 115
MessageType.CONFIGURATION_CONTROL_EXECUTION_CONTEXT_REMOVE.value = 116
MessageType.CONFIGURATION_CONTROL_SOURCE_CONTEXT_CREATE.value = 117
MessageType.CONFIGURATION_CONTROL_SOURCE_CONTEXT_UPDATE.value = 118
MessageType.CONFIGURATION_CONTROL_SOURCE_CONTEXT_REMOVE.value = 119
MessageType.CONFIGURATION_CONTROL_CONTAINER_CREATE.value = 120
MessageType.CONFIGURATION_CONTROL_CONTAINER_REMOVE.value = 121
MessageType.FLOW_CONTROL_EXECUTE_NOW_START.value = 220
MessageType.FLOW_CONTROL_EXECUTE_NOW_EXECUTE.value = 221
MessageType.FLOW_CONTROL_EXECUTE_NOW_UPDATE.value = 222
MessageType.FLOW_CONTROL_EXECUTE_NOW_STOP.value = 223
MessageType.FLOW_CONTROL_EXECUTE_PARALLEL_START.value = 224
MessageType.FLOW_CONTROL_EXECUTE_PARALLEL_EXECUTE.value = 225
MessageType.FLOW_CONTROL_EXECUTE_PARALLEL_UPDATE.value = 226
MessageType.FLOW_CONTROL_EXECUTE_PARALLEL_STOP.value = 227
MessageType.FLOW_CONTROL_EXECUTE_PARALLEL_WAITING_TACTS.value = 228
MessageType.ERROR.value = 1000
MessageType.DATA.value = 1001
MessageType.LOG.value = 1002

# class ValueType(Enum):
#     __order__ = 'STRING BYTE SHORT INTEGER LONG BIG_INTEGER FLOAT DOUBLE BIG_DECIMAL BYTES'
#     STRING = 0
#     BYTE = 1
#     SHORT = 2
#     INTEGER = 3
#     LONG = 4
#     BIG_INTEGER = 5
#     FLOAT = 6
#     DOUBLE = 7
#     BIG_DECIMAL = 8
#     BYTES = 9
ValueType = Enum('STRING', 'BYTE', 'SHORT', 'INTEGER', 'LONG', 'BIG_INTEGER', 'FLOAT', 'DOUBLE', 'BIG_DECIMAL', 'BYTES', 'OBJECT_ARRAY', 'BOOLEAN')
ValueType.STRING.value = 0
ValueType.BYTE.value = 1
ValueType.SHORT.value = 2
ValueType.INTEGER.value = 3
ValueType.LONG.value = 4
ValueType.BIG_INTEGER.value = 5
ValueType.FLOAT.value = 6
ValueType.DOUBLE.value = 7
ValueType.BIG_DECIMAL.value = 8
ValueType.BYTES.value = 9
ValueType.OBJECT_ARRAY.value = 10
ValueType.BOOLEAN.value = 11

# class SourceType(Enum):
#     __order__ = 'MODULE_CONFIGURATION EXECUTION_CONTEXT STATIC_VALUE MULTIPART CALLER CALLER_RELATIVE_NAME'
#     MODULE_CONFIGURATION = 0
#     EXECUTION_CONTEXT = 1
#     STATIC_VALUE = 2
#     MULTIPART = 3
#     CALLER = 4
#     CALLER_RELATIVE_NAME = 5
SourceType = Enum('MODULE_CONFIGURATION', 'EXECUTION_CONTEXT', 'STATIC_VALUE', 'MULTIPART', 'CALLER', 'CALLER_RELATIVE_NAME', 'OBJECT_ARRAY')
SourceType.MODULE_CONFIGURATION.value = 0
SourceType.EXECUTION_CONTEXT.value = 1
SourceType.STATIC_VALUE.value = 2
SourceType.MULTIPART.value = 3
SourceType.CALLER.value = 4
SourceType.CALLER_RELATIVE_NAME.value = 5
SourceType.OBJECT_ARRAY.value = 6

# class SourceGetType(Enum):
#     __order__ = 'ALL NEW NEW_ALL LAST LAST_ALL'
#     ALL = 0
#     NEW = 1
#     NEW_ALL = 2
#     LAST = 3
#     LAST_ALL = 4
SourceGetType = Enum('ALL', 'NEW', 'NEW_ALL', 'LAST', 'LAST_ALL')
SourceGetType.ALL.value = 0
SourceGetType.NEW.value = 1
SourceGetType.NEW_ALL.value = 2
SourceGetType.LAST.value = 3
SourceGetType.LAST_ALL.value = 4

# class SourceFilterType(Enum):
#     __order__ = 'POSITION NUMBER STRING_EQUAL STRING_CONTAIN'
#     POSITION = 0
#     NUMBER = 1
#     STRING_EQUAL = 2
#     STRING_CONTAIN = 3
SourceFilterType = Enum('POSITION', 'NUMBER', 'STRING_EQUAL', 'STRING_CONTAIN', 'OBJECT_PATHS')
SourceFilterType.POSITION.value = 0
SourceFilterType.NUMBER.value = 1
SourceFilterType.STRING_EQUAL.value = 2
SourceFilterType.STRING_CONTAIN.value = 3
SourceFilterType.OBJECT_PATHS.value = 4


class IValue:
    """Interface for value objects"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getType(self):
        # type: () -> ValueType
        """value type"""
        pass

    @abstractmethod
    def getValue(self):
        # type: () -> str or bytes or int or long or float or bool or ObjectArray
        """value as object"""
        pass


class IMessage(IValue):
    """Interface for Message"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getDate(self):
        # type: () -> datetime
        """get date of creation"""
        pass

    @abstractmethod
    def getMessageType(self):
        # type: () -> MessageType
        """get message type
        for process messages - DATA"""
        pass


class IAction:
    """Interface for Action"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getMessages(self):
        # type: () -> List[IMessage]
        """get messages"""
        pass

    @abstractmethod
    def getType(self):
        # type: () -> ActionType
        """get type"""
        pass


class ICommand:
    """Interface for Command"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getActions(self):
        # type: () -> List[IAction]
        """get actions"""
        pass

    @abstractmethod
    def getType(self):
        # type: () -> CommandType
        """get type"""
        pass


# class ObjectType(Enum):
#     __order__ = 'OBJECT_ARRAY OBJECT_ELEMENT OBJECT_ELEMENT_SIMPLE VALUE_ANY STRING BYTE SHORT INTEGER LONG FLOAT DOUBLE BIG_INTEGER BIG_DECIMAL BYTES'
#     OBJECT_ARRAY = 0
#     OBJECT_ELEMENT = 1
#     OBJECT_ELEMENT_SIMPLE = 2
#     VALUE_ANY = 3
#     STRING = 4
#     BYTE = 5
#     SHORT = 6
#     INTEGER = 7
#     LONG = 8
#     FLOAT = 9
#     DOUBLE = 10
#     BIG_INTEGER = 11
#     BIG_DECIMAL = 12
#     BYTES = 13
ObjectType = Enum('OBJECT_ARRAY', 'OBJECT_ELEMENT', 'VALUE_ANY', 'STRING', 'BYTE', 'SHORT', 'INTEGER', 'LONG', 'FLOAT', 'DOUBLE', 'BIG_INTEGER',
                  'BIG_DECIMAL', 'BYTES', 'BOOLEAN')
ObjectType.OBJECT_ARRAY.value = 0
ObjectType.OBJECT_ELEMENT.value = 1
ObjectType.VALUE_ANY.value = 2
ObjectType.STRING.value = 3
ObjectType.BYTE.value = 4
ObjectType.SHORT.value = 5
ObjectType.INTEGER.value = 6
ObjectType.LONG.value = 7
ObjectType.FLOAT.value = 8
ObjectType.DOUBLE.value = 9
ObjectType.BIG_INTEGER.value = 10
ObjectType.BIG_DECIMAL.value = 11
ObjectType.BYTES.value = 12
ObjectType.BOOLEAN.value = 13


class ObjectField(object):
    def __init__(self, name, value=None, typev=None):
        # type: (str, object, ObjectType) -> None
        self.name = name
        self.type = typev
        self.value = value
        if value is not None and typev is None:
            self.setValue(value)

    def setValue(self, value, typev=None):
        # type: (object, type) -> None
        self.value = value
        if value is not None:
            valueType = type(value)
        else:
            valueType = None
        if typev is None:
            if valueType is ObjectArray:
                self.type = ObjectType.OBJECT_ARRAY
            elif valueType is ObjectElement:
                self.type = ObjectType.OBJECT_ELEMENT
            elif valueType is ObjectField:
                self.type = value.getType()
                self.value = value.getValue()
            elif valueType is IValue:
                self.type = ObjectType._values[ObjectType._keys.index(str(value.getType()))]
                self.value = value.getValue()
            elif valueType is str or valueType is unicode:
                self.type = ObjectType.STRING
            elif valueType is bytearray or valueType is bytes:
                self.type = ObjectType.BYTES
            elif valueType is bool:
                self.type = ObjectType.BOOLEAN
            elif valueType is int:
                self.type = ObjectType.INTEGER
            elif valueType is long:
                self.type = ObjectType.LONG
            elif valueType is float:
                self.type = ObjectType.DOUBLE
            elif valueType is not None:
                doubleValueFunc = getattr(value, "doubleValue", None)
                if callable(doubleValueFunc):
                    self.type = ObjectType.DOUBLE
                    self.value = doubleValueFunc()
                else:
                    raise ValueError("wrong type {}".format(valueType))
            else:
                raise ValueError("wrong type {}".format(valueType))
        else:
            self.type = typev
            if valueType is ObjectField:
                self.type = value.getType()
                self.value = value.getValue()
            elif valueType is IValue:
                self.type = ObjectType._values[ObjectType._keys.index(str(value.getType()))]
                self.value = value.getValue()

    def getName(self):
        # type: () -> str
        return self.name

    def getType(self):
        # type: () -> ObjectType
        return self.type

    def getValue(self):
        # type: () -> str or bytes or int or long or float or bool or ObjectArray or ObjectElement or None
        return self.value

    def isSimple(self):
        # type: () -> bool
        return ObjectType.OBJECT_ARRAY != self.type and ObjectType.OBJECT_ELEMENT != self.type

    def __str__(self):
        return "%s %s=%r" % (self.type, self.name, self.value)

    def __repr__(self):
        return "%s %s=%r" % (self.type, self.name, self.value)

    def __eq__(self, o):
        if self is o:
            return True
        return o and isinstance(o, ObjectField) and self.type == o.type and self.name == o.name and self.value == o.value

    def __ne__(self, o):
        return not self.__eq__(o)


class ObjectElement(object):
    def __init__(self, fields=None):
        # type: (List[ObjectField]) -> None
        if fields is not None:
            self.fields = list(fields)
        else:
            self.fields = []

    def getFields(self):
        # type: () -> List[ObjectField]
        return self.fields

    def findField(self, name):
        # type: (str) -> Optional[ObjectField]
        for f in self.fields:
            if f.name == name:
                return f
        return None

    def findFieldIgnoreCase(self, name):
        # type: (str) -> Optional[ObjectField]
        name = name.lower()
        for f in self.fields:
            if f.name.lower() == name:
                return f
        return None

    def isSimple(self):
        # type: () -> bool
        isSimple = True
        for field in self.fields:
            if not field.isSimple():
                isSimple = False
                break
        return isSimple

    def __str__(self):
        return "{count=%d, fields=%r}" % (len(self.fields), self.fields)

    def __repr__(self):
        return "{count=%d, fields=%r}" % (len(self.fields), self.fields)

    def __eq__(self, o):
        if self is o:
            return True
        if not o or not isinstance(o, ObjectElement) or len(self.fields) != len(o.fields):
            return False
        result = True
        for f in self.fields:
            if o.findField(f.name) != f:
                result = False
                break
        return result

    def __ne__(self, o):
        return not self.__eq__(o)


class ObjectArray(object):
    def __init__(self, typev=ObjectType.OBJECT_ELEMENT, objects=None):
        # type: (ObjectType, List[object]) -> None
        self.type = typev
        self.objects = []
        if objects is not None:
            for obj in objects:
                self.add(obj)

    def check(self, obj, valueType=None):
        # type: (object, type) -> None
        if obj is None:
            raise ValueError("obj is None")
        if valueType is None:
            valueType = type(obj)
        if self.type == ObjectType.OBJECT_ARRAY:
            if valueType is not ObjectArray:
                raise ValueError("wrong obj type")
        elif self.type == ObjectType.OBJECT_ELEMENT:
            if valueType is not ObjectElement:
                raise ValueError("wrong obj type")
        elif self.type == ObjectType.VALUE_ANY:
            if valueType is not str and valueType is not unicode and valueType is not bytearray and valueType is not bytes and valueType is not int and valueType is not long and valueType is not float and valueType is not bool:
                raise ValueError("wrong obj type")
        elif self.type == ObjectType.STRING:
            if valueType is not str or valueType is not unicode:  # not isinstance(obj, basestring)
                raise ValueError("wrong obj type")
        elif self.type == ObjectType.BYTES:
            if valueType is not bytearray or valueType is not bytes:
                raise ValueError("wrong obj type")
        elif self.type == ObjectType.BYTE or self.type == ObjectType.SHORT or self.type == ObjectType.INTEGER:
            if valueType is not int:
                raise ValueError("wrong obj type")
        elif self.type == ObjectType.LONG:
            if valueType is not long:
                raise ValueError("wrong obj type")
        elif self.type == ObjectType.FLOAT or self.type == ObjectType.DOUBLE:
            if valueType is not float:
                raise ValueError("wrong obj type")
        elif self.type == ObjectType.BOOLEAN:
            if valueType is not bool:
                raise ValueError("wrong obj type")
        else:
            raise ValueError("wrong obj type")

    def size(self):
        # type: () -> int
        return len(self.objects)

    def get(self, id):
        # type: (int) -> object
        return self.objects[id]

    def add(self, obj):
        # type: (object) -> None
        valueType = type(obj)
        if valueType is ObjectField:
            obj = obj.getValue()
        elif valueType is IValue:
            obj = obj.getValue()
        self.check(obj, valueType)
        self.objects.append(obj)

    def set(self, id, obj):
        # type: (int, object) -> None
        valueType = type(obj)
        if valueType is ObjectField:
            obj = obj.getValue()
        elif valueType is IValue:
            obj = obj.getValue()
        self.check(obj)
        self.objects[id] = obj

    def remove(self, id):
        # type: (int) -> None
        del self.objects[id]

    def getType(self):
        # type: () -> ObjectType
        return self.type

    def isSimple(self):
        # type: () -> bool
        return ObjectType.OBJECT_ARRAY != self.type and ObjectType.OBJECT_ELEMENT != self.type

    def __str__(self):
        return "[size=%d, objects=%r, type=%s]" % (len(self.objects), self.objects, self.type)

    def __repr__(self):
        return "[size=%d, objects=%r, type=%s]" % (len(self.objects), self.objects, self.type)

    def __eq__(self, o):
        if self is o:
            return True
        return o and isinstance(o, ObjectArray) and self.type == o.type and self.objects == o.objects

    def __ne__(self, o):
        return not self.__eq__(o)


class CFGIModule:
    """Interface for Module"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getName(self):
        # type: () -> str
        """get name"""
        pass

    @abstractmethod
    def countTypes(self):
        # type: () -> int
        """count types"""
        pass

    @abstractmethod
    def getTypeName(self, typeId):
        # type: (int) -> str
        """
        get type name

        :param int typeId:      serial number in the list of types
        """
        pass

    @abstractmethod
    def getMinCountSources(self, typeId):
        # type: (int) -> int
        """get minimum count sources

        :param int typeId:      serial number in the list of types
        """
        pass

    @abstractmethod
    def getMaxCountSources(self, typeId):
        # type: (int) -> int
        """get maximum count sources

        :param int typeId:      serial number in the list of types
        """
        pass

    @abstractmethod
    def getMinCountExecutionContexts(self, typeId):
        # type: (int) -> int
        """get minimum count execution contexts

        :param int typeId:      serial number in the list of types
        """
        pass

    @abstractmethod
    def getMaxCountExecutionContexts(self, typeId):
        # type: (int) -> int
        """get maximum count execution contexts

        :param int typeId:      serial number in the list of types
        """
        pass

    @abstractmethod
    def getMinCountManagedConfigurations(self, typeId):
        # type: (int) -> int
        """get minimum count managed configurations

        :param int typeId:      serial number in the list of types
        """
        pass

    @abstractmethod
    def getMaxCountManagedConfigurations(self, typeId):
        # type: (int) -> int
        """get maximum count managed configurations

        :param int typeId:      serial number in the list of types
        """
        pass


class CFGIContainer:
    """Interface for Container"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getName(self):
        # type: () -> str
        """get name"""
        pass

    @abstractmethod
    def isEnable(self):
        # type: () -> bool
        """is work"""
        pass


class CFGIContainerManaged(CFGIContainer):
    """Interface for Managed Container"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def countConfigurations(self):
        # type: () -> int
        """
        count child configurations
        """
        pass

    @abstractmethod
    def getConfiguration(self, id):
        # type: (int) -> Optional[CFGIConfiguration]
        """
        get child configuration

        :param int id:         serial number in the list of child configurations
        :returns:
            - CFGIConfiguration - if exist
            - None - if not find
        """
        pass

    @abstractmethod
    def countManagedConfigurations(self):
        # type: () -> int
        """
        count child managed configurations
        """
        pass

    @abstractmethod
    def getManagedConfiguration(self, id):
        # type: (int) -> Optional[CFGIConfigurationManaged]
        """
        get child managed configuration

        :param int id:         serial number in the list of child managed configurations
        :returns:
            - CFGIConfigurationManaged - if exist
            - None - if not find
        """
        pass

    @abstractmethod
    def countContainers(self):
        # type: () -> int
        """
        count child containers
        """
        pass

    @abstractmethod
    def getContainer(self, id):
        # type: (int) -> Optional[CFGIContainer]
        """
        get child container

        :param int id:         serial number in the list of child containers
        :returns:
            - CFGIContainer - if exist
            - None - if not find
        """
        pass

    @abstractmethod
    def createContainer(self, name):
        # type: (str) -> CFGIContainerManaged
        """
        create child container

        :param str name:        unique name for container
        """
        pass

    @abstractmethod
    def removeContainer(self, id):
        # type: (int) -> None
        """
        delete empty child container

        :param int id:          serial number in the list of child containers
        """
        pass


class CFGISourceFilter:
    """Interface for Source filter"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getType(self):
        # type: () -> SourceFilterType
        """get type of filter."""
        pass

    @abstractmethod
    def countParams(self):
        # type: () -> int
        """
        count params
        """
        pass

    @abstractmethod
    def getParam(self, id):
        # type: (int) -> Optional[object]
        """
        get param
        params may have any types, depends on the SourceFilterType and id

        :param int id:         serial number in the list of filter params
        :returns:
            - POSITION: Array[int] (n*2 elements: from - inclusive and to - exclusive for range or position and null), int (period length, if greater than zero, then defines the set within which the previous list values apply), int (count periods, determines the number of periods), int (start offset, before the first period)
            - NUMBER: float (min, inclusive), float (max, inclusive)
            - STRING_EQUAL: boolean (type, if true then need equals, also, not equal), string (value for compare)
            - STRING_CONTAIN: boolean (type, if true then need contain, also, not contain), string (value)
        """
        pass


class CFGISource:
    """Interface for Source"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getType(self):
        # type: () -> SourceType
        """get type of source."""
        pass

    @abstractmethod
    def countParams(self):
        # type: () -> int
        """
        count params
        """
        pass

    @abstractmethod
    def getParam(self, id):
        # type: (int) -> Optional[object]
        """
        get param
        params may have any types, depends on the SourceType and id

        :param int id:         serial number in the list of source params
        :returns:
            - MODULE_CONFIGURATION: CFGIConfiguration configuration (source), SourceGetType getType (type of get commands from source), int countLast (only for SourceGetType.LAST. minimum 1), boolean eventDriven (is event driven)
            - EXECUTION_CONTEXT: CFGIExecutionContext executionContext (source), SourceGetType getType (type of get commands from source), int countLast (only for SourceGetType.LAST. minimum 1), boolean eventDriven (is event driven)
            - STATIC_VALUE: IValue (str, number, bytes, bool, ObjectArray)
            - MULTIPART: null
            - CALLER_RELATIVE_NAME: string (caller level cfg name)
        """
        pass

    @abstractmethod
    def countFilters(self):
        # type: () -> int
        """
        count filters
        """
        pass

    @abstractmethod
    def getFilter(self, id):
        # type: (int) -> Optional[CFGISourceFilter]
        """
        get filter

        :param int id:         serial number in the list of Filters
        :returns: CFGISourceFilter
        """
        pass


class CFGISourceManaged(CFGISource):
    """Interface for Managed Source"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def createFilterPosition(self, range, period=0, countPeriods=0, startOffset=0, forObject=False):
        # type: (List[int], int, int, int, bool) -> CFGISourceFilter
        """
        Create position filter and bind it to this source
        add filter to end of current list (order = max_order + 1)
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param List[int] range:     n*2 elements: from - inclusive and to - exclusive for range or position and null
        :param int period:          period length, if greater than zero, then defines the set within which the previous list values apply
        :param int countPeriods:    determines the number of periods
        :param int startOffset:     before the first period
        :param bool forObject:      if true - used for ObjectArrays, overwise for all values
        """
        pass

    @abstractmethod
    def createFilterNumber(self, min, max, fieldName=None):
        # type: (int, int, str) -> CFGISourceFilter
        """
        Create number filter and bind it to this source
        add filter to end of current list (order = max_order + 1)
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param int min:             inclusive
        :param int max:             inclusive
        :param str fieldName:       field name in ObjectArray. if empty used for simple values, overwise for ObjectArrays.
        """
        pass

    @abstractmethod
    def createFilterStrEq(self, needEquals, value, fieldName=None):
        # type: (bool, str, str) -> CFGISourceFilter
        """
        Create string equal filter and bind it to this source
        add filter to end of current list (order = max_order + 1)
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param bool needEquals:     if true then need equals, also, not equal
        :param str value:           value for compare
        :param str fieldName:       field name in ObjectArray. if empty used for simple values, overwise for ObjectArrays.
        """
        pass

    @abstractmethod
    def createFilterStrContain(self, needContain, value, fieldName=None):
        # type: (bool, str, str) -> CFGISourceFilter
        """
        Create string contain filter and bind it to this source
        add filter to end of current list (order = max_order + 1)
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param bool needContain:    if true then need equals, also, not equal
        :param str value:           value for compare
        :param str fieldName:       field name in ObjectArray. if empty used for simple values, overwise for ObjectArrays.
        """
        pass

    @abstractmethod
    def createFilterObjectPaths(self, paths):
        # type: (List[str]) -> CFGISourceFilter
        """
        Create string contain filter and bind it to this source
        add filter to end of current list (order = max_order + 1)
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param List[str] paths:     object array paths. path - dot separated names.
        """
        pass

    @abstractmethod
    def updateFilterPosition(self, id, range, period=0, countPeriods=0, startOffset=0, forObject=False):
        # type: (int, List[int], int, int, int, bool) -> CFGISourceFilter
        """
        Update Position filter in list
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param int id:              serial number in the list
        :param List[int] range:     n*2 elements: from - inclusive and to - exclusive for range or position and null
        :param int period:          period length, if greater than zero, then defines the set within which the previous list values apply
        :param int countPeriods:    determines the number of periods
        :param int startOffset:     before the first period
        :param bool forObject:      if true - used for ObjectArrays, overwise for all values
        """
        pass

    @abstractmethod
    def updateFilterNumber(self, id, min, max, fieldName=None):
        # type: (int, int, int, str) -> CFGISourceFilter
        """
        Update Number filter in list
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param int id:              serial number in the list
        :param int min:             inclusive
        :param int max:             inclusive
        :param str fieldName:       field name in ObjectArray. if empty used for simple values, overwise for ObjectArrays.
        """
        pass

    @abstractmethod
    def updateFilterStrEq(self, id, needEquals, value, fieldName=None):
        # type: (int, bool, str, str) -> CFGISourceFilter
        """
        Update Str Eq filter in list
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param int id:              serial number in the list
        :param bool needEquals:     if true then need equals, also, not equal
        :param str value:           value for compare
        :param str fieldName:       field name in ObjectArray. if empty used for simple values, overwise for ObjectArrays.
        """
        pass

    @abstractmethod
    def updateFilterStrContain(self, id, needContain, value, fieldName=None):
        # type: (int, bool, str, str) -> CFGISourceFilter
        """
        Update Str Contain filter in list
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param int id:              serial number in the list
        :param bool needContain:    if true then need equals, also, not equal
        :param str value:           value for compare
        :param str fieldName:       field name in ObjectArray. if empty used for simple values, overwise for ObjectArrays.
        """
        pass

    @abstractmethod
    def updateFilterObjectPaths(self, id, paths):
        # type: (int, List[str]) -> CFGISourceFilter
        """
        Update Object Paths filter in list
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param int id:              serial number in the list
        :param List[str] paths:     object array paths. path - dot separated names.
        """
        pass

    @abstractmethod
    def removeFilter(self, id):
        # type: (int) -> None
        """
        remove filter from list

        :param int id:          serial number in the list of filters
        """
        pass


class CFGISourceList:
    """Interface for Source multipart"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def countSource(self):
        # type: () -> int
        """
        count sources
        """
        pass

    @abstractmethod
    def getSource(self, id):
        # type: (int) -> Optional[CFGISource]
        """
        get source

        :param int id:          serial number in the list of sources
        :returns:
            - CFGISource - if exist
            - None - if not find
        """
        pass


class CFGISourceListManaged(CFGISourceList):
    """Interface for Managed Source multipart"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def createSourceConfiguration(self, configuration, getType=SourceGetType.NEW, countLast=1, eventDriven=False):
        # type: (CFGIConfiguration, SourceGetType, int, bool) -> CFGISourceManaged
        """
        create source and bind it to this execution context
        add source to end of current list (order = max_order + 1)
        created ContextSourceType is MODULE_CONFIGURATION

        :param CFGIConfiguration configuration: configuration source.
        :param SourceGetType getType:   type of get commands from source.  default NEW.
        :param int countLast:   only for ContextSourceGetType.LAST. minimum 1. default 1.
        :param bool eventDriven:   if true, then source is event driven. default is false.
        """
        pass

    @abstractmethod
    def createSourceExecutionContext(self, executionContext, getType=SourceGetType.NEW, countLast=1, eventDriven=False):
        # type: (CFGIExecutionContext, SourceGetType, int, bool) -> CFGISourceManaged
        """
        create source and bind it to this execution context
        add source to end of current list (order = max_order + 1)
        created ContextSourceType is EXECUTION_CONTEXT

        :param CFGIExecutionContext executionContext: execution context source.
        :param SourceGetType getType:   type of get commands from source.  default NEW.
        :param int countLast:   only for ContextSourceGetType.LAST. minimum 1. default 1.
        :param bool eventDriven:   if true, then source is event driven. default is false.
        """
        pass

    @abstractmethod
    def createSourceValue(self, value):
        # type: (object) -> CFGISourceManaged
        """
        create source and bind it to this execution context
        add source to end of current list (order = max_order + 1)
        created ContextSourceType is STATIC_VALUE

        :param object value:    str, number, bytes, bool, ObjectArray.
        """
        pass

    @abstractmethod
    def createSource(self):
        # type: () -> CFGISourceManaged
        """
        create source and bind it to this execution context
        add source to end of list (order = max_order + 1)
        created ContextSourceType is MULTIPART
        """
        pass

    @abstractmethod
    def createSourceObjectArray(self, value, fields):
        # type: (ObjectArray, List[str]) -> CFGISourceManaged
        """
        create source and bind it to this execution context
        add source to end of current list (order = max_order + 1)
        created ContextSourceType is OBJECT_ARRAY

        :param ObjectArray value: value.
        :param List[str] fields: list of field (comma separated list of paths).
        """
        pass

    @abstractmethod
    def updateSourceConfiguration(self, id, configuration, getType=SourceGetType.NEW, countLast=1, eventDriven=False):
        # type: (int, CFGIConfiguration, SourceGetType, int, bool) -> CFGISourceManaged
        """
        update source
        ContextSourceType is MODULE_CONFIGURATION

        :param int id:          serial number in the list of sources
        :param CFGIConfiguration configuration: configuration source.
        :param SourceGetType getType:   type of get commands from source.  default NEW.
        :param int countLast:   only for ContextSourceGetType.LAST. minimum 1. default 1.
        :param bool eventDriven:   if true, then source is event driven. default is false.
        """
        pass

    @abstractmethod
    def updateSourceExecutionContext(self, id, executionContext, getType=SourceGetType.NEW, countLast=1, eventDriven=False):
        # type: (int, CFGIExecutionContext, SourceGetType, int, bool) -> CFGISourceManaged
        """
        update source
        ContextSourceType is EXECUTION_CONTEXT

        :param int id:          serial number in the list of sources
        :param CFGIExecutionContext executionContext: execution context source.
        :param SourceGetType getType:   type of get commands from source.  default NEW.
        :param int countLast:   only for ContextSourceGetType.LAST. minimum 1. default 1.
        :param bool eventDriven:   if true, then source is event driven. default is false.
        """
        pass

    @abstractmethod
    def updateSourceValue(self, id, value):
        # type: (int, object) -> CFGISourceManaged
        """
        update source
        ContextSourceType is OBJECT_ARRAY

        :param int id:          serial number in the list of sources
        :param object value:    str, number, bytes, bool, ObjectArray.
        """
        pass

    @abstractmethod
    def updateSourceObjectArray(self, id, value, fields):
        # type: (int, ObjectArray, List[str]) -> CFGISourceManaged
        """
        update source
        ContextSourceType is STATIC_VALUE

        :param int id:          serial number in the list of sources
        :param ObjectArray value: value.
        :param List[str] fields: list of field (comma separated list of paths).
        """
        pass

    @abstractmethod
    def removeSource(self, id):
        # type: (int) -> None
        """
        remove source from list

        :param int id:          serial number in the list of sources
        """
        pass

    @abstractmethod
    def getSourceListManaged(self, id):
        # type: (int) -> Optional[CFGISourceListManaged]
        """
        get managed source list

        :param int id:          serial number in the list of sources
        :returns:
            - CFGISourceListManaged - if exist
            - None - if not find
        """
        pass

    @abstractmethod
    def getSourceManaged(self, id):
        # type: (int) -> Optional[CFGISourceManaged]
        """
        get managed source

        :param int id:          serial number in the list of sources
        :returns:
            - CFGISourceManaged - if exist
            - None - if not find
        """
        pass


class CFGIConfiguration:
    """Interface for Module Configuration"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getModule(self):
        # type: () -> CFGIModule
        """get module"""
        pass

    @abstractmethod
    def getName(self):
        # type: () -> str
        """get name"""
        pass

    @abstractmethod
    def getDescription(self):
        # type: () -> str
        """get description"""
        pass

    @abstractmethod
    def getAllSettings(self):
        # type: () -> Dict[str, IValue]
        """
        get all settings
        """
        pass

    @abstractmethod
    def getSetting(self, key):
        # type: (str) -> Optional[IValue]
        """
        get setting value

        :param str key:         setting name
        :returns:
            - str or bytes or int or long or float - if exist
            - None - if not find
        """
        pass

    @abstractmethod
    def getAllVariables(self):
        # type: () -> Dict[str, IValue]
        """
        get all variables
        """
        pass

    @abstractmethod
    def getVariable(self, key):
        # type: (str) -> Optional[IValue]
        """
        get variable value

        :param str key:         variable name
        :returns:
            - str or bytes or int or long or float - if exist
            - None - if not find
        """
        pass

    @abstractmethod
    def getBufferSize(self):
        # type: () -> int
        """get buffer size"""
        pass

    @abstractmethod
    def getThreadBufferSize(self):
        # type: () -> int
        """get thread buffer size"""
        pass

    @abstractmethod
    def isEnable(self):
        # type: () -> bool
        """is work"""
        pass

    @abstractmethod
    def isActive(self):
        # type: () -> bool
        """check is configuration work now (process execute any commands)"""
        pass


class CFGIExecutionContext(CFGISourceList):
    """Interface for Execution Context"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getConfiguration(self):
        # type: () -> CFGIConfiguration
        """get configuration"""
        pass

    @abstractmethod
    def getName(self):
        # type: () -> str
        """get name"""
        pass

    @abstractmethod
    def getMaxWorkInterval(self):
        # type: () -> int
        """
        get max work interval in milliseconds
        if -1, no time limit
        """
        pass

    @abstractmethod
    def isEnable(self):
        # type: () -> bool
        """is work"""
        pass

    @abstractmethod
    def isActive(self):
        # type: () -> bool
        """check is context work now (execute any command)"""
        pass

    @abstractmethod
    def getType(self):
        # type: () -> str
        """
        get type
        unique for configuration

        :returns: type or empty for default/any type
        """
        pass


class CFGIExecutionContextManaged(CFGIExecutionContext, CFGISourceListManaged):
    """Interface for Managed Execution Context"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def setName(self, name):
        # type: (str) -> None
        """
        change name

        :param str name:        unique name for configuration
        """
        pass

    @abstractmethod
    def setMaxWorkInterval(self, maxWorkInterval):
        # type: (int) -> None
        """
        change max work interval

        :param int maxWorkInterval: if -1, no time limit. in milliseconds
        """
        pass

    @abstractmethod
    def setEnable(self, enable):
        # type: (bool) -> None
        """
        enable or disable

        :param bool enable:     true for enable
        """
        pass

    @abstractmethod
    def countExecutionContexts(self):
        # type: () -> int
        """
        count execution contexts
        """
        pass

    @abstractmethod
    def getExecutionContext(self, id):
        # type: (int) -> Optional[CFGIExecutionContext]
        """
        get execution context

        :param int id:          serial number in the list of Execution Contexts
        :returns:
            - CFGIExecutionContext - if exist
            - None - if not find
        """
        pass

    @abstractmethod
    def insertExecutionContext(self, id, executionContext):
        # type: (int, CFGIExecutionContext) -> None
        """
        insert execution context in list
        Shifts the element currently at that position (if any) and any subsequent elements to the right (adds one to their indices).

        :param int id:          serial number in the list of Execution Contexts
        :param CFGIExecutionContext executionContext:   execution context
        """
        pass

    @abstractmethod
    def updateExecutionContext(self, id, executionContext):
        # type: (int, CFGIExecutionContext) -> None
        """
        update execution context in list

        :param int id:          serial number in the list of Execution Contexts
        :param CFGIExecutionContext executionContext:   execution context
        """
        pass

    @abstractmethod
    def removeExecutionContext(self, id):
        # type: (int) -> None
        """
        remove execution context from list

        :param int id:          serial number in the list of Execution Contexts
        """
        pass

    @abstractmethod
    def countManagedConfigurations(self):
        # type: () -> int
        """
        count managed configurations
        """
        pass

    @abstractmethod
    def getManagedConfiguration(self, id):
        # type: (int) -> Optional[CFGIConfiguration]
        """
        get managed configuration

        :param int id:          serial number in the list of Managed configurations
        :returns:
            - CFGIConfiguration - if exist
            - None - if not find
       """
        pass

    @abstractmethod
    def insertManagedConfiguration(self, id, configuration):
        # type: (int, CFGIConfiguration) -> None
        """
        insert configuration in list
        Shifts the element currently at that position (if any) and any subsequent elements to the right (adds one to their indices).

        :param int id:          serial number in the list of Managed configurations
        :param CFGIConfiguration configuration: configuration
        """
        pass

    @abstractmethod
    def updateManagedConfiguration(self, id, configuration):
        # type: (int, CFGIConfiguration) -> None
        """
        update configuration in list

        :param int id:          serial number in the list of Managed configurations
        :param CFGIConfiguration configuration: configuration
        """
        pass

    @abstractmethod
    def removeManagedConfiguration(self, id):
        # type: (int) -> None
        """
        remove configuration from list

        :param int id:          serial number in the list of Managed configurations
        """
        pass

    @abstractmethod
    def setType(self, type):
        # type: (str) -> None
        """
        change type

        :param str type:        type name or empty for default/any type (if exist)
        """
        pass


class CFGIConfigurationManaged(CFGIConfiguration):
    """Interface for Managed Module Configuration"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def setName(self, name):
        # type: (str) -> None
        """
        change name

        :param str name:        unique name for container
        """
        pass

    @abstractmethod
    def setSetting(self, key, value):
        # type: (str, object) -> None
        """
        change setting

        :param str key:         setting name
        :param object value:    value object (str, number, bytes, bool, ObjectArray)
        """
        pass

    @abstractmethod
    def setVariable(self, key, value):
        # type: (str, object) -> None
        """
        change variable

        :param str key:         variable name
        :param object value:    value object (str, number, bytes, bool, ObjectArray)
        """
        pass

    @abstractmethod
    def removeVariable(self, key):
        # type: (str) -> None
        """
        remove variable

        :param str key:         variable name
        """
        pass

    @abstractmethod
    def setBufferSize(self, bufferSize):
        # type: (int) -> None
        """
        change buffer size

        :param int bufferSize:  0 is minimum
        """
        pass

    @abstractmethod
    def setThreadBufferSize(self, threadBufferSize):
        # type: (int) -> None
        """
        change thread buffer size

        :param int threadBufferSize:  1 is minimum
        """
        pass

    @abstractmethod
    def setEnable(self, enable):
        # type: (bool) -> None
        """
        enable or disable

        :param bool enable:     true for enable
        """
        pass

    @abstractmethod
    def countExecutionContexts(self):
        # type: () -> int
        """
        count execution contexts
        """
        pass

    @abstractmethod
    def getExecutionContext(self, id):
        # type: (int) -> Optional[CFGIExecutionContextManaged]
        """
        get execution context

        :param int id:         serial number in the list of Execution Contexts
        :returns:
            - CFGIExecutionContextManaged - if exist
            - None - if not find
        """
        pass

    @abstractmethod
    def createExecutionContext(self, name, type, maxWorkInterval=-1):
        # type: (str, str, int) -> CFGIExecutionContextManaged
        """
        create execution context and bind it to this configuration

        :param str name:        unique name for configuration
        :param str type:        ec type
        :param int maxWorkInterval: max work interval. if -1, no time limit. in milliseconds. default is -1
        """
        pass

    @abstractmethod
    def updateExecutionContext(self, id, name, type, maxWorkInterval=-1):
        # type: (int, str, str, int) -> CFGIExecutionContextManaged
        """
        update execution context

        :param int id:              serial number in the list of Execution Contexts
        :param str name:            unique name for configuration
        :param str type:            ec type
        :param int maxWorkInterval: max work interval. if -1, no time limit. in milliseconds. default is -1
        """
        pass

    @abstractmethod
    def removeExecutionContext(self, id):
        # type: (int) -> None
        """
        delete execution context

        :param int id:          serial number in the list of Execution Contexts
        """
        pass

    @abstractmethod
    def getContainer(self):
        # type: () -> CFGIContainerManaged
        """
        get container
        """
        pass


class FileTool:
    """tool for work with unmodifiable files"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getName(self):
        # type: () -> str
        """get name"""
        pass

    @abstractmethod
    def exists(self):
        # type: () -> bool
        """is file exist"""
        pass

    @abstractmethod
    def isDirectory(self):
        # type: () -> bool
        """is directory"""
        pass

    @abstractmethod
    def getChildrens(self):
        # type: () -> List[FileTool]
        """get files in folder"""
        pass

    @abstractmethod
    def getBytes(self):
        # type: () -> bytes
        """reed all file"""
        pass

    @abstractmethod
    def length(self):
        # type: () -> int
        """file size"""
        pass


class Module:
    """Main module interface"""

    __metaclass__ = ABCMeta

    # @classmethod
    @abstractmethod
    def start(self, configurationTool):
        # type: (ConfigurationTool) -> None
        """
        call once per process on start

        :param ConfigurationTool configurationTool: configuration tool
        :raise ModuleException: main exception
        """
        pass

    # @classmethod
    @abstractmethod
    def process(self, configurationTool, executionContextTool):
        # type: (ConfigurationTool, ExecutionContextTool) -> None
        """
        main method. call every time when need execute

        :param ConfigurationTool configurationTool: configuration tool
        :param ExecutionContextTool executionContextTool: execution context tool
        :raise ModuleException: main exception
        """
        pass

    # @classmethod
    @abstractmethod
    def update(self, configurationTool):
        # type: (ConfigurationTool) -> None
        """
        call then need update

        :param ConfigurationTool configurationTool: configuration tool
        :raise ModuleException: main exception
        """
        pass

    # @classmethod
    @abstractmethod
    def stop(self, configurationTool):
        # type: (ConfigurationTool) -> None
        """
        call once per process on stop

        :param ConfigurationTool configurationTool: configuration tool
        :raise ModuleException: main exception
        """
        pass


class ConfigurationTool(CFGIConfiguration):
    """main configuration tool"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def setVariable(self, key, value):
        # type: (str, object) -> None
        """
        change variable

        :param str key:                         variable name
        :param str or bytes or int or long or float value:   value object ()
        """
        pass

    @abstractmethod
    def isVariableChanged(self, key):
        # type: (str) -> bool
        """check is variable has changed from last execution or last check
        usfull for check changes from external (processes or user)

        :param str key:         variable name
        """
        pass

    @abstractmethod
    def removeVariable(self, key):
        # type: (str) -> IValue
        """remove variable

        :param str key:         variable name
        """
        pass

    @abstractmethod
    def getHomeFolder(self):
        # type: () -> FileTool
        """get module folder
        contains all files, what was in smcm file"""
        pass

    @abstractmethod
    def getWorkDirectory(self):
        # type: () -> str
        """get full path to work directory
        only if module allow this"""
        pass

    @abstractmethod
    def countExecutionContexts(self):
        # type: () -> int
        """
        count execution contexts
        """
        pass

    @abstractmethod
    def getExecutionContext(self, id):
        # type: (int) -> Optional[CFGIExecutionContext]
        """
        get execution context

        :param int id:         serial number in the list of Execution Contexts
        :returns:
            - CFGIExecutionContext - if exist
            - None - if not find
        """
        pass

    @abstractmethod
    def getContainer(self):
        # type: () -> CFGIContainerManaged
        """
        get container
        """
        pass

    @abstractmethod
    def loggerTrace(self, text):
        # type: (str) -> None
        """
        logger trace

        :param int text:         text
        """
        pass

    @abstractmethod
    def loggerDebug(self, text):
        # type: (str) -> None
        """
        logger debug

        :param int text:         text
        """
        pass

    @abstractmethod
    def loggerInfo(self, text):
        # type: (str) -> None
        """
        logger info

        :param int text:         text
        """
        pass

    @abstractmethod
    def loggerWarn(self, text):
        # type: (str) -> None
        """
        logger warn

        :param int text:         text
        """
        pass

    @abstractmethod
    def loggerError(self, text):
        # type: (str) -> None
        """
        logger error

        :param int text:         text
        """
        pass

    @abstractmethod
    def getInfo(self, key):
        # type: (str) -> Optional[IValue]
        """
        get info by key

        :param str key:         key name
        :returns:
            - str or bytes or int or long or float - if exist
            - None - if not find
        """
        pass


class ConfigurationControlTool:
    """Tool for work with managed configurations"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getModules(self):
        # type: () -> List[CFGIModule]
        """list of all installed modules"""
        pass

    @abstractmethod
    def countManagedConfigurations(self):
        # type: () -> int
        """count managed configurations"""
        pass

    @abstractmethod
    def getManagedConfiguration(self, id):
        # type: (int) -> Optional[CFGIConfigurationManaged]
        """
        get managed configuration

        :param int id:          serial number in the list of Managed configurations
        :returns:
            - CFGIConfigurationManaged - if exist
            - None - if not find
        """
        pass

    @abstractmethod
    def createConfiguration(self, id, container, module, name):
        # type: (int, CFGIContainer, CFGIModule, str) -> CFGIConfigurationManaged
        """
        create configuration and add it in list of managed configurations

        :param int id:                  index at which the specified element is to be inserted
        :param CFGIContainer container: container
        :param CFGIModule module:       module
        :param str name:                unique name for configuration
        """
        pass

    @abstractmethod
    def removeManagedConfiguration(self, id):
        # type: (int) -> None
        """
        remove managed configuration

        :param int id:          serial number in the list of Managed configurations
        """
        pass


class FlowControlTool:
    """Tool for throw new command to managed execution contexts and get result"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def countManagedExecutionContexts(self):
        # type: () -> int
        """count managed execution contexts"""
        pass

    @abstractmethod
    def executeNow(self, type, managedId, values):
        # type: (CommandType, int, List[object]) -> None
        """
        throw new command to managed execution context
        command execute in this thread
        function will wait for the command to execute

        :param CommandType type:           type of command
        :param int managedId:              serial number in the list of Managed execution contexts
        :param list values:                list of values for create dummy messages from this process, or null
        """
        pass

    @abstractmethod
    def executeParallel(self, type, managedIds, values, waitingTacts=0, maxWorkInterval=-1):
        # type: (CommandType, List[int], List[object], int, int) -> long
        """
        throw new command to managed execution context
        command execute in new thread
        function return control immediately

        :param CommandType type:           type of command
        :param list managedIds:            list of serial numbers in the list of Managed execution contexts
        :param list values:                list of values for create dummy messages from this process, or null
        :param int waitingTacts:           if it is necessary that the new thread first wait for the specified time (in tacts)
        :param int maxWorkInterval:        define max work interval of new thread (in tacts)

        return id of thread
        """
        pass

    @abstractmethod
    def isThreadActive(self, threadId):
        # type: (long) -> bool
        """
        check is thread alive

        :param long threadId:               id thread
        """
        pass

    @abstractmethod
    def getMessagesFromExecuted(self, threadId=0, managedId=0):
        # type: (long, int) -> List[IAction]
        """
        get data from managed execution context
        who receive commands from this process

        :param long threadId:               id thread. if 0 then using data from current thread
        :param int managedId:              serial number in the list of Managed execution contexts

        return only DATA messages
        """
        pass

    @abstractmethod
    def getCommandsFromExecuted(self, threadId=0, managedId=0):
        # type: (long, int) -> List[ICommand]
        """
        work as getMessagesFromExecuted

        :param long threadId:               id thread. if 0 then using data from current thread
        :param int managedId:              serial number in the list of Managed execution contexts

        return commands
        """
        pass

    @abstractmethod
    def releaseThread(self, threadId):
        # type: (long) -> None
        """
        after executeParallel and work with him, need to release thread
        if thread work - not stop it

        :param long threadId:               id thread
        """
        pass

    @abstractmethod
    def releaseThreadCache(self, threadId):
        # type: (long) -> None
        """
        after executeParallel and work with him, need to release thread

        :param long threadId:               id thread
        """
        pass

    @abstractmethod
    def getManagedExecutionContext(self, id):
        # type: (int) -> Optional[CFGIExecutionContext]
        """
        get managed execution context

        :param int id:                     serial number in the list of Managed execution contexts

        return CFGIExecutionContext or None
        """
        pass


class ExecutionContextTool(CFGIExecutionContext):
    """main execution context tool"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def addMessage(self, value):
        # type: (object) -> None
        """
        emit message

        :param object value:    object (str, number, bytes, bool, ObjectArray)
        """
        pass

    @abstractmethod
    def addError(self, value):
        # type: (object) -> None
        """
        emit error message

        :param object value:    object (str, number, bytes, bool, ObjectArray)
        """
        pass

    @abstractmethod
    def addLog(self, value):
        # type: (str) -> None
        """
        emit log message

        :param string value:    string
        """
        pass

    @abstractmethod
    def countCommands(self, sourceId):
        # type: (int) -> int
        """
        get count commands in source

        :param int sourceId     serial number in the list of Sources
        """
        pass

    @abstractmethod
    def countCommandsFromExecutionContext(self, executionContext):
        # type: (CFGIExecutionContextManaged) -> int
        """
        get count commands (all) for managed execution context

        :param CFGIExecutionContextManaged executionContext:    managed execution context
        """
        pass

    @abstractmethod
    def getMessages(self, sourceId, fromIndex=-1, toIndex=-1):
        # type: (int, int, int) -> List[IAction]
        """
        get Process Actions from source (only DATA messages)
        Returns a view of the portion of this list between the specified fromIndex, inclusive, and toIndex, exclusive.

        :param int sourceId     serial number in the list of Sources
        :param int fromIndex    start serial number in the list of commands in source (exclusive). if -1 then get all
        :param int toIndex      end serial number in the list of commands in source (inclusive). if -1 then get all
        """
        pass

    @abstractmethod
    def getCommands(self, sourceId, fromIndex=-1, toIndex=-1):
        # type: (int, int, int) -> List[ICommand]
        """
        get Commands from source
        Returns a view of the portion of this list between the specified fromIndex, inclusive, and toIndex, exclusive.

        :param int sourceId     serial number in the list of Sources
        :param int fromIndex    start serial number in the list of commands in source (exclusive). if -1 then get all
        :param int toIndex      end serial number in the list of commands in source (inclusive). if -1 then get all
        """
        pass

    @abstractmethod
    def getCommandsFromExecutionContext(self, executionContext, fromIndex=-1, toIndex=-1):
        # type: (CFGIExecutionContextManaged, int, int) -> List[ICommand]
        """
        get Commands from managed execution context
        Returns a view of the portion of this list between the specified fromIndex, inclusive, and toIndex, exclusive.

        :param CFGIExecutionContextManaged executionContext:    managed execution context
        :param int fromIndex:   start serial number in the list of commands in source (exclusive). if -1 then get all
        :param int toIndex:     end serial number in the list of commands in source (inclusive). if -1 then get all
        """
        pass

    @abstractmethod
    def isError(self, action):
        # type: (IAction) -> bool
        """
        is Process Actions has errors

        :param IAction action: action
        """
        pass

    @abstractmethod
    def getConfigurationControlTool(self):
        # type: () -> ConfigurationControlTool
        """get tool for work with managed configurations"""
        pass

    @abstractmethod
    def getFlowControlTool(self):
        # type: () -> FlowControlTool
        """get tool for throw new command to managed execution contexts and get result"""
        pass

    @abstractmethod
    def isNeedStop(self):
        # type: () -> bool
        """check is need stop process work immediately
        usefull for long work (example - web server)"""
        pass
