'''
Created on Jun. 11, 2019

@author: KJNETHER
'''
import pytest
from bcdc_apitests.fixtures.packages \
    import \
        package_create_if_not_exists, \
        test_valid_package_exists, \
        test_invalid_package_exists, \
        package_get_id_fixture
# from bcdc_apitests.fixtures.packages import *
# from bcdc_apitests.fixtures.ckan import *
# from bcdc_apitests.fixtures.load_config import *
# from bcdc_apitests.fixtures.load_data import *
# from bcdc_apitests.fixtures.config_fixture import *
# from bcdc_apitests.fixtures.orgs import *

from bcdc_apitests.fixtures.resources \
    import \
        resource_get_id_fixture, \
        res_create_if_not_exists, \
        resource_delete_if_exists, \
        resource_teardown, \
        get_resource_fixture
        
        
# post test cleanup removal of pkg if previous test fails. this is to be apart of the pre/post run at module level
# TODO: move this into a conftest
@pytest.fixture(scope='module')
def test_post_cleanup(remote_api_super_admin_auth, test_package_name):
    '''
    call delete on all resources that are part of the package, and 
    then delete the package.
    
    '''
    resource_teardown(remote_api_super_admin_auth, test_package_name)

