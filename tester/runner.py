from tester.client import call_api
from tester.tests import run_contract_tests
import storage

def execute_full_run():
    url = "https://api.zippopotam.us/us/90210"
    
    # 1. Appel
    resp, lat = call_api(url)
    
    # 2. Tests
    success, metrics = run_contract_tests(resp)
    
    # 3. Sauvegarde
    status = resp.status_code if resp else 500
    storage.save_run(status, lat, 1 if success else 0, metrics)