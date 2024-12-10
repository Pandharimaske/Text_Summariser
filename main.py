from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "DATA INGESTION"

try:
    logger.info(f"{STAGE_NAME} stage Initiated")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} stage Completed")

except Exception as e:
    logger.exception(e)
    raise e
