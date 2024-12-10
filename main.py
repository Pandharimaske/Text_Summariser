from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.textSummarizer.pipeline.model_trainer_pipeline import ModelTrainerPipeline


STAGE_NAME = "DATA INGESTION"

try:
    logger.info(f"{STAGE_NAME} stage Initiated")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} stage Completed")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "DATA TRANSFORMATION"

try:
    logger.info(f"{STAGE_NAME} stage Initiated")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"{STAGE_NAME} stage Completed")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "MODEL TRAINER"

try:
    logger.info(f"{STAGE_NAME} stage Initiated")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_training()
    logger.info(f"{STAGE_NAME} stage Completed")

except Exception as e:
    logger.exception(e)
    raise e


