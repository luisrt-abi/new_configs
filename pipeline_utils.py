import yaml
from pydantic import BaseModel
from enum import Enum
import importlib
from functools import cached_property
from datetime import date


class Country(Enum):
    MX = 'MX'
    CO = 'CO'


class pipeline_names(str, Enum):
    BasePOP = 'base_pop'
    OtherPipe = 'otherpipe'
    AnotherPipe = 'anotherpipe'


class Pipeline(BaseModel):
    pipeline: pipeline_names
    country: Country
    status: bool
    parameters: dict


class PipelineCreator:
    def __init__(self, country, configs=None):
        self.country = Country(country).value
        self.configs = configs
        self.run_date = date.today()

    @cached_property
    def raw_info(self):
        config = []
        if self.configs:
            config = self.fetch_configs()
        return config

    @property
    def pipeline_info(self):
        config = [self.__load_config(conf) for conf in self.raw_info]
        return config

    def fetch_configs(self):
        path = 'configs/' + self.country + '/' + self.configs + '.yaml'
        config = self.read_yaml(path)
        return config

    def active_pipelines(self, pipeline):
        active = [pipe for pipe in pipeline if pipe.status]
        assert len(active) > 0, 'No active pipelines'
        assert all([self.country == pipe.country.value for pipe in active]), 'Country mismatch'
        return active

    def read_yaml(self, file_path: str) -> list:
        with open(file_path, 'r') as stream:
            config = yaml.safe_load(stream)
        return config

    def __load_config(self, config: dict):
        return Pipeline(**config)

    def append_config(self, config: dict):
        assert isinstance(config, dict), 'config must be a dict'
        self.raw_info.append(config)

    def __load_pipeline(self, pipeline: Pipeline):
        pipelinemod = str(pipeline.pipeline.name)
        loading_class = f"{pipelinemod}{pipeline.country.value}"
        loading_module = f"pipelines.{pipeline.pipeline.value}"
        print(f"loading {loading_class} from {loading_module}")
        imported_module = importlib.import_module(f'{loading_module}')
        cls = getattr(imported_module, f'{loading_class}')
        prms = getattr(imported_module, f'{pipelinemod}Parameters')
        prms = prms(**pipeline.parameters)
        cls = cls(parameters=prms, run_date=self.run_date)
        return cls

    def get_pipeline(self):
        pipeline = self.active_pipelines(self.pipeline_info)
        pipeline = [self.__load_pipeline(conf) for conf in pipeline]
        return pipeline

    def execute(self):
        pipeline = self.get_pipeline()
        for pipe in pipeline:
            pipe.execute()

    def save_configs(self, filepath: str):
        info = self.raw_info
        with open(f'configs/{self.country}/{filepath}_{self.run_date}.yml', 'w') as yaml_file:
            yaml.dump(info, yaml_file)
