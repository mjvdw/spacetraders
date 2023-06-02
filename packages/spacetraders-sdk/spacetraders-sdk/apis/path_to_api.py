import typing_extensions

from spacetraders-sdk.paths import PathValues
from spacetraders-sdk.apis.paths. import 
from spacetraders-sdk.apis.paths.register import Register
from spacetraders-sdk.apis.paths.systems import Systems
from spacetraders-sdk.apis.paths.systems_system_symbol import SystemsSystemSymbol
from spacetraders-sdk.apis.paths.systems_system_symbol_waypoints import SystemsSystemSymbolWaypoints
from spacetraders-sdk.apis.paths.systems_system_symbol_waypoints_waypoint_symbol import SystemsSystemSymbolWaypointsWaypointSymbol
from spacetraders-sdk.apis.paths.systems_system_symbol_waypoints_waypoint_symbol_market import SystemsSystemSymbolWaypointsWaypointSymbolMarket
from spacetraders-sdk.apis.paths.systems_system_symbol_waypoints_waypoint_symbol_shipyard import SystemsSystemSymbolWaypointsWaypointSymbolShipyard
from spacetraders-sdk.apis.paths.systems_system_symbol_waypoints_waypoint_symbol_jump_gate import SystemsSystemSymbolWaypointsWaypointSymbolJumpGate
from spacetraders-sdk.apis.paths.factions import Factions
from spacetraders-sdk.apis.paths.factions_faction_symbol import FactionsFactionSymbol
from spacetraders-sdk.apis.paths.my_agent import MyAgent
from spacetraders-sdk.apis.paths.my_contracts import MyContracts
from spacetraders-sdk.apis.paths.my_contracts_contract_id import MyContractsContractId
from spacetraders-sdk.apis.paths.my_contracts_contract_id_accept import MyContractsContractIdAccept
from spacetraders-sdk.apis.paths.my_contracts_contract_id_deliver import MyContractsContractIdDeliver
from spacetraders-sdk.apis.paths.my_contracts_contract_id_fulfill import MyContractsContractIdFulfill
from spacetraders-sdk.apis.paths.my_ships import MyShips
from spacetraders-sdk.apis.paths.my_ships_ship_symbol import MyShipsShipSymbol
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_cargo import MyShipsShipSymbolCargo
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_orbit import MyShipsShipSymbolOrbit
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_refine import MyShipsShipSymbolRefine
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_chart import MyShipsShipSymbolChart
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_cooldown import MyShipsShipSymbolCooldown
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_dock import MyShipsShipSymbolDock
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_survey import MyShipsShipSymbolSurvey
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_extract import MyShipsShipSymbolExtract
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_jettison import MyShipsShipSymbolJettison
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_jump import MyShipsShipSymbolJump
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_navigate import MyShipsShipSymbolNavigate
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_nav import MyShipsShipSymbolNav
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_warp import MyShipsShipSymbolWarp
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_sell import MyShipsShipSymbolSell
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_scan_systems import MyShipsShipSymbolScanSystems
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_scan_waypoints import MyShipsShipSymbolScanWaypoints
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_scan_ships import MyShipsShipSymbolScanShips
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_refuel import MyShipsShipSymbolRefuel
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_purchase import MyShipsShipSymbolPurchase
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_transfer import MyShipsShipSymbolTransfer
from spacetraders-sdk.apis.paths.my_ships_ship_symbol_negotiate_contract import MyShipsShipSymbolNegotiateContract

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SOLIDUS: ,
        PathValues.REGISTER: Register,
        PathValues.SYSTEMS: Systems,
        PathValues.SYSTEMS_SYSTEM_SYMBOL: SystemsSystemSymbol,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS: SystemsSystemSymbolWaypoints,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL: SystemsSystemSymbolWaypointsWaypointSymbol,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_MARKET: SystemsSystemSymbolWaypointsWaypointSymbolMarket,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_SHIPYARD: SystemsSystemSymbolWaypointsWaypointSymbolShipyard,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_JUMPGATE: SystemsSystemSymbolWaypointsWaypointSymbolJumpGate,
        PathValues.FACTIONS: Factions,
        PathValues.FACTIONS_FACTION_SYMBOL: FactionsFactionSymbol,
        PathValues.MY_AGENT: MyAgent,
        PathValues.MY_CONTRACTS: MyContracts,
        PathValues.MY_CONTRACTS_CONTRACT_ID: MyContractsContractId,
        PathValues.MY_CONTRACTS_CONTRACT_ID_ACCEPT: MyContractsContractIdAccept,
        PathValues.MY_CONTRACTS_CONTRACT_ID_DELIVER: MyContractsContractIdDeliver,
        PathValues.MY_CONTRACTS_CONTRACT_ID_FULFILL: MyContractsContractIdFulfill,
        PathValues.MY_SHIPS: MyShips,
        PathValues.MY_SHIPS_SHIP_SYMBOL: MyShipsShipSymbol,
        PathValues.MY_SHIPS_SHIP_SYMBOL_CARGO: MyShipsShipSymbolCargo,
        PathValues.MY_SHIPS_SHIP_SYMBOL_ORBIT: MyShipsShipSymbolOrbit,
        PathValues.MY_SHIPS_SHIP_SYMBOL_REFINE: MyShipsShipSymbolRefine,
        PathValues.MY_SHIPS_SHIP_SYMBOL_CHART: MyShipsShipSymbolChart,
        PathValues.MY_SHIPS_SHIP_SYMBOL_COOLDOWN: MyShipsShipSymbolCooldown,
        PathValues.MY_SHIPS_SHIP_SYMBOL_DOCK: MyShipsShipSymbolDock,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SURVEY: MyShipsShipSymbolSurvey,
        PathValues.MY_SHIPS_SHIP_SYMBOL_EXTRACT: MyShipsShipSymbolExtract,
        PathValues.MY_SHIPS_SHIP_SYMBOL_JETTISON: MyShipsShipSymbolJettison,
        PathValues.MY_SHIPS_SHIP_SYMBOL_JUMP: MyShipsShipSymbolJump,
        PathValues.MY_SHIPS_SHIP_SYMBOL_NAVIGATE: MyShipsShipSymbolNavigate,
        PathValues.MY_SHIPS_SHIP_SYMBOL_NAV: MyShipsShipSymbolNav,
        PathValues.MY_SHIPS_SHIP_SYMBOL_WARP: MyShipsShipSymbolWarp,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SELL: MyShipsShipSymbolSell,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SCAN_SYSTEMS: MyShipsShipSymbolScanSystems,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SCAN_WAYPOINTS: MyShipsShipSymbolScanWaypoints,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SCAN_SHIPS: MyShipsShipSymbolScanShips,
        PathValues.MY_SHIPS_SHIP_SYMBOL_REFUEL: MyShipsShipSymbolRefuel,
        PathValues.MY_SHIPS_SHIP_SYMBOL_PURCHASE: MyShipsShipSymbolPurchase,
        PathValues.MY_SHIPS_SHIP_SYMBOL_TRANSFER: MyShipsShipSymbolTransfer,
        PathValues.MY_SHIPS_SHIP_SYMBOL_NEGOTIATE_CONTRACT: MyShipsShipSymbolNegotiateContract,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SOLIDUS: ,
        PathValues.REGISTER: Register,
        PathValues.SYSTEMS: Systems,
        PathValues.SYSTEMS_SYSTEM_SYMBOL: SystemsSystemSymbol,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS: SystemsSystemSymbolWaypoints,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL: SystemsSystemSymbolWaypointsWaypointSymbol,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_MARKET: SystemsSystemSymbolWaypointsWaypointSymbolMarket,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_SHIPYARD: SystemsSystemSymbolWaypointsWaypointSymbolShipyard,
        PathValues.SYSTEMS_SYSTEM_SYMBOL_WAYPOINTS_WAYPOINT_SYMBOL_JUMPGATE: SystemsSystemSymbolWaypointsWaypointSymbolJumpGate,
        PathValues.FACTIONS: Factions,
        PathValues.FACTIONS_FACTION_SYMBOL: FactionsFactionSymbol,
        PathValues.MY_AGENT: MyAgent,
        PathValues.MY_CONTRACTS: MyContracts,
        PathValues.MY_CONTRACTS_CONTRACT_ID: MyContractsContractId,
        PathValues.MY_CONTRACTS_CONTRACT_ID_ACCEPT: MyContractsContractIdAccept,
        PathValues.MY_CONTRACTS_CONTRACT_ID_DELIVER: MyContractsContractIdDeliver,
        PathValues.MY_CONTRACTS_CONTRACT_ID_FULFILL: MyContractsContractIdFulfill,
        PathValues.MY_SHIPS: MyShips,
        PathValues.MY_SHIPS_SHIP_SYMBOL: MyShipsShipSymbol,
        PathValues.MY_SHIPS_SHIP_SYMBOL_CARGO: MyShipsShipSymbolCargo,
        PathValues.MY_SHIPS_SHIP_SYMBOL_ORBIT: MyShipsShipSymbolOrbit,
        PathValues.MY_SHIPS_SHIP_SYMBOL_REFINE: MyShipsShipSymbolRefine,
        PathValues.MY_SHIPS_SHIP_SYMBOL_CHART: MyShipsShipSymbolChart,
        PathValues.MY_SHIPS_SHIP_SYMBOL_COOLDOWN: MyShipsShipSymbolCooldown,
        PathValues.MY_SHIPS_SHIP_SYMBOL_DOCK: MyShipsShipSymbolDock,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SURVEY: MyShipsShipSymbolSurvey,
        PathValues.MY_SHIPS_SHIP_SYMBOL_EXTRACT: MyShipsShipSymbolExtract,
        PathValues.MY_SHIPS_SHIP_SYMBOL_JETTISON: MyShipsShipSymbolJettison,
        PathValues.MY_SHIPS_SHIP_SYMBOL_JUMP: MyShipsShipSymbolJump,
        PathValues.MY_SHIPS_SHIP_SYMBOL_NAVIGATE: MyShipsShipSymbolNavigate,
        PathValues.MY_SHIPS_SHIP_SYMBOL_NAV: MyShipsShipSymbolNav,
        PathValues.MY_SHIPS_SHIP_SYMBOL_WARP: MyShipsShipSymbolWarp,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SELL: MyShipsShipSymbolSell,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SCAN_SYSTEMS: MyShipsShipSymbolScanSystems,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SCAN_WAYPOINTS: MyShipsShipSymbolScanWaypoints,
        PathValues.MY_SHIPS_SHIP_SYMBOL_SCAN_SHIPS: MyShipsShipSymbolScanShips,
        PathValues.MY_SHIPS_SHIP_SYMBOL_REFUEL: MyShipsShipSymbolRefuel,
        PathValues.MY_SHIPS_SHIP_SYMBOL_PURCHASE: MyShipsShipSymbolPurchase,
        PathValues.MY_SHIPS_SHIP_SYMBOL_TRANSFER: MyShipsShipSymbolTransfer,
        PathValues.MY_SHIPS_SHIP_SYMBOL_NEGOTIATE_CONTRACT: MyShipsShipSymbolNegotiateContract,
    }
)
