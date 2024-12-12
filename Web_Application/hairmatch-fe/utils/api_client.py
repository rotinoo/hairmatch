import requests
import io
import csv

BASE_URL = "https://hairmatch-be-550434348755.asia-southeast1.run.app"

def detect_face_type(image):
    try:
        # Convert the image to binary data
        image_binary = io.BytesIO()
        image.save(image_binary, format="JPEG")
        image_binary.seek(0)

        # Simulate a file upload
        files = {"image": ("image.jpg", image_binary, "image/jpeg")}

        response = requests.post(
            f"{BASE_URL}/api/detect/face",
            files=files,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data.get("tipe_wajah", "Unknown")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

def detect_hair_type(image):
    try:
        # Convert the image to binary data
        image_binary = io.BytesIO()
        image.save(image_binary, format="JPEG")
        image_binary.seek(0)

        # Simulate a file upload
        files = {"image": ("image.jpg", image_binary, "image/jpeg")}

        response = requests.post(
            f"{BASE_URL}/api/detect/hair",
            files=files,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data.get("tipe_rambut", "Unknown")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

def fetch_recommendations(face_type, hair_type, csv_file_path):
    try:
        # Fetch recommendations from the API
        response = requests.post(
            f"{BASE_URL}/api/recommend",
            json={"tipe_wajah": face_type, "tipe_rambut": hair_type},
            timeout=30
        )
        response.raise_for_status()
        api_data = response.json()

        # Extract recommended categories and their descriptions
        recommended_categories = {
            item["nama"].replace(" ", "_"): item["penjelasan"]
            for item in api_data.get("gaya_rambut", [])
        }

        # Open CSV file and normalize headers
        recommendations = {}
        with open(csv_file_path, "r", encoding="utf-8-sig") as file:  # Use utf-8-sig to handle BOM
            reader = csv.DictReader(file)
            headers = {header.strip().replace(" ", "_"): header.strip() for header in reader.fieldnames}  # Normalize headers

            # Check if 'Category' exists in the normalized headers
            if "Category" not in headers:
                raise KeyError("CSV file missing 'Category' column. Ensure the header is correctly spelled and formatted.")

            # Process rows in the CSV
            for row in reader:
                category = row[headers["Category"]].strip()

                if category in recommended_categories:
                    # Initialize the recommendation entry if it doesn't exist
                    if category not in recommendations:
                        recommendations[category] = {
                            "name": category.replace("_", " "),
                            "urls": [],
                            "description": recommended_categories[category],  # Use API description
                        }

                    # Append URL to the recommendation entry
                    file_url = row.get(headers.get("File_URL", "")).strip()
                    if file_url:  # Ensure the URL exists before appending
                        recommendations[category]["urls"].append(file_url)

        # Convert recommendations dictionary to a list
        recommendations_list = [
            {"name": rec["name"], "urls": rec["urls"], "description": rec["description"]}
            for rec in recommendations.values()
        ]

        return recommendations_list

    except KeyError as e:
        print(f"KeyError: {e}. Ensure the CSV contains all required columns (e.g., 'Category', 'File_URL').")
        return []
    except FileNotFoundError:
        print(f"Error: The CSV file at '{csv_file_path}' was not found. Check the file path.")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Error: API request failed - {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
