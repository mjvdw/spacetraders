import typing_extensions

from spacetraders.apis.tags import TagValues
from spacetraders.apis.tags.factions_api import FactionsApi
from spacetraders.apis.tags.fleet_api import FleetApi
from spacetraders.apis.tags.contracts_api import ContractsApi
from spacetraders.apis.tags.systems_api import SystemsApi
from spacetraders.apis.tags.agents_api import AgentsApi
from spacetraders.apis.tags.default_api import DefaultApi

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
