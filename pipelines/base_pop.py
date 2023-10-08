from pydantic import BaseModel, ConfigDict
from datetime import date


class BasePOPParameters(BaseModel):
    bp1: str
    bp2: str
    bp3: str
    model_config = ConfigDict(extra='forbid')


class BasePOP:
    def __init__(self, parameters: BasePOPParameters, run_date: date) -> None:
        self.parameters = parameters
        self.country = None
        self.run_date = run_date
        pass

    def execute(self):
        print('basepop executed', self.parameters, self.country)
        pass


class BasePOPMX(BasePOP):
    def __init__(self, parameters: BasePOPParameters, run_date: date) -> None:
        super().__init__(parameters=parameters, run_date=run_date)
        self.country = 'MX'
        pass


class BasePOPCO(BasePOP):
    def __init__(self, parameters: BasePOPParameters, run_date: date) -> None:
        super().__init__(parameters=parameters, run_date=run_date)
        self.country = 'CO'
        pass
