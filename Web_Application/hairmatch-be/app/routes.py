from flask import Blueprint, request, jsonify
import os
from .models import load_models, predict_image
from .utils import save_uploaded_file, clean_up_file, recomendation

# Blueprint for organizing routes
bp = Blueprint('api', __name__)

face_shape_model, hair_type_model, face_classes, hair_classes = load_models()

@bp.route('/api/detect/face', methods=['POST'])
def detect_face():
    image = request.files.get('image')
    if not image:
        return jsonify({"error": "No image uploaded"}), 400

    image_path = save_uploaded_file(image)
    try:
        face_type = predict_image(image_path, face_shape_model, face_classes)
        clean_up_file(image_path)
        return jsonify({"tipe_wajah": face_type})
    except Exception as e:
        clean_up_file(image_path)
        return jsonify({"error": str(e)}), 500

@bp.route('/api/detect/hair', methods=['POST'])
def detect_hair():
    image = request.files.get('image')
    if not image:
        return jsonify({"error": "No image uploaded"}), 400

    image_path = save_uploaded_file(image)
    try:
        hair_type = predict_image(image_path, hair_type_model, hair_classes)
        clean_up_file(image_path)
        return jsonify({"tipe_rambut": hair_type})
    except Exception as e:
        clean_up_file(image_path)
        return jsonify({"error": str(e)}), 500

@bp.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.json
    
    # Validate request body
    if not data or "tipe_wajah" not in data or "tipe_rambut" not in data:
        return jsonify({"error": "Missing 'tipe_wajah' or 'tipe_rambut' in request"}), 400

    # Extract the input values
    tipe_wajah = data["tipe_wajah"]
    tipe_rambut = data["tipe_rambut"]

    # Use the recomendation function to get recommendations
    recommendations = recomendation(tipe_rambut, tipe_wajah)

    # Check if recommendations are empty
    if not recommendations:
        return jsonify({"error": "No recommendations found for the given inputs"}), 404

    # Prepare the response with directory URLs
    response = [
        {
            "nama": rec["style"],  # Hairstyle name
            "penjelasan": rec["explanation"]  # Hairstyle explanation
        }
        for rec in recommendations
    ]

    # Return the response as JSON
    return jsonify({"gaya_rambut": response}), 200
