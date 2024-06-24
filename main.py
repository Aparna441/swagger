import json

def main():
    try:
        with open('https://petstore.swagger.io/v2/swagger.json', 'r') as f:
            json_data = f.read()
            data = json.loads(json_data)
            print("JSON data parsed successfully:")
            print(data)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")

if __name__ == "__main__":
    main()

