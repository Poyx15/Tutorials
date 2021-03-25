import json

water_level = '''
{
    "status": [
        {
            "level": "level 1",
            "action": "SMS only",
            "message": "Alert level 1",
            "test": true
        },
        {
            "level": "level 2",
            "action": "SMS only",
            "message": "Alert level 2",
            "test": true
        },
        {
            "level": "level 3",
            "action": "SMS only",
            "message": "Alert level 3",
            "test": false
        },
        {
            "level": "level 4",
            "action": "SMS and Override FM",
            "message": "Alert level 4",
            "test": true
            
        },
        {
            "level": "level 5",
            "action": "SMS and override FM",
            "message": "Alert level 5: force evacuation",
            "test": false
        }
    ]
}
'''

data = json.loads(water_level)


for water_level in data['status']:
    del water_level['level']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)