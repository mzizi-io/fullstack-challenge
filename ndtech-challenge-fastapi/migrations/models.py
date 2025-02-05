from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    BIGINT,
    Column,
    DateTime,
    Float,
    Integer,
    String,
    Text,
    func
)

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


class Assets(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_address = Column(String(255), nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    zip_code = Column(Integer, nullable=False)
    rec_type = Column(String(255), nullable=False)
    pin = Column(BIGINT, nullable=False)
    ovacls = Column(Integer, nullable=False)
    class_description = Column(Text, nullable=False)
    current_land = Column(Integer, nullable=False)
    current_building = Column(Integer, nullable=False)
    current_total = Column(Integer, nullable=False)
    estimated_market_value = Column(Integer, nullable=False)
    prior_land = Column(Integer, nullable=False)
    prior_building = Column(Integer, nullable=False)
    prior_total = Column(Integer, nullable=False)
    pprior_land = Column(Integer, nullable=False)
    pprior_building = Column(Integer, nullable=False)
    pprior_total = Column(Integer, nullable=False)
    pprior_year = Column(Integer, nullable=False)
    town = Column(Integer, nullable=False)
    volume = Column(Integer, nullable=False)
    loc = Column(String(20), nullable=False)
    tax_code = Column(Integer, nullable=False)
    neighborhood = Column(Integer, nullable=False)
    houseno = Column(Integer, nullable=False)
    direction = Column(String(3), nullable=False)
    street = Column(String(20), nullable=False)
    suffix = Column(String(5), nullable=False)
    apt = Column(String(10), nullable=True)
    city = Column(String(20), nullable=False)
    res_type = Column(String(255), nullable=True)
    bldg_use = Column(String(255), nullable=True)
    apt_desc = Column(Integer, nullable=True)
    comm_units = Column(Integer, nullable=True)
    ext_desc = Column(String(50), nullable=True)
    full_bath = Column(Integer, nullable=True)
    half_bath = Column(Integer, nullable=True)
    bsmt_desc = Column(String(50), nullable=True)
    attic_desc = Column(String(50), nullable=True)
    ac = Column(Integer, nullable=True)
    fireplace = Column(Integer, nullable=True)
    gar_desc = Column(String(50), nullable=True)
    age = Column(Integer, nullable=True)
    building_sq_ft = Column(Integer, nullable=True)
    land_sq_ft = Column(Integer, nullable=True)
    bldg_sf = Column(Integer, nullable=True)
    units_tot = Column(Integer, nullable=True)
    multi_sale = Column(Integer, nullable=True)
    deed_type = Column(Integer, nullable=True)
    sale_date = Column(DateTime, nullable=True)
    sale_amount = Column(Integer, nullable=True)
    appcnt = Column(Integer, nullable=True)
    appeal_a = Column(Integer, nullable=True)
    appeal_a_status = Column(String(100), nullable=True)
    appeal_a_result = Column(String(100), nullable=True)
    appeal_a_reason = Column(Integer, nullable=True)
    appeal_a_pin_result = Column(String(100), nullable=True)
    appeal_a_propav = Column(Integer, nullable=True)
    appeal_a_currav = Column(Integer, nullable=True)
    appeal_a_resltdate = Column(DateTime, nullable=True)
