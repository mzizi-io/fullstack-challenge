from src.core.search import Search
import pytest


@pytest.mark.asyncio(scope="session")
async def test_get(session):
    res = await Search().get(session=session, page=1, per_page=10)
    res_json = res.model_dump()
    assert res_json["assets"][0]["pin"] == 17083150310000
    assert res_json["assets"][1]["pin"] == 17173240300000
    assert res_json["assets"][2]["pin"] == 17173240160000
    assert res_json["assets"][3]["pin"] == 17173240170000
    assert res_json["assets"][4]["pin"] == 17173240180000
    assert res_json["assets"][5]["pin"] == 17173160420000
    assert res_json["assets"][6]["pin"] == 17171230450000
    assert res_json["assets"][7]["pin"] == 17173240190000
    assert res_json["assets"][8]["pin"] == 17173160430000


@pytest.mark.asyncio(scope="session")
async def test_distinct_values(session):
    res = await Search().get_distinct_values(session=session, field="rec_type")
    assert len(res) == 1
