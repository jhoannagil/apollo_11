from dataclasses import dataclass

@dataclass
class Mission:

    name: str
    date: str
    device_type : str
    device_status: str
    
    def __init__(self) -> None:
        self.__name: str = None
        self.__date: str = None
        self.__device_type: str = None
        self.__device_status: str = None

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name:str) -> None:
        self.__name = name
    
    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date:str) -> None:
        self.__date = date

    @property
    def device_type(self) -> str:
        return self.__device_type

    @device_type.setter
    def device_type(self, device_type:str) -> None:
        self.__device_type = device_type

    @property
    def device_status(self) -> str:
        return self.__device_status

    @device_status.setter
    def device_status(self, device_status:str) -> None:
        self.__device_status = device_status
    
