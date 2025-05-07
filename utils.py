import json
from datetime import datetime

def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def export_to_file(data, file_path, format_type='txt'):
    try:
        if format_type == 'json':
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        else:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(data)
        return True
    except Exception as e:
        print(f"Export Error: {str(e)}")
        return False