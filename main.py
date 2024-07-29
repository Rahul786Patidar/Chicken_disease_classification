from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingpipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingpipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingpipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========")
except Exception as e:
        logger.exception (e)
        raise e




STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"********************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingpipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========")
except Exception as e:
        logger.exception (e)
        raise e