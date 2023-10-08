from pydantic import BaseModel, ConfigDict
from datetime import date

class OtherPipeParameters(BaseModel):
    op1: str
    op2: str
    op3: str
    model_config = ConfigDict(extra='forbid')


class OtherPipe:
    def __init__(self, parameters: OtherPipeParameters, run_date: date) -> None:
        self.parameters = parameters
        self.country = None
        self.run_date = run_date
        pass

    def execute(self):
        print('otherpipe executed', self.parameters, self.country)
        pass


class OtherPipeMX(OtherPipe):
    def __init__(self, parameters: OtherPipeParameters, run_date = date) -> None:
        super().__init__(parameters=parameters, run_date=run_date)
        self.country = 'MX'
        pass


class OtherPipeCO(OtherPipe):
    def __init__(self, parameters: dict, run_date: date) -> None:
        super().__init__(parameters=parameters, run_date=run_date)
        self.country = 'CO'
        pass
