from pipeline_utils import PipelineCreator
country = 'CO'
pipeline = 'base_pop'

## Test 1
# if config file already exists:
pipeline = PipelineCreator(country=country, configs=pipeline)
pipeline.execute()

## Test 2
# if config file does not exist:
# country is necceary to create the config file and validate the pipeline
pipeline = PipelineCreator(country=country)
# a new or a testing config can be appended to the pipeline
conf = {
  'pipeline': 'anotherpipe',
  'country': 'CO',
  'status': True,
  'parameters': {
    'ap1': 'a_new_schema',
    'ap2': 'a_table',
    'ap3': 'smthg'
  }
}
pipeline.append_config(conf)
pipeline.execute()
# We can save the configs on the configs folder as a YAML file
pipeline.save_configs(filepath='test')
# print(pipeline.pipeline_info)
