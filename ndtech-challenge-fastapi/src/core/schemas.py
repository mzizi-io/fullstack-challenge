from pydantic import BaseModel
from typing import List, Union
from enum import Enum
from datetime import date


class SearchTypes(Enum):
    INDEXED_TEXT = "indexed_text"
    SIMILAR_STRING = "similar_string"
    EXACT_STRING = "exact_string"
    RANGE = "range"


class SearchCondition(BaseModel):
    field: str
    value: str
    search_type: SearchTypes


class RangeSearchCondition(BaseModel):
    field: str
    min: float
    max: float
    search_type: SearchTypes = SearchTypes.RANGE


class SearchParams(BaseModel):
    params: List[Union[SearchCondition, RangeSearchCondition]]
    per_page: int
    page: int


class AssetSearchRow(BaseModel):
    id: int
    full_address: str
    longitude: float
    latitude: float
    zip_code: int
    rec_type: str
    pin: int
    ovacls: int
    class_description: str
    current_land: int
    current_building: int
    current_total: int
    estimated_market_value: int
    prior_land: int
    prior_building: int
    prior_total: int
    pprior_land: int
    pprior_building: int
    pprior_total: int
    pprior_year: int

    # Possibly missing fields
    town: Union[int, None]
    volume: Union[int, None]
    loc: Union[str, None]
    tax_code: Union[int, None]
    neighborhood: Union[int, None]
    houseno: Union[int, None]
    direction: Union[str, None]
    street: Union[str, None]
    suffix: Union[str, None]
    apt: Union[str, None]
    city: Union[str, None]
    res_type: Union[str, None]
    bldg_use: Union[str, None]
    apt_desc: Union[int, None]
    comm_units: Union[int, None]
    ext_desc: Union[str, None]
    full_bath: Union[int, None]
    half_bath: Union[int, None]
    bsmt_desc: Union[str, None]
    attic_desc: Union[str, None]
    ac: Union[int, None]
    fireplace: Union[int, None]
    gar_desc: Union[str, None]
    age: Union[int, None]
    building_sq_ft: Union[int, None]
    land_sq_ft: Union[int, None]
    bldg_sf: Union[int, None]
    units_tot: Union[int, None]
    multi_sale: Union[int, None]
    deed_type: Union[int, None]
    sale_date: Union[date, None]
    sale_amount: Union[int, None]
    appcnt: Union[int, None]
    appeal_a: Union[int, None]
    appeal_a_status: Union[str, None]
    appeal_a_result: Union[str, None]
    appeal_a_reason: Union[int, None]
    appeal_a_pin_result: Union[str, None]
    appeal_a_propav: Union[int, None]
    appeal_a_currav: Union[int, None]
    appeal_a_resltdate: Union[date, None]

    class Config:
        from_attributes = True


class AssetSearchResponse(BaseModel):
    assets: List[AssetSearchRow]


class AuthParam(BaseModel):
    pass


class AuthValidResponse(BaseModel):
    pass
