import pytest
from loguru import logger
from omnitrix import OmnitrixLogger

@pytest.fixture(autouse=True)
def caplog_loguru(caplog):
    handler_id = logger.add(caplog.handler, format="{message}", level="DEBUG")
    yield caplog
    logger.remove(handler_id)

def test_omnitrix_logger_outputs(caplog_loguru):
    omnitrix = OmnitrixLogger()

    # Testa a transformação
    omnitrix.transformacao("Chama", "Soltando fogo pelas mãos!")
    assert "[CHAMA] - Soltando fogo pelas mãos!" in caplog_loguru.text
    assert caplog_loguru.records[-1].levelname == "INFO"


