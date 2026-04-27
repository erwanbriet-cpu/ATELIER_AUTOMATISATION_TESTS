def run_contract_tests(response):
    if response is None: return False, "Erreur Réseau"
    
    data = response.json()
    results = {
        "http_200": response.status_code == 200,
        "is_json": 'application/json' in response.headers.get('Content-Type', ''),
        "has_places": 'places' in data,
        "is_list": isinstance(data.get('places'), list),
        "not_empty": len(data.get('places')) > 0,
        "fast_enough": response.elapsed.total_seconds() < 2
    }
    
    return all(results.values()), str(results)