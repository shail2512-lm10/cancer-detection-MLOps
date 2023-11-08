from CancerDetection import logger
from CancerDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CancerDetection.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"------ {STAGE_NAME} has started ------- ")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"------ {STAGE_NAME} completed -------\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"************")
    logger.info(f"------- {STAGE_NAME} has started --------")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f"------- {STAGE_NAME} completed -------\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e