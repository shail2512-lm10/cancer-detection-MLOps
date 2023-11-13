from CancerDetection import logger
from CancerDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CancerDetection.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from CancerDetection.pipeline.stage_03_model_training import ModelTrainingPipeline
from CancerDetection.pipeline.stage_04_model_evaluation import EvaluationPipeline

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


STAGE_NAME = "Training"
try:
    logger.info(f"*************")
    logger.info(f"------- {STAGE_NAME} has started --------")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"------- {STAGE_NAME} completed -------\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"***********")
    logger.info(f"------- {STAGE_NAME} started --------")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f"------- {STAGE_NAME} completed --------\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e