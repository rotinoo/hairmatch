# API Documentation

## Base URL
The base URL of the API will depend on the deployment environment. For example, if deployed on Google Cloud Run, it will look something like:

```
https://<your-service-url>/api
```

---

## Endpoints

### 1. **Detect Face Type**
**Endpoint:**
```
POST /api/detect/face
```

**Description:**
Uploads an image to predict the face type.

**Request:**
- **Headers:**
  - `Content-Type: multipart/form-data`
- **Body:**
  - `image` (required): The image file of a face to analyze.

**Response:**
- **200 OK**
```json
{
  "tipe_wajah": "Oval"
}
```
- **400 Bad Request**
```json
{
  "error": "No image uploaded"
}
```
- **500 Internal Server Error**
```json
{
  "error": "<error message>"
}
```

### 2. **Detect Hair Type**
**Endpoint:**
```
POST /api/detect/hair
```

**Description:**
Uploads an image to predict the hair type.

**Request:**
- **Headers:**
  - `Content-Type: multipart/form-data`
- **Body:**
  - `image` (required): The image file of hair to analyze.

**Response:**
- **200 OK**
```json
{
  "tipe_rambut": "Curly"
}
```
- **400 Bad Request**
```json
{
  "error": "No image uploaded"
}
```
- **500 Internal Server Error**
```json
{
  "error": "<error message>"
}
```

### 3. **Get Hairstyle Recommendations**
**Endpoint:**
```
POST /api/recommend
```

**Description:**
Provides hairstyle recommendations based on the detected face type and hair type.

**Request:**
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
  ```json
  {
    "tipe_wajah": "Oval",
    "tipe_rambut": "Curly"
  }
  ```

**Response:**
- **200 OK**
```json
{
  "gaya_rambut": [
    {
      "nama": "Afro",
      "gambar": "https://example.com/afro.jpg"
    },
    {
      "nama": "Pompadour",
      "gambar": "https://example.com/pompadour.jpg"
    }
  ]
}
```
- **400 Bad Request**
```json
{
  "error": "Missing 'tipe_wajah' or 'tipe_rambut' in request"
}
```

---

## Error Codes
### Common Error Responses
| Code | Message                         | Description                                     |
|------|---------------------------------|-------------------------------------------------|
| 400  | Bad Request                     | Missing or invalid parameters in the request.   |
| 500  | Internal Server Error           | Unexpected server error. Check the error message for details. |

---

## Example Usage

### Curl Command to Detect Face Type
```bash
curl -X POST \
     -F "image=@/path/to/image.jpg" \
     https://<your-service-url>/api/detect/face
```

### Curl Command to Detect Hair Type
```bash
curl -X POST \
     -F "image=@/path/to/image.jpg" \
     https://<your-service-url>/api/detect/hair
```

### Curl Command to Get Recommendations
```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"tipe_wajah": "Oval", "tipe_rambut": "Curly"}' \
     https://<your-service-url>/api/recommend
```

