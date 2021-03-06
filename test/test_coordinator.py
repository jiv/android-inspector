# coding=utf-8
import os
import unittest

from components.coordinator import Coordinator
from components.definitions_database_manager import DefinitionsDatabaseManager
from components.extensions_manager import ExtensionsManager
from components.operations_manager import OperationsManager
from components.repositories_manager import RepositoriesManager
from model import DeviceInfo


class TestCoordinator(unittest.TestCase):
    def setUp(self):
        definitions_database = DefinitionsDatabaseManager(os.path.join('test', 'definitions.db'),
                                                          'create_db.sql',
                                                          'insert_default_data_types.sql',
                                                          'insert_default_data_source_types.sql',
                                                          'insert_default_operations.sql')
        repositories_manager = RepositoriesManager('repositories')
        operations_manager = OperationsManager(definitions_database, repositories_manager)
        extensions_manager = ExtensionsManager(definitions_database, repositories_manager)
        self.coordinator = Coordinator(operations_manager, extensions_manager)

    def test_use_case_batch_mode(self):
        ids = ['EmailMessageAOSPEmail']
        device_info = DeviceInfo('5.1', 'XT1053')
        results_dir_path = os.path.join('test', 'results')
        simple_output = True

        self.coordinator.execute_operations(ids, device_info, results_dir_path, simple_output)

    def tearDown(self):
        os.remove(os.path.join('test', 'definitions.db'))

if __name__ == '__main__':
    unittest.main()
