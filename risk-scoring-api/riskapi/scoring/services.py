def calculate_risk_score(data):
    risk_score = 0
    breakdown = {}
    
    # Rule 1: Region and data sensitivity
    if data.get('region') == 'EU' and data.get('data_sensitivity') == 'high':
        risk_score += 30
        breakdown['region_and_sensitivity'] = 30
    
    # Rule 2: Processor name
    if data.get('processor_name') == 'UnknownVendor':
        risk_score += 20
        breakdown['processor_risk'] = 20
    
    # Rule 3: Purpose
    if data.get('purpose') == 'marketing':
        risk_score += 15
        breakdown['purpose_risk'] = 15
    
    # Cap at 100
    risk_score = min(risk_score, 100)
    
    return {
        'risk_score': risk_score,
        'risk_breakdown': breakdown
    }