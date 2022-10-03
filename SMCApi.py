import datetime

from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import List, Dict, Optional


class ModuleException(Exception):
    """main exception"""

    def __init__(self, text):
        super(ModuleException, self).__init__(text)
        self.txt = text


class ActionType(Enum):
    __order__ = 'START EXECUTE UPDATE STOP'
    START = 0
    EXECUTE = 1
    UPDATE = 2
    STOP = 3


class CommandType(Enum):
    __order__ = 'START EXECUTE UPDATE STOP'
    START = 0
    EXECUTE = 1
    UPDATE = 2
    STOP = 3


class MessageType(Enum):
    MESSAGE_PROCESS_STATE_CHANGE = 1

    MESSAGE_ACTION_START = 4
    MESSAGE_ACTION_STOP = 6
    MESSAGE_ACTION_ERROR = 7

    MESSAGE_CONFIGURATION_CONTROL_CONFIGURATION_SETTING_UPDATE = 108
    MESSAGE_CONFIGURATION_CONTROL_CONFIGURATION_VARIABLE_UPDATE = 109
    MESSAGE_CONFIGURATION_CONTROL_CONFIGURATION_VARIABLE_REMOVE = 110
    MESSAGE_CONFIGURATION_CONTROL_CONFIGURATION_CREATE = 111
    MESSAGE_CONFIGURATION_CONTROL_CONFIGURATION_UPDATE = 112
    MESSAGE_CONFIGURATION_CONTROL_CONFIGURATION_REMOVE = 113
    MESSAGE_CONFIGURATION_CONTROL_EXECUTION_CONTEXT_CREATE = 114
    MESSAGE_CONFIGURATION_CONTROL_EXECUTION_CONTEXT_UPDATE = 115
    MESSAGE_CONFIGURATION_CONTROL_EXECUTION_CONTEXT_REMOVE = 116
    MESSAGE_CONFIGURATION_CONTROL_SOURCE_CONTEXT_CREATE = 117
    MESSAGE_CONFIGURATION_CONTROL_SOURCE_CONTEXT_UPDATE = 118
    MESSAGE_CONFIGURATION_CONTROL_SOURCE_CONTEXT_REMOVE = 119
    MESSAGE_CONFIGURATION_CONTROL_CONTAINER_CREATE = 120
    MESSAGE_CONFIGURATION_CONTROL_CONTAINER_REMOVE = 121

    MESSAGE_FLOW_CONTROL_EXECUTE_NOW_START = 220
    MESSAGE_FLOW_CONTROL_EXECUTE_NOW_EXECUTE = 221
    MESSAGE_FLOW_CONTROL_EXECUTE_NOW_UPDATE = 222
    MESSAGE_FLOW_CONTROL_EXECUTE_NOW_STOP = 223
    MESSAGE_FLOW_CONTROL_EXECUTE_PARALLEL_START = 224
    MESSAGE_FLOW_CONTROL_EXECUTE_PARALLEL_EXECUTE = 225
    MESSAGE_FLOW_CONTROL_EXECUTE_PARALLEL_UPDATE = 226
    MESSAGE_FLOW_CONTROL_EXECUTE_PARALLEL_STOP = 227
    MESSAGE_FLOW_CONTROL_EXECUTE_PARALLEL_WAITING_TACTS = 228

    MESSAGE_ERROR_TYPE = 1000
    MESSAGE_DATA = 1001


class ValueType(Enum):
    __order__ = 'STRING BYTE SHORT INTEGER LONG BIG_INTEGER FLOAT DOUBLE BIG_DECIMAL BYTES'
    STRING = 0
    BYTE = 1
    SHORT = 2
    INTEGER = 3
    LONG = 4
    BIG_INTEGER = 5
    FLOAT = 6
    DOUBLE = 7
    BIG_DECIMAL = 8
    BYTES = 9


