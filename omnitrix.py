import sys
from loguru import logger

logger.remove()

logger.add(
    sys.stderr,
    format="<green>[OMNITRIX]</green> | <level>{level: <10}</level> | <level>{message}</level>",
    level="DEBUG"
)

class OmnitrixLogger:
    @staticmethod
    def relogiocarregado(msg):
        logger.success(f"{msg}")

    @staticmethod
    def transformacao(alien, msg="Transformação Concluída"):
        logger.info(f"[{alien.upper()}] - {msg}")

    @staticmethod
    def relogiodescarregando(msg="Energia diminuindo..."):
        logger.warning(f"{msg}")

    @staticmethod
    def relogiorecarga(msg="Modo de Recarga Ativado."):
        logger.error(f"{msg}")

    @staticmethod
    def autodestruicao(msg="Código de Autodestruição Iniciado!"):
        logger.critical(f"{msg}")

#omnitrix = OmnitrixLogger()

#omnitrix.relogiocarregado("Dispositivo online. DNA Primordial sincronizado.")
#omnitrix.transformacao("Chama", "Soltando fogo pelas mãos!")
#omnitrix.relogiodescarregando("Aviso: Tempo limite de transformação se aproximando (Restam 60s).")
#omnitrix.relogiorecarga("Omnitrix descarregou. Aguarde 10 minutos para reiniciar.")
#omnitrix.autodestruicao("Protocolo S3-E1 executado por Azmuth.")