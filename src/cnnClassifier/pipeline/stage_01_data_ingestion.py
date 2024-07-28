from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger


STAGE_NAME = "Data Ingestion stage"

<<<<<<< HEAD
class DataIngestionTrainingPipeline:
=======
class DataIngestionTrainingpipeline:
>>>>>>> 53e3e44 (data ingestion completed)
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
<<<<<<< HEAD
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x")
    except Exception as e:

         logger.exception(e)
         raise e
=======
        obj = DataIngestionTrainingpipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========")
    except Exception as e:
        logger.exception (e)
        raise e
>>>>>>> 53e3e44 (data ingestion completed)
