# coding=utf-8
import unittest
from components.definitions_database import DefinitionsDatabase
from model import DataSource, DeviceInfo


class MyTestCase(unittest.TestCase):
    def test_something(self):
        db_helper = DefinitionsDatabase('definitions.db',
                                        '../my_test_create_db.sql',
                                        '../my_test_insert_default_operations.sql')
        ds = DataSource('Application', {'package_name': 'com.android.email'})
        bad_ds = DataSource('Application', {})
        dv_info = DeviceInfo('3.0.0', 'GT-I9300')

        print db_helper.query_operations_info('EmailMessage', ds, dv_info)

        self.assertEqual(db_helper.query_operations_info('Non_existent', ds, dv_info), [])

        self.assertEqual(db_helper.get_operation_exec_info('operation_1'),
                         {'extractor_id': 'ApplicationExtractor', 'inspector_id': 'EmailMessageInspector',
                          'param_values': {'package_name': 'com.android.email'}})
        self.assertEqual(db_helper.get_operation_exec_info('id_non_existent'), {})

        self.assertTrue(db_helper.exists_operation('operation_1'))
        self.assertFalse(db_helper.exists_operation('Non_existent'))

        self.assertTrue(db_helper.exists_data_type('EmailMessage'))
        self.assertFalse(db_helper.exists_data_type('Non_existent'))

        self.assertTrue(db_helper.exists_data_source_type('Application'))
        self.assertFalse(db_helper.exists_data_source_type('Non_existent'))

        self.assertTrue(db_helper.has_all_required_param_values(ds))
        self.assertFalse(db_helper.has_all_required_param_values(bad_ds))


if __name__ == '__main__':
    unittest.main()