class SourceType(Enum):
    __order__ = 'MODULE_CONFIGURATION EXECUTION_CONTEXT STATIC_VALUE MULTIPART CALLER CALLER_RELATIVE_NAME'
    MODULE_CONFIGURATION = 0
    EXECUTION_CONTEXT = 1
    STATIC_VALUE = 2
    MULTIPART = 3
    CALLER = 4
    CALLER_RELATIVE_NAME = 5


class SourceGetType(Enum):
    __order__ = 'ALL NEW NEW_ALL LAST LAST_ALL'
    ALL = 0
    NEW = 1
    NEW_ALL = 2
    LAST = 3
    LAST_ALL = 4


class SourceFilterType(Enum):
    __order__ = 'POSITION NUMBER STRING_EQUAL STRING_CONTAIN'
    POSITION = 0
    NUMBER = 1
    STRING_EQUAL = 2
    STRING_CONTAIN = 3


class INumber:
    """Interface for number object"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def intValue(self):
        # type: () -> int
        """to int type value"""
        pass

    @abstractmethod
    def longValue(self):
        # type: () -> long
        """to long type value"""
        pass

    @abstractmethod
    def floatValue(self):
        # type: () -> float
        """to float type value"""
        pass


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
        # type: () -> str or bytes or INumber
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


class CFGIModule:
    """Interface for Module"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getName(self):
        # type: () -> str
        """get name"""
        pass

    @abstractmethod
    def getMinCountSources(self):
        # type: () -> int
        """get minimum count sources"""
        pass

    @abstractmethod
    def getMaxCountSources(self):
        # type: () -> int
        """get maximum count sources"""
        pass

    @abstractmethod
    def getMinCountExecutionContexts(self):
        # type: () -> int
        """get minimum count execution contexts"""
        pass

    @abstractmethod
    def getMaxCountExecutionContexts(self):
        # type: () -> int
        """get maximum count execution contexts"""
        pass

    @abstractmethod
    def getMinCountManagedConfigurations(self):
        # type: () -> int
        """get minimum count managed configurations"""
        pass

    @abstractmethod
    def getMaxCountManagedConfigurations(self):
        # type: () -> int
        """get maximum count managed configurations"""
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
        # type: () -> Dict[str, str or bytes or INumber]
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
            - str or bytes or INumber - if exist
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
            - str or bytes or INumber - if exist
            - None - if not find
        """
        pass

    @abstractmethod
    def getBufferSize(self):
        # type: () -> int
        """get buffer size"""
        pass

    @abstractmethod
    def isEnable(self):
        # type: () -> bool
        """is work"""
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
        :param object value:    value object (string, number, bytes)
        """
        pass

    @abstractmethod
    def setVariable(self, key, value):
        # type: (str, object) -> None
        """
        change variable

        :param str key:         variable name
        :param str or bytes or INumber value:    value object
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

        :param int bufferSize:  1 is minimum
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
    def createExecutionContext(self, name, maxWorkInterval=-1):
        # type: (str, int) -> CFGIExecutionContextManaged
        """
        create execution context and bind it to this configuration

        :param str name:        unique name for configuration
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

        :param object value: str, number or byte array.
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
    def removeManagedConfiguration(self, id):
        # type: (int) -> None
        """
        remove configuration from list

        :param int id:          serial number in the list of Managed configurations
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
        # type: (int) -> object
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
        # type: (int) -> object
        """
        get param
        params may have any types, depends on the SourceType and id

        :param int id:         serial number in the list of source params
        :returns:
            - MODULE_CONFIGURATION: CFGIConfiguration configuration (source), SourceGetType getType (type of get commands from source), int countLast (only for SourceGetType.LAST. minimum 1), boolean eventDriven (is event driven)
            - EXECUTION_CONTEXT: CFGIExecutionContext executionContext (source), SourceGetType getType (type of get commands from source), int countLast (only for SourceGetType.LAST. minimum 1), boolean eventDriven (is event driven)
            - STATIC_VALUE: IValue (String, Number or byte array)
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
    def createFilterPosition(self, range, period=0, countPeriods=0, startOffset=0):
        # type: (List[int], int, int, int) -> CFGISourceFilter
        """
        Create position filter and bind it to this source
        add filter to end of current list (order = max_order + 1)
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param List[int] range:     n*2 elements: from - inclusive and to - exclusive for range or position and null
        :param int period:          period length, if greater than zero, then defines the set within which the previous list values apply
        :param int countPeriods:    determines the number of periods
        :param int startOffset:     before the first period
        """
        pass

    @abstractmethod
    def createFilterNumber(self, min, max):
        # type: (int, int) -> CFGISourceFilter
        """
        Create number filter and bind it to this source
        add filter to end of current list (order = max_order + 1)
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param int min:    inclusive
        :param int max:    inclusive
        """
        pass

    @abstractmethod
    def createFilterStrEq(self, needEquals, value):
        # type: (bool, str) -> CFGISourceFilter
        """
        Create string equal filter and bind it to this source
        add filter to end of current list (order = max_order + 1)
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param bool needEquals:     if true then need equals, also, not equal
        :param str value:           value for compare
        """
        pass

    @abstractmethod
    def createFilterStrContain(self, needContain, value):
        # type: (bool, str) -> CFGISourceFilter
        """
        Create string contain filter and bind it to this source
        add filter to end of current list (order = max_order + 1)
        only for MODULE_CONFIGURATION and EXECUTION_CONTEXT SourceType

        :param bool needContain:    if true then need equals, also, not equal
        :param str value:           value for compare
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
        :param str or bytes or INumber value:   value object ()
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
    def hasLicense(self, freeDays):
        # type: (int) -> bool
        """
        check if has license

        :param int freeDays:         free trial days. 0 or more.
        :returns bool - true if has license
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

        :param object value:    object (string, number, bytes)
        """
        pass

    @abstractmethod
    def addError(self, value):
        # type: (object) -> None
        """
        emit error message

        :param object value:    object (string, number, bytes)
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

        type                   type of command
        managedId              serial number in the list of Managed execution contexts
        values                 list of values for create dummy messages from this process, or null
        """
        pass

    @abstractmethod
    def executeParallel(self, type, managedIds, values, waitingTacts=0, maxWorkInterval=-1):
        # type: (CommandType, List[int], List[object], int, int) -> int
        """
        throw new command to managed execution context
        command execute in new thread
        function return control immediately

        type                   type of command
        managedIds             list of serial numbers in the list of Managed execution contexts
        values                 list of values for create dummy messages from this process, or null
        waitingTacts           if it is necessary that the new thread first wait for the specified time (in tacts)
        maxWorkInterval        define max work interval of new thread (in tacts)

        return id of thread
        """
        pass

    @abstractmethod
    def isThreadActive(self, threadId):
        # type: (int) -> int
        """
        check is thread alive

        threadId               id thread
        """
        pass

    @abstractmethod
    def getMessagesFromExecuted(self, threadId=0, managedId=0):
        # type: (int, int) -> List[IAction]
        """
        get data from managed execution context
        who receive commands from this process

        threadId               id thread. if 0 then using data from current thread
        managedId              serial number in the list of Managed execution contexts

        return only DATA messages
        """
        pass

    @abstractmethod
    def getCommandsFromExecuted(self, threadId=0, managedId=0):
        # type: (int, int) -> List[ICommand]
        """
        work as getMessagesFromExecuted

        threadId               id thread. if 0 then using data from current thread
        managedId              serial number in the list of Managed execution contexts

        return commands
        """
        pass

    @abstractmethod
    def releaseThread(self, threadId):
        # type: (int) -> None
        """
        after executeParallel and work with him, need to release thread

        threadId               id thread
        """
        pass

    @abstractmethod
    def getManagedExecutionContext(self, id):
        # type: (int) -> Optional[CFGIExecutionContext]
        """
        get managed execution context

        id                     serial number in the list of Managed execution contexts

        return CFGIExecutionContext or None
        """
        pass
