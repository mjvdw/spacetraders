import typing_extensions

from spacetraders.paths import PathValues
from spacetraders.apis.paths. import 
from spacetraders.apis.paths.register import Register
from spacetraders.apis.paths.systems import Systems
from spacetraders.apis.paths.systems_system_symbol import SystemsSystemSymbol
from spacetraders.apis.paths.systems_system_symbol_waypoints import SystemsSystemSymbolWaypoints
from spacetraders.apis.paths.systems_system_symbol_waypoints_waypoint_symbol import SystemsSystemSymbolWaypointsWaypointSymbol
from spacetraders.apis.paths.systems_system_symbol_waypoints_waypoint_symbol_market import SystemsSystemSymbolWaypointsWaypointSymbolMarket
from spacetraders.apis.paths.systems_system_symbol_waypoints_waypoint_symbol_shipyard import SystemsSystemSymbolWaypointsWaypointSymbolShipyard
from spacetraders.apis.paths.systems_system_symbol_waypoints_waypoint_symbol_jump_gate import SystemsSystemSymbolWaypointsWaypointSymbolJumpGate
from spacetraders.apis.paths.factions import Factions
from spacetraders.apis.paths.factions_faction_symbol import FactionsFactionSymbol
from spacetraders.apis.paths.my_agent import MyAgent
from spacetraders.apis.paths.my_contracts import MyContracts
from spacetraders.apis.paths.my_contracts_contract_id import MyContractsContractId
from spacetraders.apis.paths.my_contracts_contract_id_accept import MyContractsContractIdAccept
from spacetraders.apis.paths.my_contracts_contract_id_deliver import MyContractsContractIdDeliver
from spacetraders.apis.paths.my_contracts_contract_id_fulfill import MyContractsContractIdFulfill
from spacetraders.apis.paths.my_ships import MyShips
from spacetraders.apis.paths.my_ships_ship_symbol import MyShipsShipSymbol
from spacetraders.apis.paths.my_ships_ship_symbol_cargo import MyShipsShipSymbolCargo
from spacetraders.apis.paths.my_ships_ship_symbol_orbit import MyShipsShipSymbolOrbit
from spacetraders.apis.paths.my_ships_ship_symbol_refine import MyShipsShipSymbolRefine
from spacetraders.apis.paths.my_ships_ship_symbol_chart import MyShipsShipSymbolChart
from spacetraders.apis.paths.my_ships_ship_symbol_cooldown import MyShipsShipSymbolCooldown
from spacetraders.apis.paths.my_ships_ship_symbol_dock import MyShipsShipSymbolDock
from spacetraders.apis.paths.my_ships_ship_symbol_survey import MyShipsShipSymbolSurvey
from spacetraders.apis.paths.my_ships_ship_symbol_extract import MyShipsShipSymbolExtract
from spacetraders.apis.paths.my_ships_ship_symbol_jettison import MyShipsShipSymbolJettison
from spacetraders.apis.paths.my_ships_ship_symbol_jump import MyShipsShipSymbolJump
from spacetraders.apis.paths.my_ships_ship_symbol_navigate import MyShipsShipSymbolNavigate
from spacetraders.apis.paths.my_ships_ship_symbol_nav import MyShipsShipSymbolNav
from spacetraders.apis.paths.my_ships_ship_symbol_warp import MyShipsShipSymbolWarp
from spacetraders.apis.paths.my_ships_ship_symbol_sell import MyShipsShipSymbolSell
from spacetraders.apis.paths.my_ships_ship_symbol_scan_systems import MyShipsShipSymbolScanSystems
from spacetraders.apis.paths.my_ships_ship_symbol_scan_waypoints import MyShipsShipSymbolScanWaypoints
from spacetraders.apis.paths.my_ships_ship_symbol_scan_ships import MyShipsShipSymbolScanShips
from spacetraders.apis.paths.my_ships_ship_symbol_refuel import MyShipsShipSymbolRefuel
from spacetraders.apis.paths.my_ships_ship_symbol_purchase import MyShipsShipSymbolPurchase
from spacetraders.apis.paths.my_ships_ship_symbol_transfer import MyShipsShipSymbolTransfer
from spacetraders.apis.paths.my_ships_ship_symbol_negotiate_contract import MyShipsShipSymbolNegotiateContract

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
