"""Migration - 2025-01-22_00-02-29

Revision ID: 741db123f41e
Revises: 
Create Date: 2025-01-22 00:02:29.797961

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '741db123f41e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_address', sa.String(length=255), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('zip_code', sa.Integer(), nullable=False),
    sa.Column('rec_type', sa.String(length=255), nullable=False),
    sa.Column('pin', sa.Integer(), nullable=False),
    sa.Column('ovacls', sa.Integer(), nullable=False),
    sa.Column('class_description', sa.String(length=255), nullable=False),
    sa.Column('current_land', sa.Integer(), nullable=False),
    sa.Column('current_building', sa.Integer(), nullable=False),
    sa.Column('current_total', sa.Integer(), nullable=False),
    sa.Column('estimated_market_value', sa.Integer(), nullable=False),
    sa.Column('prior_land', sa.Integer(), nullable=False),
    sa.Column('prior_building', sa.Integer(), nullable=False),
    sa.Column('prior_total', sa.Integer(), nullable=False),
    sa.Column('pprior_land', sa.Integer(), nullable=False),
    sa.Column('pprior_building', sa.Integer(), nullable=False),
    sa.Column('pprior_total', sa.Integer(), nullable=False),
    sa.Column('pprior_year', sa.Integer(), nullable=False),
    sa.Column('town', sa.Integer(), nullable=False),
    sa.Column('volume', sa.Integer(), nullable=False),
    sa.Column('loc', sa.String(length=20), nullable=False),
    sa.Column('tax_code', sa.Integer(), nullable=False),
    sa.Column('neighborhood', sa.Integer(), nullable=False),
    sa.Column('houseno', sa.Integer(), nullable=False),
    sa.Column('direction', sa.String(length=3), nullable=False),
    sa.Column('street', sa.String(length=20), nullable=False),
    sa.Column('suffix', sa.String(length=5), nullable=False),
    sa.Column('apt', sa.String(length=10), nullable=True),
    sa.Column('city', sa.String(length=20), nullable=False),
    sa.Column('res_type', sa.String(length=255), nullable=True),
    sa.Column('bldg_use', sa.String(length=255), nullable=True),
    sa.Column('apt_desc', sa.Integer(), nullable=True),
    sa.Column('comm_units', sa.Integer(), nullable=True),
    sa.Column('ext_desc', sa.String(length=50), nullable=True),
    sa.Column('full_bath', sa.Integer(), nullable=True),
    sa.Column('half_bath', sa.Integer(), nullable=True),
    sa.Column('bsmt_desc', sa.String(length=50), nullable=True),
    sa.Column('attic_desc', sa.String(length=50), nullable=True),
    sa.Column('ac', sa.Integer(), nullable=True),
    sa.Column('fireplace', sa.Integer(), nullable=True),
    sa.Column('gar_desc', sa.String(length=50), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('building_sq_ft', sa.Integer(), nullable=True),
    sa.Column('land_sq_ft', sa.Integer(), nullable=True),
    sa.Column('bldg_sf', sa.Integer(), nullable=True),
    sa.Column('units_tot', sa.Integer(), nullable=True),
    sa.Column('multi_sale', sa.Integer(), nullable=True),
    sa.Column('deed_type', sa.Integer(), nullable=True),
    sa.Column('sale_date', sa.DateTime(), nullable=True),
    sa.Column('sale_amount', sa.Integer(), nullable=True),
    sa.Column('appcnt', sa.Integer(), nullable=True),
    sa.Column('appeal_a', sa.Integer(), nullable=True),
    sa.Column('appeal_a_status', sa.String(length=100), nullable=True),
    sa.Column('appeal_a_result', sa.String(length=100), nullable=True),
    sa.Column('appeal_a_reason', sa.Integer(), nullable=True),
    sa.Column('appeal_a_pin_result', sa.String(length=100), nullable=True),
    sa.Column('appeal_a_propav', sa.Integer(), nullable=True),
    sa.Column('appeal_a_currav', sa.Integer(), nullable=True),
    sa.Column('appeal_a_resltdate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('assets')
    # ### end Alembic commands ###
