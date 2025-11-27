import pytest
from weather_api.weather import get_weather

@pytest.mark.asyncio
async def test_get_weather():
    data = await get_weather("London")
    assert "main" in data
    assert "temp" in data["main"]