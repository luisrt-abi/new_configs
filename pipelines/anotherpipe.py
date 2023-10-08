from pydantic import BaseModel, ConfigDict
from datetime import date


class AnotherPipeParameters(BaseModel):
    ap1: str
    ap2: str
    ap3: str
    model_config = ConfigDict(extra='forbid')


class AnotherPipe:
    def __init__(self, parameters: AnotherPipeParameters, run_date=date) -> None:
        self.parameters = parameters
        self.country = None
        self.run_date = run_date
        pass

    def execute(self):
        print('anotherpipe executed', self.parameters, self.country)
        pass


class AnotherPipeMX(AnotherPipe):
    def __init__(self, parameters: dict, run_date: date ) -> None:
        super().__init__(parameters=parameters, run_date=run_date)
        self.country = 'MX'
        pass


class AnotherPipeCO(AnotherPipe):
    def __init__(self, parameters: dict, run_date: date) -> None:
        super().__init__(parameters=parameters, run_date=run_date)
        self.country = 'CO'
        pass
