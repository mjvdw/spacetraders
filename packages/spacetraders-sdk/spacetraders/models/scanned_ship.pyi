# coding: utf-8

"""
    SpaceTraders API

    SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.  The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.  ```json http {   \"method\": \"GET\",   \"url\": \"https://api.spacetraders.io/v2\", } ```  Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.  We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.     # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: joel@spacetraders.io
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from spacetraders import schemas  # noqa: F401


class ScannedShip(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The ship that was scanned. Details include information about the ship that could be detected by the scanner.
    """


    class MetaOapg:
        required = {
            "symbol",
            "nav",
            "engine",
            "registration",
        }
        
        class properties:
            symbol = schemas.StrSchema
        
            @staticmethod
            def registration() -> typing.Type['ShipRegistration']:
                return ShipRegistration
        
            @staticmethod
            def nav() -> typing.Type['ShipNav']:
                return ShipNav
            
            
            class engine(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "symbol",
                    }
                    
                    class properties:
                        symbol = schemas.StrSchema
                        __annotations__ = {
                            "symbol": symbol,
                        }
                
                symbol: MetaOapg.properties.symbol
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    symbol: typing.Union[MetaOapg.properties.symbol, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'engine':
                    return super().__new__(
                        cls,
                        *_args,
                        symbol=symbol,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class frame(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "symbol",
                    }
                    
                    class properties:
                        symbol = schemas.StrSchema
                        __annotations__ = {
                            "symbol": symbol,
                        }
                
                symbol: MetaOapg.properties.symbol
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    symbol: typing.Union[MetaOapg.properties.symbol, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'frame':
                    return super().__new__(
                        cls,
                        *_args,
                        symbol=symbol,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class reactor(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "symbol",
                    }
                    
                    class properties:
                        symbol = schemas.StrSchema
                        __annotations__ = {
                            "symbol": symbol,
                        }
                
                symbol: MetaOapg.properties.symbol
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    symbol: typing.Union[MetaOapg.properties.symbol, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'reactor':
                    return super().__new__(
                        cls,
                        *_args,
                        symbol=symbol,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class mounts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "symbol",
                            }
                            
                            class properties:
                                symbol = schemas.StrSchema
                                __annotations__ = {
                                    "symbol": symbol,
                                }
                        
                        symbol: MetaOapg.properties.symbol
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            symbol: typing.Union[MetaOapg.properties.symbol, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                symbol=symbol,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mounts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "symbol": symbol,
                "registration": registration,
                "nav": nav,
                "engine": engine,
                "frame": frame,
                "reactor": reactor,
                "mounts": mounts,
            }
    
    symbol: MetaOapg.properties.symbol
    nav: 'ShipNav'
    engine: MetaOapg.properties.engine
    registration: 'ShipRegistration'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registration"]) -> 'ShipRegistration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nav"]) -> 'ShipNav': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["engine"]) -> MetaOapg.properties.engine: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frame"]) -> MetaOapg.properties.frame: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reactor"]) -> MetaOapg.properties.reactor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mounts"]) -> MetaOapg.properties.mounts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol", "registration", "nav", "engine", "frame", "reactor", "mounts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registration"]) -> 'ShipRegistration': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nav"]) -> 'ShipNav': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["engine"]) -> MetaOapg.properties.engine: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frame"]) -> typing.Union[MetaOapg.properties.frame, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reactor"]) -> typing.Union[MetaOapg.properties.reactor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mounts"]) -> typing.Union[MetaOapg.properties.mounts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol", "registration", "nav", "engine", "frame", "reactor", "mounts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        nav: 'ShipNav',
        engine: typing.Union[MetaOapg.properties.engine, dict, frozendict.frozendict, ],
        registration: 'ShipRegistration',
        frame: typing.Union[MetaOapg.properties.frame, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        reactor: typing.Union[MetaOapg.properties.reactor, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        mounts: typing.Union[MetaOapg.properties.mounts, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ScannedShip':
        return super().__new__(
            cls,
            *_args,
            symbol=symbol,
            nav=nav,
            engine=engine,
            registration=registration,
            frame=frame,
            reactor=reactor,
            mounts=mounts,
            _configuration=_configuration,
            **kwargs,
        )

from spacetraders.models.ship_nav import ShipNav
from spacetraders.models.ship_registration import ShipRegistration