
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name="eltechstorage"
    account_key="IyFO9uWTEjD05LlPBuScWLarIzjQFOfVDH7MNbK+s3V+cMANHvVeP6h5cZ8Vln9c5qwUJcPvZoDF+AStY8dFRA=="
    azure_container="media"
    expiration_specs=None

class AzureStaticStorage(AzureStorage):
    account_name = 'eltechstorage' # Must be replaced by your storage_account_name
    account_key = "IyFO9uWTEjD05LlPBuScWLarIzjQFOfVDH7MNbK+s3V+cMANHvVeP6h5cZ8Vln9c5qwUJcPvZoDF+AStY8dFRA==" # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None