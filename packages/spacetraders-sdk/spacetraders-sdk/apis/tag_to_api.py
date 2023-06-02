import typing_extensions

from spacetraders-sdk.apis.tags import TagValues
from spacetraders-sdk.apis.tags.factions_api import FactionsApi
from spacetraders-sdk.apis.tags.fleet_api import FleetApi
from spacetraders-sdk.apis.tags.contracts_api import ContractsApi
from spacetraders-sdk.apis.tags.systems_api import SystemsApi
from spacetraders-sdk.apis.tags.agents_api import AgentsApi
from spacetraders-sdk.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.FACTIONS: FactionsApi,
        TagValues.FLEET: FleetApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.SYSTEMS: SystemsApi,
        TagValues.AGENTS: AgentsApi,
        TagValues.DEFAULT: DefaultApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.FACTIONS: FactionsApi,
        TagValues.FLEET: FleetApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.SYSTEMS: SystemsApi,
        TagValues.AGENTS: AgentsApi,
        TagValues.DEFAULT: DefaultApi,
    }
)
