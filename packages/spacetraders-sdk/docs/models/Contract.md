# spacetraders.models.contract.Contract

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**terms** | [**ContractTerms**](ContractTerms.md) | [**ContractTerms**](ContractTerms.md) |  | 
**factionSymbol** | str,  | str,  | The symbol of the faction that this contract is for. | 
**fulfilled** | bool,  | BoolClass,  | Whether the contract has been fulfilled | if omitted the server will use the default value of False
**accepted** | bool,  | BoolClass,  | Whether the contract has been accepted by the agent | if omitted the server will use the default value of False
**expiration** | str, datetime,  | str,  | Deprecated in favor of deadlineToAccept | value must conform to RFC-3339 date-time
**id** | str,  | str,  |  | 
**type** | str,  | str,  |  | must be one of ["PROCUREMENT", "TRANSPORT", "SHUTTLE", ] 
**deadlineToAccept** | str, datetime,  | str,  | The time at which the contract is no longer available to be accepted | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

